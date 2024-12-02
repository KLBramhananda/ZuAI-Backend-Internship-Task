import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import json

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["nailib_data"]
collection = db["samples"]

# Scraping function
def scrape_data(url):
    response = requests.get(url)
    
    # Check if the response is valid (status code 200)
    if response.status_code == 200:
        print(f"Successfully fetched HTML content from: {url}")
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract data
        title = soup.find("h1").text.strip() if soup.find("h1") else "Unknown"
        subject = "Math AI SL"  # Modify based on extraction logic
        description = soup.find("p").text.strip() if soup.find("p") else "No Description"
        
        # Extract sections (based on your task details)
        sections = {}
        section_titles = soup.find_all("h2")  # Assuming section titles are in <h2> tags
        for title_tag in section_titles:
            section_title = title_tag.text.strip()  # Extract text content from the <h2> tag
            section_content = title_tag.find_next("p").text.strip() if title_tag.find_next("p") else "No Content"
            sections[section_title] = section_content
        
        # Extract file links
        file_links = [a['href'] for a in soup.find_all('a', href=True) if "pdf" in a['href']]
        file_link = file_links[0] if file_links else "No File Link"
        
        # Extract publication date (modify selector as per page structure)
        pub_date_tag = soup.find("time")
        publication_date = pub_date_tag.text.strip() if pub_date_tag else "Unknown"

        # Compute word count and read time
        word_count = len(description.split()) if description != "No Description" else 0
        read_time = f"{round(word_count / 200)} mins" if word_count > 0 else "Not available"

        # Example: Extract checklist items
        checklist_items = [li.text.strip() for li in soup.find_all("li")]
        sections["Checklist"] = checklist_items

        # Create the data to be inserted into MongoDB
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
        
        # Upsert to MongoDB
        collection.update_one({"title": title}, {"$set": data}, upsert=True)
        print(f"Data inserted/updated for: {title}")
    else:
        print(f"Failed to fetch URL: {url}, Status Code: {response.status_code}")

# Export data from MongoDB to a JSON file
def export_to_json(file_name):
    data = list(collection.find({}, {"_id": 0}))  # Exclude _id from the output
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data exported to {file_name}")

# List of URLs to scrape
urls = [
    "https://nailib.com/ia-sample/ib-math-ai-sl/63909fa87396d2b674677e94",
    # Add more URLs here
]

# Run the scraper for each URL
for url in urls:
    scrape_data(url)

# Export data to JSON
export_to_json("nailib_data.json")
