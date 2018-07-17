import  os

print("hello world")
print("a","b","c","d","e")


print("name=","bill")

print("ruby,","Python,","C++,","Perl")

print("Ruby,"+"Python,"+"C++,"+"Perl")

#通过sep命名参数，可以指定多参数值的分隔符
print("ruby","Python","C++","Perl",sep=",")

#通过命名参数end可以改变输出字符串结尾的字符
print("hello",end=" ")
print("world")