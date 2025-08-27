from pydantic import BaseModel,Field
from typing import List,Optional
from crewai.tools import tool
from scrapegraph_py import Client
from tavily import TavilyClient
no_keywords = 10
import os
from dotenv import load_dotenv


class ResultQueires(BaseModel):
        queries:List[str] = Field(
            ...,
            description="Queries that will be passed to the search enigne",
            min_items=1,maxitems=no_keywords
            )
        

class SignleSearchResult(BaseModel):
    title : Optional[str]
    url: str = Field(..., title="the page url")
    content: str
    score: float
    search_query:str

class AllSearchResults(BaseModel):
    results: List[SignleSearchResult]



class ProductSpec(BaseModel):
        specification_name: str
        specification_value: str

class SingleExtractedProduct(BaseModel):
        page_url: str = Field(..., title="The original url of the product page")
        product_title: str = Field(..., title="The title of the product")
        product_image_url: str = Field(..., title="The url of the product image")
        product_url: str = Field(..., title="The url of the product")
        product_current_price: float = Field(..., title="The current price of the product")
        product_original_price: float = Field(title="The original price of the product before discount. Set to None if no discount", default=None)
        product_discount_percentage: float = Field(title="The discount percentage of the product. Set to None if no discount", default=None)
        product_specs: List[ProductSpec] = Field(..., title="The specifications of the product. Focus on the most important specs to compare.", min_items=1, max_items=5)

        agent_recommendation_rank: int = Field(..., title="The rank of the product to be considered in the final procurement report. (out of 5, Higher is Better) in the recommendation list ordering from the best to the worst")
        agent_recommendation_notes: List[str]  = Field(..., title="A set of notes why would you recommend or not recommend this product to the company, compared to other products.")


class AllExtractedProducts(BaseModel):
        products: List[SingleExtractedProduct]

@tool
def search_engine_tool(query:str):
        """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
        load_dotenv()
        search_client= TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        return search_client.search(query=query,max_results=5)
    

@tool
def scraper_tool(page_url:str):
        """
        An AI Tool to help an agent to scrape a web page

         Example:
                web_scraping_tool(
                  page_url="https://www.noon.com/egypt-en/search/?q=espresso%20machine"
                 )
         """
        load_dotenv()
        scraper = Client(api_key=os.getenv("SCRAPE_API_KEY"))
        details = scraper.smartscraper(
              website_url=page_url,
              user_prompt="Extract ```json\n"+SingleExtractedProduct.schema_json()+"```\n from the provided web page"
        )
        return {
              "page_url":page_url,
              "details":details
        }