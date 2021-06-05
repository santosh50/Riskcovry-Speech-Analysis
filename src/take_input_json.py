"""
import gtts
from playsound import playsound
import json
import random
"""
textts = gtts.gTTS ( " Hello Programmers " ) 
textts.save("JTP.mp3") 
playsound("JTP.mp3") 

"""
"""
SpeechToText API

"""

optionS = ["Diabetes","Thyroid","Cancer", "Pressure", "Others"]



#R = '{"Request":{"question_key": "q1","options": optionS,"audio": "I have cancer and thyroid"}}'
  
R = '{"question_key":"q1", "options": ["Diabetes","Thyroid","Cancer", "Pressure", "Others"]}'
#x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(R)
print(y)


#print(R.Request)   
#disease = random.choice(optionS) 
#print(disease)
#textts = gtts.gTTS ("I have" + disease) 
"""
Response = "I have" + disease
Ans = {"Answer": {"audio_": Response}
       }
"""

#print(json.dumps(R, sort_keys=True));
