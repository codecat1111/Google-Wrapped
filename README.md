# Google-Wrapped 📊  
A knockoff of Spotify Wrapped using **Google Search History**, **YouTube History**, and other Google data, displayed with statistical insights using **Pandas**, **Flask**, and **JavaScript**. This project extracts user data through **Google Takeout** and offers a detailed breakdown of browsing patterns, top sites, daily/weekly visits, and even generates a **word cloud** of visited site titles.

---

## Table of Contents
- [Google Export Guide](#google-export-guide)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [API Calls](#api-calls)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Google Export Guide
To use this application, you'll need your Google data. Follow these steps to export your data:

1. **Visit** [Google Takeout](https://takeout.google.com/).
2. **Select** the following services:
   - **Search History**
   - **YouTube History**
   - (Optional) Other Google services you want to include.
3. **Export your data** and download the JSON files.
4. **Place the exported files** in the project folder.
5. **Clean the data** (if necessary) and save it as `cleaned_browser_history.json` for use in the application.

---

## Features
- **Detailed Browser Fingerprint** using the [FingerprintJS library](https://fingerprint.com/).  
- **Daily and Monthly Visits** summary with **interactive charts**.  
- **Top Sites Metadata** fetched from the **LinkPreview API**.  
- **Word Cloud Generation** of visited site titles using **WordCloud**.  
- **Data visualization** using **Pandas** and **Matplotlib**.  
- **Responsive web interface** powered by Flask with **HTML/CSS**.

---

## Demo
![Demo GIF](https://via.placeholder.com/800x400?text=Demo+Coming+Soon)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Google-Wrapped.git
   cd Google-Wrapped
   ```
2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   .\env\Scripts\activate   # For Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Place your Google Export data (BrowserHistory.json, YouTube History.json, etc.) inside the project folder and clean the data to match your requirements. Save it as cleaned_browser_history.json.**
5. **Add your LinkPreview API key**
     
      Create an account at LinkPreview to get your API key. Replace MY_API_KEY in app.py with your API key.
  
7. **Run the Flask application**:
  ```bash
  python app.py
  ```
7. **Open localhost in your browser to view the app.**

## API Calls:

1. Top Sites Metadata:
```bash
GET /api/top-sites
```
2. Daily Visits:
```bash
GET /api/daily-visits
```
3. Monthly Visits:
```bash
GET /api/monthly-visits
```
4. Word Cloud Generation:
```bash
GET /api/wordcloud
```
