import random

#로또 번호는 1~46, 총 6개 당첨번호
today_lotto_num=[]

# today_lotto_num.append(random.randrange(1,47,1)) 
# today_lotto_num.append(random.randrange(1,47,1)) 
# today_lotto_num.append(random.randrange(1,47,1)) 
# today_lotto_num.append(random.randrange(1,47,1)) 
# today_lotto_num.append(random.randrange(1,47,1)) 
# today_lotto_num.append(random.randrange(1,47,1)) 

# start=0
# while start<6:
#     today_lotto_num.append(random.randrange(1,47,1))
#     start+=1

# for i in range(0,6):
#     today_lotto_num.append(random.randrange(1,47,1))    

today_lotto_num=random.sample(range(1,47),6)    
 
print("오늘의 추천번호는 "
+str(today_lotto_num[0])+","
+str(today_lotto_num[1])+","
+str(today_lotto_num[2])+","
+str(today_lotto_num[3])+","
+str(today_lotto_num[4])+","
+str(today_lotto_num[5])+" 입니다." )