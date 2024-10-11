from flask import Flask, jsonify, render_template
import pandas as pd
import datetime
import requests
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load the cleaned data (assuming it is saved in a JSON file)
df = pd.read_json('cleaned_browser_history.json')

# Route for the homepage
API_URL = "https://api.linkpreview.net"
API_KEY = "MY_API_KEY"


@app.route('/')
def index():
    return render_template('GoogleWrapped.html')

# API to get top sites


def get_site_metadata(url):
    """Fetch metadata for a given URL using the LinkPreview API."""
    params = {'key': API_KEY, 'q': url}
    try:
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()  # Returns title, description, image, etc.
        return {"url": url, "title": "No title found", "description": "No description found", "image": ""}
    except Exception as e:
        return {"url": url, "title": "Error fetching data", "description": str(e), "image": ""}


@app.route('/api/top-sites')
def top_sites():
    top_sites = df['url'].value_counts().head(5).to_dict()

    # Create a list to hold the metadata for the top sites
    metadata_list = []

    # Fetch metadata for each top site URL
    for url in top_sites.keys():
        site_metadata = get_site_metadata(url)
        metadata_list.append(site_metadata)

    return jsonify(metadata_list)


# API to get daily visits


@app.route('/api/daily-visits', methods=['GET'])
def daily_visits():
    # Example daily_visits_count is a dictionary with datetime.date as keys
    daily_visits_count = {datetime.date(
        2024, 5, 11): 5, datetime.date(2024, 6, 12): 10}

    # Convert datetime.date keys to strings
    daily_visits_count_str = {
        k.isoformat(): v for k, v in daily_visits_count.items()}

    return jsonify({'daily_visits': daily_visits_count_str})


@app.route('/api/monthly-visits', methods=['GET'])
def monthly_visits():
    # Example monthly_visits_count is a dictionary with pandas.Period as keys
    import pandas as pd
    monthly_visits_count = {
        pd.Period('2024-05', 'M'): 100, pd.Period('2024-06', 'M'): 120}

    # Convert pandas.Period keys to strings
    monthly_visits_count_str = {k.strftime(
        '%Y-%m'): v for k, v in monthly_visits_count.items()}

    return jsonify({'monthly_visits': monthly_visits_count_str})


@app.route('/api/daily-visits-chart', methods=['GET'])
def daily_visits_chart():
    # Example daily_visits is a dictionary with datetime.date as keys
    daily_visits = {datetime.date(2024, 1, 1): 5,
                    datetime.date(2024, 9, 9): 10}

    # Convert datetime.date keys to strings
    daily_visits_str = {k.isoformat(): v for k, v in daily_visits.items()}

    return jsonify(daily_visits_str)

# API to generate word cloud


@app.route('/api/wordcloud')
def wordcloud():
    text = " ".join(df['title'].dropna())
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white').generate(text)

    img = io.BytesIO()
    wordcloud.to_image().save(img, format='PNG')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    return jsonify({'wordcloud': img_base64})


if __name__ == '__main__':
    app.run(debug=True)
