import sys
sys.path.append(r'C:/Users/aharakun/Downloads/lessonplanner-main/WebScraper/WebScraper')
import fetch_url
from fetch_url import fetch_links
links=fetch_links()
print(links)
