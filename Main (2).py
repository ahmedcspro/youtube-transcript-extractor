from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url_or_id):
    if re.fullmatch(r"[0-9A-Za-z_-]{11}", url_or_id):
        return url_or_id

    pattern = r"(?:v=|youtu\.be/|embed/|shorts/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, url_or_id)

    return match.group(1) if match else None


def get_transcript_text(url_or_id):
    video_id = extract_video_id(url_or_id)

    if not video_id:
        return "Invalid YouTube URL"

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)

        return " ".join(item.text for item in transcript)

    except Exception as e:
        return f"Error: {e}"


youtube_url = "https://youtu.be/oUEz0ItQEkU"

script = get_transcript_text(youtube_url)

print(script)