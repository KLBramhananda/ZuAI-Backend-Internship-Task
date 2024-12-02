import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["nailib_data"]
collection = db["samples"]

def scrape_data(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Successfully fetched HTML content from: {url}")
        soup = BeautifulSoup(response.content, "html.parser")
        
        title = soup.find("h1").text.strip() if soup.find("h1") else "Unknown"
        subject = "Math AI SL"
        description = soup.find("p").text.strip() if soup.find("p") else "No Description"
        
        sections = {}
        section_titles = soup.find_all("h2")
        for title_tag in section_titles:
            section_title = title_tag.text.strip()
            section_content = title_tag.find_next("p").text.strip() if title_tag.find_next("p") else "No Content"
            sections[section_title] = section_content
        
        file_links = [a['href'] for a in soup.find_all('a', href=True) if "pdf" in a['href']]
        file_link = file_links[0] if file_links else "No File Link"
        
        pub_date_tag = soup.find("time")
        publication_date = pub_date_tag.text.strip() if pub_date_tag else "Unknown"

        word_count = len(description.split()) if description != "No Description" else 0
        read_time = f"{round(word_count / 200)} mins" if word_count > 0 else "Not available"

        checklist_items = [li.text.strip() for li in soup.find_all("li")]
        sections["Checklist"] = checklist_items

        data = {
            "title": title,
            "subject": subject,
            "description": description,
            "sections": sections,
            "word_count": word_count,
            "read_time": read_time,
            "file_link": file_link,
            "publication_date": publication_date
        }
        
        collection.update_one({"title": title}, {"$set": data}, upsert=True)
        print(f"Data inserted/updated for: {title}")
    else:
        print(f"Failed to fetch URL: {url}, Status Code: {response.status_code}")

def export_to_json(file_name):
    data = list(collection.find({}, {"_id": 0}))
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data exported to {file_name}")

urls = [
    "https://nailib.com/ia-sample/ib-math-ai-sl/63909fa87396d2b674677e94",
]

for url in urls:
    scrape_data(url)

export_to_json("nailib_data.json")
