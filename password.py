password = 'a123456'

while True:
	user_password = input('請輸入密碼:')
	if password == user_password:
		print('登入成功！')
		break
	elif password != user_password:
		print('密碼錯誤! 還有2次機會') 
		user_password = input('請輸入密碼:')
		if password != user_password:
			print('密碼錯誤! 還有1次機會') 
		elif password == user_password:
			print('登入成功！') 
			break
		user_password = input('請輸入密碼:')
		if password != user_password:
			print('密碼錯誤! 程式結束')
			break
		elif password == user_password:
			print('登入成功！') 
			break