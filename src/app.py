import time
import gradio as gr
import os
from crew import crew
from llm_manager.BasicModel import BasicModel
import agentops

def env_setup():
    agentops.init(
        api_key=os.getenv("AGENTOPS_API_KEY"),
        skip_auto_end_session=True
    )

def run_pipeline(company_name,about_company, product_name, web_sites, no_keywords, country_name, score_th, language, top_recommendations_no, progress=gr.Progress()):
    progress(0, desc="Starting pipeline...")

    inputs = {
        "company_name": company_name,
        "product_name": product_name,
        "web_sites": [s.strip() for s in web_sites.split(",")],
        "no_keywords": int(no_keywords),
        "country_name": country_name,
        "score_th": float(score_th),
        "language": language,
        "top_recommendations_no": int(top_recommendations_no),
    }

    about_company = f"{company_name} :{about_company}"

    progress(0.2, desc="Setting up environment...")
    env_setup()

    progress(0.4, desc="Loading LLM...")
    base_llm = BasicModel().get_llm()

    progress(0.6, desc="Running Crew pipeline...")
    main_crew = crew(llm=base_llm, about_company=about_company)
    main_crew.start_crew(input_params=inputs)

    progress(0.9, desc="Generating Final Report...")
    html_file = os.path.join("data", "FinalReport.html")
    if not os.path.exists(html_file):
        return "<h2>No output file found!</h2>"

    progress(1.0, desc="Done ✅")
    file_url = f"/file={html_file}"
    return f"""
        <a href="{file_url}" target="_blank">
            <button style="padding:10px 20px; font-size:16px; border-radius:8px; background:#4CAF50; color:white; border:none; cursor:pointer;">
                📄 Open Final Report
            </button>
        </a>
    """

if __name__ == "__main__":
    demo = gr.Interface(
        fn=run_pipeline,
        inputs=[
            gr.Textbox(label="Company Name", value="Moaaz"),
            gr.Textbox(label="About Company", value="A personal startup company interested in AI Tech"),
            gr.Textbox(label="Product Name", value="Coffee machine"),
            gr.Textbox(label="Websites (comma separated)", value="amazon.com,jumia.com,noon.com"),
            gr.Number(label="Number of Keywords", value=5),
            gr.Textbox(label="Country Name", value="Egypt"),
            gr.Number(label="Score Threshold", value=0.30),
            gr.Textbox(label="Language", value="English"),
            gr.Number(label="Top Recommendations", value=10),
        ],
        outputs=gr.HTML(label="Results"),
        title="Product Search Agent",
        description="Fill in the parameters and run the AI-powered product search."
    )

    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
