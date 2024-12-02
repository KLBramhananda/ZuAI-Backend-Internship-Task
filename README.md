# IB Math IA & EE Scraping and Data Storage Application

## Objective

This project focuses on scraping IB Math AI SL IA (Internal Assessment) and EE (Extended Essay) samples from the Nailib website. The goal is to extract key data from these pages, clean and store it in a MongoDB database for easy access and further processing.

## Features

### Data Extraction
- Scrapes the following key data from IB Math IA SL and EE sample pages:
  - **Title**: Name of the IA or EE.
  - **Subject**: Example - Math AI SL.
  - **Description**: Checklist or instructions.
  - **Sections**: Extracts content under different sections like:
    - Introduction, Mathematical Information, etc.
  - **Word Count**: Extracted word count.
  - **Read Time**: Estimated time to read.
  - **File Link**: Links to downloadable files if available.
  - **Publication Date**: If available, stores the date of publication.

### Data Processing & Storage
- **Data Cleaning**: Cleans the data by removing unnecessary spaces and handling missing fields.
- **MongoDB Integration**: 
  - Stores extracted data in MongoDB using a simple schema.
  - Prevents duplication using MongoDB's upsert functionality.

### Error Handling
- The application handles potential errors like network issues or missing data gracefully.

### Bonus Features (Optional)
- **Automation**: Automates scraping at regular intervals using Cron.
- **REST API**: Creates an API to access the scraped data from MongoDB.
- **Dockerization**: The solution is dockerized for portability and easy deployment.

## Technologies Used

- **Python**: For building the scraper and handling the backend logic.
- **Libraries**:
  - **BeautifulSoup** or **Selenium** for scraping web data.
  - **PyMongo** for storing and querying data in MongoDB.
- **Docker**: For containerizing the application (bonus feature).
- **Cron**: For automating the scraping process (bonus feature).

## Project Setup

### Prerequisites

- **Python 3.x** and **pip** (Python package installer).
- **MongoDB** installed locally or a cloud-based MongoDB service.

### Steps to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/KLBramhananda/ZuAI-Backend-Internship-Task

 
## Install dependencies:

cd document-capture-scraping
pip install -r requirements.txt

# Run the backend:

python app.py

(Optional) If you want to view the scraped data in a frontend React app:

# Navigate to the react-frontend folder:

cd react-frontend
Install the necessary dependencies:

npm install
Start the React app:

npm start
Docker (Optional)

## Build and run the Docker container:

docker build -t document-capture-scraping .
docker run -p 5000:5000 document-capture-scraping

### How It Works

Scraping: Scrapes IB Math IA SL and EE data from Nailib.
Data Cleaning: Ensures the extracted data is formatted properly.
MongoDB Storage: Stores the data in MongoDB, preventing duplicates.
API Access: Exposes a REST API to query and retrieve the data.
Automation: Sets up Cron to run the scraper at intervals for updated data.

## Evaluation Criteria
Data Accuracy: Correctly extracted, cleaned, and structured data.
Code Quality: Clean, readable, and well-documented code.
MongoDB Integration: Proper data storage and querying.
Error Handling: Proper handling of edge cases and errors.
Presentation: Clear project setup instructions and well-documented GitHub repository.

## Contributions
Feel free to fork this project, raise issues, or create pull requests. Contributions and suggestions are welcome!


## License
This project is licensed under the MIT License.

This **README.md** is simple, concise, and gives a clear overview of your project while highlightin

