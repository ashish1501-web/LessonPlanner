import json
from duckduckgo_search import DDGS
def fetch_links():
    input_text = input("Enter the topic:")

    input_text_gfg= input_text + "by Geeks For Geeks"
    input_text_javat= input_text + "by Javatpoint"
    urls=[]
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(input_text_gfg, max_results=1)]
        for dict in results:
           urls.append(dict["href"])
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(input_text_javat, max_results=1)]
        for dict in results:
            urls.append(dict["href"])
    return urls