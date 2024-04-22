import scrapy
import streamlit as st
from scrapy.selector import Selector
import asyncio
import sys
sys.path.append(r'C:/Users/aharakun/Downloads/lessonplanner-main/WebScraper/WebScraper')
import fetch_url
from fetch_url import fetch_links
import sys
sys.path.append(r'C:/Users/aharakun/Downloads/lessonplanner-main/WebScraper/WebScraper/spiders')
from get_topic import get_topic_to_scrape

class TitleSpider(scrapy.Spider):
    name = 'LessonPlanner'
    topic = input("Enter the Topic")
    # topic=get_topic_to_scrape()
    print(topic)
    print("222222222222222222222222222222222222222222222")
    start_urls = asyncio.run(fetch_links(topic))
    for i in start_urls:
        print(i)
    
    def parse(self, response):
        html_content = ''''''
        if "geeksforgeeks" in response.url:
            contents = response.css('.content').extract()
        if "javatpoint" in response.url:
            contents = response.css('.onlycontent .onlycontentinner').extract()
        for content in contents:
            html_content += content
        selector = Selector(text=html_content)
        text = selector.xpath('string()').extract()
        s = ""
        for i in text:
            s += i
        # clean the data
        import re
        cleaned_data = re.sub(r'\[|\]|\'|\,|\t|\r', '', s)
        # cleaned_text = re.sub(r'\s{1,}', ' ', cleaned_data)
        cleaned_text = cleaned_data.strip()

        output_file="result_from_"
        if "geeksforgeeks" in response.url:
            output_file+="geeks_for_geeks.txt"
        if "javatpoint" in response.url:
            output_file+="javatpoint.txt"
        # store the extracted content in file
        with open(output_file, "w",encoding='utf-8') as file:
            file.write(cleaned_text)
        print(cleaned_text)