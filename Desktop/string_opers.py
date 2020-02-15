#1
msg = 'welcome to python'
print(" positive index no. in msg is letter",msg[1])
print(" negative index no. in msg is letter",msg[-1])

#2

msg1 = 'helloworld '
print("+ve slicing is:",msg1[2:6])
print("-ve slicing is:",msg1[-10:-6])
print("slicing without position is:",msg1[::])
print("slicing without position is:", msg1[:7:3])
print("slicing without position is:", msg1[-2::])
print("slicing without position is:", msg1[:-8:] )
print("slicing without position is:", msg1[::-2] )

#3
msg2 = msg1 + msg
print("the combo of them is:",msg2)

#4
msg3 = msg *2
print("the mul will be as:",msg3)

#5
print("membership check:",'python'in msg)

#6
print("my name is %s and age is %d"%('sumanth',23))

#7
import sys
str1 = 'sumanth'
str2 = u'vemuri'
#print(str1,str2,len(str1),len(str2))
print("the lemgth is:",len(str1))

print(sys.getsizeof(str1))
print(sys.getsizeof(str2))


