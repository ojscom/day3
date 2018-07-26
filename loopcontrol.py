# num=1
# while True:
#     print(num)
#     num+=1
#     if num>100:
#         break

# message=""
# print("quit을 입력하면 종료됩니다.")
# while message!='quit':
#     message=input("typing your message : ")
#     print(">"+message)

# message=""
# print("quit을 입력하면 종료됩니다.")
# while True:
#     message=input("typing your message : ")
#     print(">"+message)
#     if message=='quit':
#         break


number=0
while number<10:
    number+=1
    if(number%2==0):
        continue
    print(number,end=' ')