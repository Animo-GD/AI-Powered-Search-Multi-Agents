import gradio as gr
from dotenv import load_dotenv
import agentops
from crew import crew
import os
from llm_manager.BasicModel import BasicModel

os.chdir(os.path.join(os.getcwd(), "src"))



def run_pipeline(company_name, product_name, web_sites, no_keywords, country_name, score_th, language, top_recommendations_no,openai_api,scrape_api,tavily_api):


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
    load_dotenv()
    os.environ["SCRAPE_API_KEY"] = scrape_api if scrape_api!="" else os.getenv("SCRAPE_API_KEY")
    os.environ["TAVILY_API_KEY"] = tavily_api if tavily_api!="" else os.getenv("TAVILY_API_KEY")
    os.environ["OPENAI_API_KEY"] = openai_api if openai_api!="" else os.getenv("OPENAI_API_KEY")
    os.environ["LITELLM_API_BASE"] = "https://openrouter.ai/api/v1"
    os.environ["OPENROUTER_API_KEY"] = openai_api if openai_api!="" else os.getenv("OPENAI_API_KEY")
    about_company = f"{company_name} is a personal startup company interested in AI Tech"
    main_crew = crew(about_company=about_company)
    main_crew.start_crew(input_params=inputs)

    html_file = os.path.join("data", "FinalReport.html")
    if not os.path.exists(html_file):
        return "<h2>No output file found!</h2>", None


    return html_file


if __name__ == "__main__":
    with gr.Blocks(title="Product Search Agent") as demo:
        gr.Markdown("## 🔍 AI-Powered Product Search Agent")

        with gr.Row():
            with gr.Column(scale=1):
                company = gr.Textbox(label="Company Name", value="Moaaz")
                product = gr.Textbox(label="Product Name", value="Nvidia GTX")
                sites = gr.Textbox(label="Websites (comma separated)", value="amazon.com,sigma-computer.com,ahw.com")
                keywords = gr.Number(label="Number of Keywords", value=5)
                country = gr.Textbox(label="Country Name", value="Egypt")
                score = gr.Number(label="Score Threshold", value=0.30)
                language = gr.Textbox(label="Language", value="English")
                topn = gr.Number(label="Top Recommendations", value=10)
                # 🔑 Accordion for API Keys
                with gr.Accordion("🔑 API Keys (Required*)", open=False):
                    openai_api = gr.Textbox(label="OpenRouter API Key", type="password", placeholder="Leave blank to use .env")
                    scrape_api = gr.Textbox(label="Scrape API Key", type="password", placeholder="Leave blank to use .env")
                    tavily_api = gr.Textbox(label="Tavily API Key", type="password", placeholder="Leave blank to use .env")

                

                start_btn = gr.Button("🚀 Start Search", variant="primary")

            with gr.Column(scale=2):
                download_btn = gr.File(label="⬇️ Download Final Report")

        # Button logic
        start_btn.click(
            fn=run_pipeline,
            inputs=[company, product, sites, keywords, country, score, language, topn,
                    openai_api,scrape_api,tavily_api],
            outputs=[download_btn]
        )

    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
