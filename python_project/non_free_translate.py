import json
import urllib.request
import multiprocessing
import pymysql


def translate(orig_word, client_id, client_secret):
    encText = urllib.parse.quote(orig_word)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        return json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
    else:
        raise ValueError(rescode)


def heavy_work(start, end, id, secret):
    conn = pymysql.connect(host='3.36.50.141', user='root', password='824b2937-79c0-4595-8ea2-e8930ed750ae',
                           database='tedbearDB',
                           autocommit=True)
    cursor = conn.cursor()
    sql = f'SELECT * FROM word_tb where mean is null and no between {start} and {end}'
    # sql = f'SELECT * FROM word_tb where mean is null'
    cursor.execute(sql)
    rows = list(cursor.fetchall())

    for idx, row in enumerate(rows):
        no = row[0]
        content = row[1].replace('#', '')
        sql = 'update word_tb set mean = %s where no = %s'
        print(f'[{no}] : {content} {id}')
        result = translate(content, id, secret)
        cursor.execute(sql, (result, no))
        print(result)
        print('-' * 100)


id_list = ["6eD87zNWX_sVSkUKkFPp", '7DMW4nhZpSagdDH_CzdX', 'nP0yfBZQWNd8qmSsi5uW', 'bYeTE3iYzbataZawmQIU',
           'Q8w1vuz6_cHHgCCRv1aK']
secret_list = ["QRw_5DFxyZ", 'EpJBRpb10p', 'Hqox4PA_i8', 'rT8HzteXrU', 'rT8HzteXrU', 'DDtnQYave0']

for i in range(len(id_list)):
    try:
        heavy_work(1, 100000, id_list[i], secret_list[i])
    except:
        continue


# if __name__ == "__main__":
#     procs = []
#
#     id_list = ["6eD87zNWX_sVSkUKkFPp", '7DMW4nhZpSagdDH_CzdX', 'nP0yfBZQWNd8qmSsi5uW', 'bYeTE3iYzbataZawmQIU',
#                'Q8w1vuz6_cHHgCCRv1aK']
#     secret_list = ["QRw_5DFxyZ", 'EpJBRpb10p', 'Hqox4PA_i8', 'rT8HzteXrU', 'rT8HzteXrU', 'DDtnQYave0']
#
#     for i in range(len(id_list)):
#         client_id = id_list[i]
#         client_secret = secret_list[i]
#         p = multiprocessing.Process(target=heavy_work, args=(1,100000, client_id, client_secret))
#         p.start()
#         procs.append(p)
#
#     for p in procs:
#         p.join()  # 프로세스가 모두 종료될 때까지 대기
