driving = input('請問你有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = int(input('請問你的年齡? '))
if driving == '有':
	if age >= 18:
		print('great')
	else:
		print('you are such a bad guy')

elif driving== '沒有':
	if age >= 18:
		print('coward')
	else:
		print('good')