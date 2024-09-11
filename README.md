# Video-Downloader

## Overview
This project is a web-based application that allows users to download videos from the internet by entering a video URL. The application scrapes the video link from the URL and downloads the video directly to the server. Users can then download the video file via a provided link.

## Features
- **Web Scraping**: Uses `BeautifulSoup` and `requests` to scrape video content from a webpage.
- **Video Download**: Automatically downloads the video from the extracted video URL.
- **Simple User Interface**: Allows users to enter the video URL and download the video.

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Web Scraping**: `BeautifulSoup`, `requests`
- **Regex Matching**: Used to find the video URL in the HTML response

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- Flask
- Requests
- BeautifulSoup

## Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Pabitra3/Video-Downloader.git
   cd Video-Downloader
   ```

2. **Set Up a Virtual Environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Required Packages**
   ```bash
   pip install flask requests beautifulsoup4 lxml
   ```

## Usage
1. **Run the Flask Application**
   Start the Flask server by running:
   ```bash
   python app.py
   ```
   The server will start at `http://127.0.0.1:5000/`.

2. **Access the Web Application**
   Open your web browser and go to `http://127.0.0.1:5000/`. You will see a form where you can input the URL of the video you want to download.

3. **Download the Video**
   - Paste the URL of the video into the input field and click "Download."
   - Once the video is processed, a link will be provided for you to download the video file.

## Code Structure
- `app.py`: The Flask backend that handles form submissions, scraping the video URL, and downloading the video.
- `templates/index.html`: The HTML form where users input the video URL.
- `templates/download.html`: Displays the download link after processing.
- `downloads/`: The folder where downloaded videos are stored.

## Project Flow
1. The user submits a video URL in the frontend form.
2. The Flask backend scrapes the webpage using BeautifulSoup and extracts the video link using a regular expression.
3. The video is downloaded from the extracted URL and stored in the server's `downloads/` folder.
4. A link to the downloaded video is displayed for the user to download the file.

## Example
1. **Input**: A video URL, such as `https://www.ted.com/talks/speaker_name_talk_title`.
2. **Output**:
   - A video file is downloaded and stored on the server.
   - A link to the video file is provided for the user to download.

## Troubleshooting
- **Invalid URL**: Ensure the URL contains a valid video and is supported by the scraping logic.
- **Error Handling**: If there's an error during the download, check the terminal for error logs.
- **File Permission Issues**: Make sure the server has write permissions to the `downloads/` folder.

## Security Considerations
- Limit the types of URLs accepted to prevent downloading videos from unauthorized or harmful sources.
- Add proper validation and sanitization for URL inputs to avoid potential attacks (e.g., injection attacks).

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure to follow the coding standards and include tests where necessary.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or issues, feel free to reach out at developersivaay@gmail.com.