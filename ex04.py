def check(id, password):

	if(id == 'ishimoto'):

		if(password == 'ryoga314'):
			print('OKです')

		else:
			print('IDかパスワードが違います')

	else:
		print('IDかパスワードが違います')

id = input('IDを入力してください：')

password = input('パスワードを入力してください：')

check(id, password)