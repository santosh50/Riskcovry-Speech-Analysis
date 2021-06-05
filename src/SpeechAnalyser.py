import yake
import speech_recognition as sr

#Convert Speech to Text
r = sr.Recognizer()
sample = sr.AudioFile("sample_audio.wav")
with sample as source:
    audio = r.record(source)
    text = r.recognize_google(audio)
    print(text)

#Initialise keyword extractor
diseases = ["high blood pressure","cancer","diabetes","thyroid"]
extractor = yake.KeywordExtractor()
language = "en"
n_gram_size = 4
num_keywords = 4
deduplication_threshold = 0.4
custom_extractor = yake.KeywordExtractor(lan = language, n = n_gram_size, dedupLim = deduplication_threshold, top= num_keywords, features = None)

def get_disease_response(audio_text, options):
    #Convert to lowercase
    audio_text = audio_text.lower()

    #No diseases
    if "no" in audio_text.split(" ") or "don't" in audio_text.split(" ") and "None" in options:
        return ["None"]
    
    #Check if keywords are part of options
    ans = []
    words = custom_extractor.extract_keywords(audio_text)
    flag = 0
    for i in words:
        flag = 0
        for j in options:
            if j.lower() in i[0].split(' ') and j not in ans: #disease identified
                ans.append(j)
                flag = 1
        if flag == 0: #diseases not in options
            if "Others" in options:
                if i[0] in diseases:
                    ans.append("Others")
    return ans

#Test examples
t1="I have cancer and thyroid"
o1=["Cancer","Thyroid"]
t2="I have no disease"
o2=["Diabetes","Thyroid","Cancer","Others","None"]
t3="I have Thyroid and High Blood Pressure"
o3=["Diabetes","Thyroid","Cancer","Others","None"]
t4="I have High Blood Pressure"
o4=["Diabetes","Thyroid","Cancer","None"]

print(get_disease_response(text, o2))
