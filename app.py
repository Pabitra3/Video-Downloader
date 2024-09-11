import os
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)
DOWNLOAD_FOLDER = 'downloads'

# Ensure download folder exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Function to download video from URL
def download_video(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    result = None

    # Search for the video URL
    for val in soup.findAll("script"):
        if re.search("talkPage.init", str(val)) is not None:
            result = str(val)
            break

    if result is None:
        raise Exception("Could not find the video in the URL")

    # Extract the MP4 URL from the script
    mp4_url = re.search(r"(?P<url>https?://[^\s]+)(mp4)", result).group("url")
    mp4_url = mp4_url.split('"')[0]
    file_name = mp4_url.split("/")[-1].split('?')[0]
    
    # Download the video
    r = requests.get(mp4_url)
    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)
    with open(file_path, 'wb') as f:
        f.write(r.content)

    return file_name

# Route to the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and download the video
@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        file_name = download_video(url)
        return redirect(url_for('downloaded', filename=file_name))
    except Exception as e:
        return f"An error occurred: {e}"

# Route to serve the downloaded file
@app.route('/downloaded/<filename>')
def downloaded(filename):
    return render_template('download.html', filename=filename)

@app.route('/files/<filename>')
def files(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
