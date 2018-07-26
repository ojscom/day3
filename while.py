fruits=['apple','banana','kiwi','watermelon']
# for fruit in fruits :
#     print(fruit+'가 있습니다.')

active=True
index=0
while active:
    print(fruits[index]+'를 꺼냈습니다. ')
    #print(fruits[index]+'를 꺼냈습니다. ',end='')
    index=index+1 
    if index>=len(fruits):
        active=False   