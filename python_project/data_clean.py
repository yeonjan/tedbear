import json
import string

current_file = open('data/video_data2.json')
current_data = json.load(current_file)
cnt = 0
for key,value in current_data.items():
    title = value['title']
    if title[0] not in string.ascii_lowercase+string.ascii_uppercase:
        continue
    print(title,value['video_url'])
    cnt += 1
print(cnt)
current_file.close()