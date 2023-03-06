import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='teddybear_test', charset='utf8')
cursor = conn.cursor()
sql = 'select * from video'
cursor.execute(sql)
# sql = "INSERT INTO teddybear_test.video (url, title, difficult, publishedAt, categoryIdx) VALUES ('asdf', 'asdf', 'asdf', '2023-03-03 16:39:08', '3')"

res = cursor.fetchall()
print(res)