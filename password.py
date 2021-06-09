password = 'a123456'
remain_chance = 3 #剩餘機會
while remain_chance > 0:
	remain_chance = remain_chance - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break #逃出迴圈
	else:
		print('密碼錯誤!')
		if remain_chance > 0:
			print('還有', remain_chance, '次機會')
		else:
			print('沒機會了，程式結束')		