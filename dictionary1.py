#dictionary는 key와 value를 갖는다. 하나 생성해보자


profile= {
    'name' : 'chan',
    'age' : '33',
    'hobby': 'game'
}

print(profile)
print('딕셔너리는 키로 접근함', profile['name'])


profile['age'] = '3'
print(profile)

print(profile.get('aaaa')) #get은 키를 가져오는것
print(profile.get('name'))

print('삭제전',profile)

del profile['age']

print('삭제후',profile)
