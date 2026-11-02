# YouTube Transcript Extractor

A lightweight Python tool that extracts available transcripts from YouTube videos and converts the transcript segments into clean, readable text.

## 📌 Project Overview

**YouTube Transcript Extractor** is a Python utility designed to automate the process of retrieving YouTube video transcripts.

The tool accepts either a YouTube video URL or an 11-character video ID, identifies the video, retrieves its available transcript, and combines the transcript segments into a single text output.

This project was built as a practical exercise in Python, API/library integration, input validation, regular expressions, and error handling.

## ✨ Features

* **YouTube URL Parsing** — Extracts video IDs from supported YouTube URL formats.
* **Video ID Validation** — Validates direct 11-character YouTube video IDs.
* **Transcript Retrieval** — Retrieves available transcripts using `youtube-transcript-api`.
* **Clean Text Output** — Combines individual transcript segments into a single readable text string.
* **Error Handling** — Handles invalid URLs and transcript retrieval errors without terminating unexpectedly.

## 🛠️ Tech Stack

* **Python 3**
* **youtube-transcript-api** — Transcript retrieval
* **Regular Expressions (`re`)** — YouTube URL and video ID parsing

## ⚙️ How It Works

```text
YouTube URL / Video ID
        ↓
Extract Video ID
        ↓
Validate Input
        ↓
Fetch Transcript
        ↓
Combine Transcript Segments
        ↓
Return Text
```

The program first identifies the YouTube video ID from the provided input. It then uses `youtube-transcript-api` to retrieve the transcript and combines the returned transcript segments into a single string.

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or newer
* An internet connection
* A YouTube video with an available transcript

### Installation

Clone the repository:

```bash
git clone https://github.com/ahmedcspro/youtube-transcript-extractor.git
cd youtube-transcript-extractor
```

Install the required dependency:

```bash
pip install youtube-transcript-api
```

### Usage

Run the program:

```bash
python main.py
```

The current version uses a YouTube URL defined in the Python script.

Example:

```python
youtube_url = "https://youtu.be/oUEz0ItQEkU"
```

The extracted transcript is then printed to the terminal.

## 📂 Project Structure

```text
youtube-transcript-extractor/
│
├── main.py
└── README.md
```


**Built with Python**
