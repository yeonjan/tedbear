import traceback

import requests
from youtube_transcript_api import YouTubeTranscriptApi
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


def get_video_info_by_video_id(video_id, key):
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


def get_script_by_video_id(video_id):
    merged_text = ''
    scripts = []
    remain = ''
    start_time = None
    for row in YouTubeTranscriptApi.get_transcript(video_id, languages=['en']):
        merged_text += row['text'].replace('\n', ' ') + ' '
        raw_script = row['text']
        stripped_text = raw_script.strip()
        remain = remain + ' ' + stripped_text
        if start_time is None:
            start_time = row['start']
        if stripped_text[-1] in '.!?':
            script = {}
            script['content'] = remain.replace('\n', ' ').strip()
            script['start_time'] = round(start_time, 1)
            script['end_time'] = round(row['start'] + row['duration'], 1)
            scripts.append(script)
            remain = ''
            start_time = None

    # print(f'문장의 수 : {len(scripts)}')
    return scripts


def crawilng(pageToken, key, old_data, channel_id, order, publishedAfter, publishedBefore):
    url = 'https://www.googleapis.com/youtube/v3/search?'
    query_params = {'part': 'snippet',
                    'channelId': channel_id,
                    'maxResults': '50',
                    'order': order,
                    # 'regionCode': 'US',
                    'videoDuration': 'medium',
                    'type': 'video',
                    'key': key,
                    'publishedAfter': publishedAfter,
                    'publishedBefore': publishedBefore
                    }
    if pageToken is not None:
        query_params['pageToken'] = pageToken
    for k, value in query_params.items():
        url += f'{k}={value}&'
    print(url)
    new_data = {}
    response = requests.get(url).json()
    data = response['items']
    for video in data:
        video_id = video['id']['videoId']
        if video_id in old_data:
            print(f'{video_id} is already Exist!')
            continue
        video_url = 'https://www.youtube.com/watch?v=' + video_id
        title = video['snippet']['title']
        published_at = video['snippet']['publishedAt']
        video_info = get_video_info_by_video_id(video_id, key)

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

    return response.get('nextPageToken'), new_data


def append_data_to_json():
    key_list = ['AIzaSyBcCoyA05NW3Su4hLw6_2sKzEaItsSA0ro', 'AIzaSyBhLQfMyqvKTifR9T6YyXxZwP71faWk_2Y',
                'AIzaSyC7biMC09pRWWidK0ma1azQ2tqT3dKAug0', 'AIzaSyBDN5GEJusPfhfdXIiMt7zC7jjUpPP7sxw']
    # channel_id_list = [TEDX_CHANNEL_ID, TED_CHANNEL_ID]
    order_list = ['date', 'rating', 'title', 'viewCount']
    file_name = 'data/video_data.json'
    for dyear in range(1, 14, 4):
        for idx in range(4):
            current_file = open(file_name)
            current_data = json.load(current_file)

            key = key_list[idx]
            channel_id = TED_CHANNEL_ID
            order = 'date'
            token = None
            year = 2008 + idx + dyear
            published_after = f'{year}-01-01T00:00:00Z'
            published_before = f'{year + 1}-01-01T00:00:00Z'

            start_len = len(current_data.keys())
            current_file.close()
            print('=' * 100)
            print(f'{idx}번째 START CRAWLING!!!!')
            print(f'key: {key} , order: {order}')
            while True:
                try:
                    next_token, data = crawilng(token, key, current_data, channel_id, order, published_after,
                                                published_before)
                    current_data.update(data)
                    token = next_token
                    print('one cycle end!!', token)
                except Exception as e:
                    traceback.print_exc()
                    break
                if token is None:
                    break
            print('전체크롤링 결과 : ', start_len, '->', len(current_data.keys()))
            with open(file_name, 'w') as outfile:
                json.dump(current_data, outfile, indent=4)


import random


def append_script_to_json():
    current_file = open(file_name)
    current_data = json.load(current_file)
    cnt = 1
    for key in current_data.keys():
        cnt += 1
        if 'scripts' not in current_data[key].keys():
            try:
                scripts = get_script_by_video_id(key)
            except:
                scripts = []
            current_data[key]['scripts'] = scripts
            print(f'{cnt}번째 자막 추출 완료!')
            if cnt % 100 == 0:
                with open(file_name, 'w') as outfile:
                    json.dump(current_data, outfile)
                print('저장완료!!!!' + '==' * 100)
    with open(file_name, 'w') as outfile:
        json.dump(current_data, outfile)


def delete_script():
    current_file = open(file_name)
    current_data = json.load(current_file)
    for key in current_data.keys():
        del current_data[key]['scripts']
    with open(file_name, 'w') as outfile:
        json.dump(current_data, outfile, indent=4)


if __name__ == '__main__':
    TED_CHANNEL_ID = 'UCAuUUnT6oDeKwE6v1NGQxug'
    TEDX_CHANNEL_ID = 'UCsT0YIqwnpJCM-mx7-gSA4Q'
    file_name = 'data/video_data.json'

    # append_data_to_json()
    append_script_to_json()

    # current_file = open(file_name)
    # current_data = json.load(current_file)
    # print(len(current_data.keys()))
