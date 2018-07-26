# def hello():
#     name=input("성함을 입력하세요 : ")
#     print("안녕하세요 "+name.title()+"님")

# hello() 

# def hello(name):
#     print("안녕하세요 "+name.title()+"님")

# typing=input("성함을 입력하세요 : ")
# hello(typing) 
# print(typing)

# def cal(num1, num2):
#     print("%d+%d=%d"%(num1,num2,num1+num2))
#     print("%d-%d=%d"%(num1,num2,num1-num2))
#     print("%d*%d=%d"%(num1,num2,num1*num2))
#     print("%d/%d=%d"%(num1,num2,num1/num2))
#     print("%d%%%d=%d"%(num1,num2,num1%num2))
#     print("%d//%d=%d"%(num1,num2,num1//num2))

# cal(10,5)  
# 
def cal(num1, num2):
    print("%d+%d=%d"%(num1,num2,num1+num2))
    print("%d-%d=%d"%(num1,num2,num1-num2))
    print("%d*%d=%d"%(num1,num2,num1*num2))
    print("%d/%d=%d"%(num1,num2,num1/num2))
    print("%d%%%d=%d"%(num1,num2,num1%num2))
    print("%d//%d=%d"%(num1,num2,num1//num2))

num1=int(input("첫번째 수를 입력하세요 : "))
num2=int(input("두번째 수를 입력하세요 : "))
cal(num1,num2)  
   