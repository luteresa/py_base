"""
1.请将下面的数值转成另外三种进制，并用print输出
(1) 12345
(2) 0xf98a
(3)0b110010110

"""
x=12354
y=0xf98a
z=0b110010110

print(bin(x))
print(oct(x))
print(hex(x))

print(bin(y))
print(oct(y))
print(int(str(y),16))

print(int('0b110010110',2))
print(oct(z))
print(hex(z))


print(str(z))

x=5423.5346
print(format(x,'0.3f'))
print(format(x,'0>10.2f'))
print(format(x,'0<10.2f'))
print(format(x,'<10.2f'))
print(format(x,'0>10,.2f'))
print(format(x,'a^10,.2f'))
