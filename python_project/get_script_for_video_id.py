from youtube_transcript_api import YouTubeTranscriptApi

for row in YouTubeTranscriptApi.get_transcript('WUvTyaaNkzM', languages=['ko']):
    if len(row['text'].strip().split()) >= 1:
        print(row)
