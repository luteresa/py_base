#Pthon语言中，每一种类型的值都可以被解释成布尔类型的值
b=True

#解释为假：None 0 "" () [] {}
print("None=",bool(None))
print("0=",bool(0))
print('""=',bool(""))
print("()=",bool(()))
print("[]=",bool([]))
print("{}=",bool({}))
print("10=",bool(10))
print("=============")
#布尔类型可以跟整数运算，不能与其他类型运算
print(1==False)
print(''==False)
print(bool("")==False)

#False:0 True:1
print(0==False)

print(10+True+False)