import requests
from youtube_transcript_api import YouTubeTranscriptApi
import datetime

TED_channel_ID = 'UCAuUUnT6oDeKwE6v1NGQxug'
url = 'https://www.googleapis.com/youtube/v3/search?'
query_params = {'part': 'snippet',
                'channelId': TED_channel_ID,
                'maxResults': '2',
                'order': 'date',
                'type': 'video',
                # 'pageToken': '2',
                'key': 'AIzaSyBcCoyA05NW3Su4hLw6_2sKzEaItsSA0ro'}

for key, value in query_params.items():
    url += f'{key}={value}&'

print(url)
response = requests.get(url).json()
data = response['items']
print(response)
print(data[0])
print(data[0].keys())
for video in data:
    print('-' * 100)
    url = 'https://www.youtube.com/watch?v=' + video['id']['videoId']
    title = video['snippet']['title']
    publishedAt = datetime.datetime.strptime(video['snippet']['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
    # categoryIdx =
    print(url, title, publishedAt, type(publishedAt))
    # print(f"categoryId : {video['snippet']['categoryId']}")
    # print(f"title : {video['snippet']['title']}")
#     print(f"videoId : {video['id']}")
#     scripts = []
#     try:
#         for row in YouTubeTranscriptApi.get_transcript(video['id'], languages=['ko']):
#             if len(row['text'].strip().split()) >= 5:
#                 scripts.append(row)
#     except:
#         print('No Korea Scripts')
#         continue
#     print(f"scripts : {scripts}")
