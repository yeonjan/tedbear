import json

arr = [[{} for _ in range(4)] for _ in range(4)]
arr[0][0] = {'clueIdx': 1, 'box': True}
arr[0][1] = {'clueIdx': 2, 'box': True}
arr[0][2] = {'clueIdx': 0, 'box': True}
arr[0][3] = {'clueIdx': 0, 'box': False}
arr[1][0] = {'clueIdx': 0, 'box': False}
arr[1][1] = {'clueIdx': 0, 'box': True}
arr[1][2] = {'clueIdx': 0, 'box': False}
arr[1][3] = {'clueIdx': 0, 'box': False}
arr[2][0] = {'clueIdx': 3, 'box': True}
arr[2][1] = {'clueIdx': 0, 'box': True}
arr[2][2] = {'clueIdx': 0, 'box': True}
arr[2][3] = {'clueIdx': 4, 'box': True}
arr[3][0] = {'clueIdx': 0, 'box': False}
arr[3][1] = {'clueIdx': 0, 'box': True}
arr[3][2] = {'clueIdx': 0, 'box': False}
arr[3][3] = {'clueIdx': 0, 'box': True}

arr = [ele for row in arr for ele in row]
print(arr)

clueList = [None for _ in range(4)]
answerList = ['dog', 'open', 'seem', 'my']
indexList = [0, 1, 8, 11]
meanList = ['개', '열다', '보이다', '나의']
directionList = ['across', 'down', 'across', 'down']

for i in range(4):
    clueList[i] = {'clueIdx': i + 1,
                   'answer': answerList[i],
                   'index': indexList[i],
                   'mean': meanList[i],
                   'shorts': {'videoIdx': 456},
                   'direction': directionList[i],
                   'length': len(answerList[i])
                   }

data = {'board': arr,'boardSize':4, 'clueList': clueList}

print(json.dumps(data, indent=4))
