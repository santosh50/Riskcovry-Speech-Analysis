# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 19:13:59 2021

@author: Akhil
"""

def get_number(text):
    dec=0
    if "point" in text.split(" "):
        dec=1
    text=[i for i in text if i!=" "]
    nums=["0","1","2","3","4","5","6","7","8","9"]
    ans=""
    first=0
    if dec==0:
        for i in text:
            if i in nums:
                ans+=i
                first=1
            elif i not in nums and first==1:
                return int(ans)
    else:
        num1=""
        f1=1
        f2=0
        num2=""
        dot=0
        for i in text:
            if i in nums and f1==1:
                num1+=i
            elif i in nums and f2==0 and f1==0:
                num2+=i
            elif i not in nums and f1==1:
                f1=0
                f2=0
            elif i not in nums and len(num2)!=0:
                return float(num1+"."+num2)

def suitable(num,option):
    if "<" in option:
        if num<get_number(option):
            return True
    if ">" in option:
        if num>get_number(option):
            return True
    return False

def get_income_response(audio_text,options):
    num=get_number(audio_text)
    ans=[]
    for i in options:
        if "-" in i:
            x=i.split("-")
            n1=get_number(x[0])
            n2=get_number(x[1])
            if num>=n1 and num<=n2:
                ans.append(i)
                return ans
        if suitable(num,i):
            ans.append(i)
            return ans
def main():
    t1="4lakh"                
    o1=["<2lakh","2lakh-5lakh","5lakh-10lakh","10lakh>"]
    t2="3lakh"
    o2=["<5lakh","5lakh-15lakh","15lakh-20lakh","20lakh>"]
    print(get_income_response(t2,o2))  
    
if __name__=='__main__':
    main()
          