import re

def match(a):
	return re.fullmatch(r'[a-z]+@[a-z]+\.com', a)

address = input('メールアドレスを入力してください：')

if(match(address) == None):
	print('何かおかしいです')
else:
	print('正しいメールアドレスです')