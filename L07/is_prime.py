# 撰寫一程式，程式檔名為 is_prime.py
# 提示使用者輸入一數字（100 以內的正整數），判斷此數字是否為質數，
# 若為質數，顯示 '是質數' ，反之顯示 '不是質數' 。
a=int(input("請輸入一數字(100以內的正整數):"))
b=2
while a>=b :
   print(b)
   #if  b==a:
     print("是質數")
     break
   elif a%b==0:
     print("不是質數")
     break
     b+=1
