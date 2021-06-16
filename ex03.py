address = input('メールアドレスを入力してください：')

f = address.find('@')

domain = address[f+1:]

print(f'メールアドレス( {address} )のドメイン：{domain}')