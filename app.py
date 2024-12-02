from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    data = [
        {
            "description": "To maximize your score, you should be able to check off as many of the following as possible...",
            "file_link": "No File Link",
            "publication_date": "Unknown",
            "read_time": "0 mins",
            "sections": {
                "Academic honesty": "This is extremely important in all your work..."
            },
            "subject": "Math AI SL",
            "title": "IA Checklist",
            "word_count": 41
        },
        {
            "description": "To maximize your score......",
            "file_link": "No File Link",
            "publication_date": "Unknown",
            "read_time": "0 mins",
            "sections": {
                "Academic honesty": "This is extremely important in all your work. and software is ....."
            },
            "subject": "Software AI SL",
            "title": "IA Checklist 2",
            "word_count": 42
        }
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
