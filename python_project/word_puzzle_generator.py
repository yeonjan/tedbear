import re
import random
import pymysql

conn = pymysql.connect(host='3.36.50.141', user='root', password='824b2937-79c0-4595-8ea2-e8930ed750ae',
                       database='tedbearDB',
                       autocommit=True)
cursor = conn.cursor()
sql = 'SELECT * FROM tedbearDB.word_tb where length(content) between 4 and 7 and score != 0 order by rand() limit 100'
cursor.execute(sql)
word_list = [*cursor.fetchall()]

pattern = r'^[a-z]+$'
use_word_list = []
for word in word_list:
    content = word[1]
    mean = word[2]
    if re.match(pattern, content):
        use_word_list.append((content, mean))
    else:
        print(word)

use_word_list = use_word_list[:10]

board = [['.'] * 100 for _ in range(100)]

sero_candidate = {}
next_char = None
y_pos = 50
x_pos = 45
for _ in range(1):
    choice_word, choice_word_mean = use_word_list.pop(random.randint(0, len(use_word_list) - 1))
    for j in range(len(choice_word)):
        board[y_pos][x_pos + j] = choice_word[j]

    j = 0
    while j < len(choice_word):
        next_word, next_mean = use_word_list.pop()
        if choice_word[j] in next_word:
            temp = next_word.find(choice_word[j])
            for a in range(len(next_word)):
                board[y_pos + a - temp][x_pos + j] = next_word[a]
            j += 2
        else:
            j += 1
print(*map(''.join, board), sep='\n')

for use_word, mean in use_word_list:
    print(use_word + ', ')
