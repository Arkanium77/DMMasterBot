def botString(a):
	a=a.split(' ')
	b=[]

	for i in range(len(a)):
		if(a[i]!=''):
			b.append(a[i])

	b.sort()
	tmp=0
	bl=[]
	num=[]
	bl.append(b[0])

	for i in b:
		if i in bl:
			tmp+=1
		else:
			bl.append(i)
			num.append(tmp)
			tmp=1

	num.append(tmp)
	a=[]
	a.append(bl)
	a.append(num)
	return a
#8-2 10-3 12-6 14-14 16-4 18-1
#8-3 10-9 12-6 14-4 16-3 18-2

		
def nvString(a):
	c=a.split(' ')
	b=[]
	for i in range(len(c)):
		if(c[i]!=''):
			b.append(c[i])
	
	a=[]
	a.append([])
	a.append([])
	for i in range(len(b)):
		tmp=b[i].split('-')
		a[0].append(tmp[0])
		a[1].append(tmp[1])
	
	return a

def moda(a):
	maxi=0

	for i in range(len(a[1])):
		if int(a[1][i])>int(a[1][maxi]):
			maxi=i
	return a[0][maxi]

def meanX(a):
	_sum=0
	_del=0

	for i in range(len(a[1])):
		_sum+=int(a[1][i])*int(a[0][i])
		_del+=int(a[1][i])	
	return _sum/_del
	
def canIDO(a):
	for i in a[0]:
		try:
			b=int(i)//2
		except Exception:
			print("Рассчеты не возможны для не числовых показателей.") 
			return False
	return True
	
def dispX(a):
	a1=[]
	a1.append([int(number)*int(number) for number in a[0]])
	a1.append(a[1])
	a1=meanX(a1)
	return a1-meanX(a)**2
	

endless=True
while endless:
	type_=input("Выберете тип вводимых данных: \n0 - бот-строка\n1 - строка name-value\n")
	if(int(type_)==0):
		a=input("Введите строку значений (разделитель - пробел): \n")
		a=botString(a)
	else:
		a=input("""Введите строку значений name-value\nЭто строка вида  name1-value1 name2-value2 и т.д. 
	где name - имя параметра, value - число раз, которое он встречается.\n
	Вводите строку сразу отсортированной:\n""")
		a=nvString(a)

	print("%s\n%s"%(a[0],a[1]))

	print ("Мода - это %s"%moda(a))


	if canIDO(a):
		print("X среднее равно %s"%meanX(a))
		print("Математическим ожиданием для подобной случайной величины будет X среднее, найденное в прошлой строке.")
		print("Дисперсия случайной величины равна %s"%dispX(a))
	else:
		print("Дальнейшие рассчеты бессмысленны.")
	s=int(input("\nЕщё раз? 0 - да, 1 - нет\n"))
	if s!=0:
		endless=False


