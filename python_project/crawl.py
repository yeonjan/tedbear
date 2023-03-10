import traceback

import requests
from youtube_transcript_api import YouTubeTranscriptApi
import datetime
import json


def get_all_category():
    url = 'https://www.googleapis.com/youtube/v3/videoCategories?'
    query_params = {'part': 'snippet',
                    'regionCode': 'KR',
                    'key': 'AIzaSyBcCoyA05NW3Su4hLw6_2sKzEaItsSA0ro'}

    for key, value in query_params.items():
        url += f'{key}={value}&'
    category_data = {}
    # print(requests.get(url).json()['items'])
    for row in requests.get(url).json()['items']:
        id = row['id']
        category = row['snippet']['title']
        category_data[id] = category
    return category_data


def get_video_info(video_id, key):
    url = 'https://www.googleapis.com/youtube/v3/videos?'
    query_params = {'part': 'snippet',
                    'id': video_id,
                    'key': key}
    for k, v in query_params.items():
        url += f'{k}={v}&'

    return requests.get(url).json()


def get_category_id_by_video_info(video_info):
    return video_info['items'][0]['snippet']['categoryId']


def get_thumbnail_url_by_video_info(video_info):
    if 'maxres' in video_info['items'][0]['snippet']['thumbnails'].keys():
        return video_info['items'][0]['snippet']['thumbnails']['maxres']['url']
    return video_info['items'][0]['snippet']['thumbnails']['high']['url']


def save_json(pageToken, key, old_data, channel_id):
    url = 'https://www.googleapis.com/youtube/v3/search?'
    query_params = {'part': 'snippet',
                    'channelId': channel_id,
                    'maxResults': '50',
                    'order': 'date',
                    # 'safeSearch': 'none',
                    'videoDuration': 'long',
                    'type': 'video',
                    'key': key
                    }
    if pageToken is not None:
        query_params['pageToken'] = pageToken
    for k, value in query_params.items():
        url += f'{k}={value}&'
    print(url)
    new_data = {}
    response = requests.get(url).json()
    print(response)
    data = response['items']
    # print(*data,sep='\n')
    for video in data:
        video_id = video['id']['videoId']
        if video_id in old_data:
            print('pass')
            continue
        video_url = 'https://www.youtube.com/watch?v=' + video_id
        title = video['snippet']['title']
        published_at = video['snippet']['publishedAt']
        video_info = get_video_info(video_id, key)

        category_idx = get_category_id_by_video_info(video_info)
        thumbnail_url = get_thumbnail_url_by_video_info(video_info)
        video_data = {}
        video_data['category_no'] = category_idx
        video_data['title'] = title
        video_data['video_url'] = video_url
        video_data['thumbnail_url'] = thumbnail_url
        video_data['published_at'] = published_at
        new_data[video_id] = video_data
        print(video_data)
        print('-' * 100)

    # nextPageToken =  response['nextPageToken'] if 'nextPageToken' in response.keys() else
    return response.get('nextPageToken'), new_data


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

if __name__ == '__main__':
    current_file = open('./video_data.json')
    key_list = ['AIzaSyBcCoyA05NW3Su4hLw6_2sKzEaItsSA0ro', 'AIzaSyBhLQfMyqvKTifR9T6YyXxZwP71faWk_2Y',
                'AIzaSyC7biMC09pRWWidK0ma1azQ2tqT3dKAug0', 'AIzaSyBDN5GEJusPfhfdXIiMt7zC7jjUpPP7sxw'
                ]
    TED_CHANNEL_ID = 'UCAuUUnT6oDeKwE6v1NGQxug'
    TEDX_CHANNEL_ID = 'UCsT0YIqwnpJCM-mx7-gSA4Q'
    channel_id_list = [TEDX_CHANNEL_ID, TED_CHANNEL_ID]
    key = key_list[0]
    channel_id = channel_id_list[0]
    try:
        current_data = json.load(current_file)
    except:
        print('error!')
        current_data = {}
    start_len = len(current_data.keys())
    current_file.close()
    file_path = './video_data.json'
    with open('./last_token', 'r') as inputfile:
        try:
            token = inputfile.readline().strip()
        except:
            token = None
    while True:
        try:
            next_token, data = save_json(token, key, current_data, channel_id)
            current_data.update(data)
            token = next_token
            print(token)
        except Exception as e:
            traceback.print_exc()
            break
        if token is None:
            break
    print('endToken', token)
    print('전체크롤링 결과 : ', start_len, '->', len(current_data.keys()))
    with open(file_path, 'w') as outfile:
        json.dump(current_data, outfile, indent=4)
    if token is not None:
        with open('./last_token', 'w') as outfile:
                outfile.write(token)
