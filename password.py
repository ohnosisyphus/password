password = 'a123456'
remain_chance = 3 #剩餘機會
while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		remain_chance = remain_chance - 1
		print('密碼錯誤! 還有', remain_chance, '次機會')
		if remain_chance == 0:
			print('密碼錯誤! 程序結束')
			break