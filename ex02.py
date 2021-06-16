import re

address = input('メールアドレスを入力してください：')

m = re.fullmatch(r'[a-z]+@[a-z]+\.com', address)

if(m == None):
	print('何かおかしいです')
else:
	print('正しいメールアドレスです')