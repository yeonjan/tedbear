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
    time = None
    for row in YouTubeTranscriptApi.get_transcript(video_id, languages=['en']):
        merged_text += row['text'].replace('\n', ' ') + ' '
        raw_script = row['text']
        stripped_text = raw_script.strip()
        remain = remain + ' ' + stripped_text
        if time is None:
            time = row['start']
        if stripped_text[-1] in '.!?':
            scripts.append([remain.strip().replace('\n', ' '), time])
            remain = ''
            time = None

    # print(*merged_text.split('.'),sep='.\n')
    # with open('./sample.txt','w',encoding='utf-8') as file:
    #     for script in scripts:
    #         file.write(f'{script[0]} : {script[1]}\n')
    #     # print(*scripts, sep='\n')
    print(f'문장의 수 : {len(scripts)}')
    return scripts


def crawilng(pageToken, key, old_data, channel_id, order, publishedBefore):
    url = 'https://www.googleapis.com/youtube/v3/search?'
    query_params = {'part': 'snippet',
                    'channelId': channel_id,
                    'maxResults': '50',
                    'order': order,
                    # 'regionCode': 'US',
                    'videoDuration': 'medium',
                    'type': 'video',
                    'key': key,
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
    for idx in range(4):
        current_file = open(file_name)
        current_data = json.load(current_file)

        key = key_list[idx]
        channel_id = TED_CHANNEL_ID
        order = order_list[idx]
        token = None

        start_len = len(current_data.keys())
        current_file.close()
        print('=' * 100)
        print(f'{idx}번째 START CRAWLING!!!!')
        print(f'key: {key} , order: {order}')
        while True:
            try:
                next_token, data = crawilng(token, key, current_data, channel_id, order,'2014-01-01T00:00:00Z')
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
        if 'scripts' in current_data[key].keys():
            print(len(current_data[key]['scripts']))
            continue
        try:
            scripts = get_script_by_video_id(key)
        except:
            scripts = []
            # traceback.print_exc()
        cnt += 1
        current_data[key]['scripts'] = scripts
        if cnt % 50 == 0:
            with open(file_name, 'w') as outfile:
                json.dump(current_data, outfile, indent=4)
            cnt = 0
            print('저장완료!!!!' + '==' * 100)
    with open(file_name, 'w') as outfile:
        json.dump(current_data, outfile, indent=4)


if __name__ == '__main__':
    TED_CHANNEL_ID = 'UCAuUUnT6oDeKwE6v1NGQxug'
    TEDX_CHANNEL_ID = 'UCsT0YIqwnpJCM-mx7-gSA4Q'
    file_name = 'data/video_data.json'

    append_data_to_json()
    append_script_to_json()
    # current_file = open(file_name)
    # current_data = json.load(current_file)
    # for key in current_data.keys():
    #     del current_data[key]['scripts']
    # with open(file_name, 'w') as outfile:
    #     json.dump(current_data, outfile, indent=4)
