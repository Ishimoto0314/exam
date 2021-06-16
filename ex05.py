def remove(list):
	list.remove('')
	print(list)
	
def average(list):
	remove(list)
	ave = sum(list) / len(list)
	print(f'平均値：{ave}')

list = [13, 17, 31, 57, '', 41, 83]

average(list)
