import pandas as pd

#1
# 2개의 series를 만들자
#  Series 와 dict 데이터를 사용한 DataFrame
d = {
'one': pd.Series([1, 2, 3], index = ['a','b','c']),
'two': pd.Series([10, 20, 30, 40], index = ['a','b','c','d'])
}


# 2개의 series를 Dataframe으로 합치자

df = pd.DataFrame(d)
print(df)

# list 와 dict를 사용
data =[
{'name': '둘리','age': 10, 'phone': '010-1111-1111'},
{'name': '마이코올~','age':30, 'phone': '010-1111-2222'},
{'name': '도우너', 'age':20,'phone': '010-3333-3333'}
    ]
# 인덱스는 따로 잡아주지 않아서 자동으로 정해진다.
df = pd.DataFrame(data)
print(df)

# 이전의 데이터 프레임에서 컬럼요소를 빼와서 새로운 데이터프레임을 만든다.
df2 = pd.DataFrame(df, columns =['name', 'phone']) # df데이터프레임에서 name,phone의 컬럼만을 추출
print(df2)

# 데이터 추가 (열 추가)
df2['height'] = [150,160,170] # 이전 dataframe에 새로운 컬럼을 추가해준다.
print(df2)

# 인덱스 선택
df3 = df2.set_index('name') # df2의 인덱스를 이름으로 한 데이터프레임을 df3으로 한다.
print("df3:",df3)

# 컬럼 선택
s = df2['name']
print(s,type(s))

#merge
df4 = pd.DataFrame([{'sido': '서울'}, {'sido': '부산'}, {'sido': '전주'}])

df5 = pd.merge(df2,df4, left_index = True, right_index= True) # 겹치는게 인덱스밖에 없어서 인덱스로 병합
print(df5)

df1 = pd.DataFrame({
    '고객번호': [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름': ['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']})

df2 = pd.DataFrame({
    '고객번호': [1001, 1001, 1005, 1006, 1008, 1001],
    '금액': [10000, 20000, 15000, 5000, 100000, 30000]})

# 공통 열인 고객번호를 기준으로 데이터를 찾아서 합친다.
# 이 때 기본적으로 양쪽 데이터프레임에 모두 키가 존재하는
# 데이터만 합쳐진다.(inner join 방식 교집합방식)
df3 = pd.merge(df1, df2)
print(df3)

#outer join 방식은 key값이 한쪽에만 있어도 양쪽 데이터를 모두 합쳐진다.(full)
df3 = pd.merge(df1, df2, how = 'outer')
print(df3) # 매칭이 안되는 값은 NAN값이 나온다.

# left, 첫 번째 파라미터의 데이터 프레임의 데이터를 전부 합치는 방식
df3 = pd.merge(df1, df2, how = 'left')
print(df3) # 매칭이 안되는 값은 NAN값이 나온다.

#right, 두 번째 파라미터의 데이터 프레임의 데이터를 전부 합치는 방식
df3 = pd.merge(df1, df2, how = 'right')
print(df3) # 매칭이 안되는 값은 NAN값이 나온다.



# 기준 열은 on인수로 명시적 설정이 가능하다.
df1 = pd.DataFrame({'성별': ['남자', '남자', '여자'],
                    '연령': ['미성년자', '성인', '미성년자'],
                    '매출1': [1, 2, 3]})

df2 = pd.DataFrame({'성별': ['남자', '남자', '여자', '여자'],
                    '연령': ['미성년자', '미성년자', '미성년자', '성인'],
                    '매출2': [4, 5, 6, 7]})

df3 = pd.merge(df1, df2)
print(df3)

#on으로 기준컬럼을 지정해줄 수 있다.

df3 = pd.merge(df1, df2, on= ['성별','연령'])
print(df3)

df3 = pd.merge(df1, df2, on= ['성별'])
print(df3)

