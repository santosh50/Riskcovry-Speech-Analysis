# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:49:37 2021

@author: Akhil
"""

def get_year(text):
    count=0
    ans=""
    nums=["0","1","2","3","4","5","6","7","8","9"]
    for i in text:
        if i in nums:
            ans+=i
            count+=1
            if count==4:
                return int(ans)
        else:
            count=0
            ans=""
            
            
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
        if ans!="":
            return int(ans)
        return 0
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
        return 0
            
def get_dob_response(audio_text):
    y=get_year(audio_text)
    text=audio_text.split(" ")
    m=0
    d=0
    if get_number(text[0])==y:
        for i in text[1:]:
            if get_number(i)!=0 and m==0:
                m=get_number(i)
            elif get_number(i)!=0 and m!=0:
                d=get_number(i)
        return [str(d)+"/"+str(m)+"/"+str(y)]
    else:
        mons={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
        d=0
        m=0
        for i in text:
            if d==0 and get_number(i)!=0:
                d=get_number(i)
            elif d!=0 and i.lower() in mons:
                m=mons[i]
                return [str(d)+"/"+str(m)+"/"+str(y)]
            elif d!=0 and get_number(i)!=0:
                m=get_number(i)
                return [str(d)+"/"+str(m)+"/"+str(y)]
def main():
    t1="1998 10 22"
    t2="23rd december 1998"
    t3="22 10 1998"
    print(get_dob_response(t3))
if __name__=="__main__":
    main()
