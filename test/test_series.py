import pandas as pd


price = [92600, 92400, 92100, 94300, 92300]
s = pd.Series(price)
print(s)
print(s[0], s[1])

# index를 부여할 때는 반드시 데이터 개수와 같아야 한다.

s = pd.Series(
    [92600, 92400, 92100, 94300, 92300],
    index=['2017-01-01', '2017-02-02', '2017-03-03', '2017-04-04', '2017-05-05'])
print(s)
print(s[1], s['2017-02-02'])

# 스칼라 값으로 초기화 할 때는 인덱스가 반드시 필요
s = pd.Series(7, index =['a','b','c','d'])
print(s)

# 딕션너리로 초기화하기
d = {'a':10, 'b': 20, 'c':30} # key = index
s1 = pd.Series(d)
print(s1)

# 왜 type 이 float인지
s1 = pd.Series(d, index = ['a','b','c','d','e'])
print(s1)

#순회 (index, values라는 속성을 통해 접근이 가능하다.)

for date in s.index:
    print('date:',date, end = '\n')
else:
    print()

for price in s.values:
    print('price:',price, end = '\n')
else:
    print()

# 연산
s1 = pd.Series([10,20,30], index = ['A','B','C'])
s2 = pd.Series([10,20,30], index = ['B','C','D'])


s3 = s1+s2
print(s3 , type(s3)) # 같은 인덱스 것만 값을 보여주고 나머지는 NaN

s3 = s1 / s2
print(s3, type(s3)) # s1에서의 B=20,C=30 , s2에서의 B=10,C=20만 계산된다.

s3 = s1 * 3
print(s3, type(s3))
