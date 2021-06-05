# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:17:55 2021

@author: Akhil
"""
'''
import spacy
nlp = spacy.load("en_core_sci_lg")
text="""I have thyroid and cancer"""
words=nlp(text)
print(words.ents)
'''

import yake
extractor=yake.KeywordExtractor()
language="en"
n_gram_size=3
num_keywords=4
deduplication_threshold=0.4
custom_extractor=yake.KeywordExtractor(lan=language, n=n_gram_size, dedupLim=deduplication_threshold, top=num_keywords, features=None)


diseases=["high blood pressure","cancer","diabetes","thyroid"]
def get_disease_response(audio_text, options):
    audio_text=audio_text.lower()
    if "no" in audio_text.split(" ") and "None" in options:
        return ["None"]
    ans=[]
    words=custom_extractor.extract_keywords(audio_text)
    flag=0
    print(words)
    for i in words:
        flag=0
        for j in options:
            if j.lower() in i[0].split(' ') and j not in ans:
                ans.append(j)
                flag=1
        if flag==0:
            if "Others" in options:
                if i[0] in diseases:
                    ans.append("Others")
    return ans
t1="I have cancer and thyroid"
o1=["Cancer","Thyroid"]
t2="I have no disease"
o2=["Diabetes","Thyroid","Cancer","Others","None"]
t3="I have Thyroid and High Blood Pressure"
o3=["Diabetes","Thyroid","Cancer","Others","None"]
t4="I have High Blood Pressure"
o4=["Diabetes","Thyroid","Cancer","None"]
#print(get_disease_response(t4,o4))