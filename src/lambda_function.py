import json

def health_reply(options, audio):
    #Initialise variables
    opt = list(map(lambda x: x.lower(), options))
    reply = audio.lower().split(" ")
    diseases = ["diabetes", "thyroid", "cancer", "blood"]
    
    #No diseases
    if("no" in reply or "don't" in reply or "not" in reply):
        if("None" in options):
            return ["None"]
        else:
            return []
    
    #Identify diseases
    ans = []
    for word in reply:
        if(word in diseases):
            if(word in opt):
                ans.append(options[opt.index(word)])
            elif("Others" in options):
                ans.append("Others")
    return ans

def income_reply(options, audio):
    #Initialise variables
    reply = audio.lower().split(" ")
    reply = float(audio.strip("lakh"))
    opt = list(map(lambda x: x.replace("lakh", "").split("-"), options[1:-1]))
    opt = list(map(lambda x: list(map(int, x)), opt))

    #Lowest income range
    if(reply  < opt[0][0]):
        return [options[0]]

    #Identify income range
    for i in range(len(opt)):
        if(opt[i][0] <= reply < opt[i][1]):
            return [options[i+1]]
    
    #Highest income range
    return [options[-1]]

def dob_reply(options, audio):
    #Initialise variables
    reply = audio.lower().split(" ")
    month = {
        "january": '01',
        "february": '02',
        "march": '03',
        "april": '04',
        "may": '05',
        "june": '06',
        "july": '07',
        "august": '08',
        "september": '09',
        "october": '10',
        "november": '11',
        "december": '12'
    }

    #Get date
    dd, mm, yy = '', '', ''
    numbers = []
    for word in reply:
        if(not word.isalpha()):
            numbers.append(word)
        elif(word in month):
            mm = month[word]
    
    #Identify dd,mm,yy
    for num in numbers:
        num = num.strip("st").strip("nd").strip("rd").strip("th")
        if(len(num) == 4):
            yy = num 
        elif(dd == ''):
            dd = num 
        elif(mm == ''):
            mm = num 

    return [('/').join([dd, mm, yy])]

def lambda_handler(event, context):
    #Get body of event
    body = json.loads(event["body"])
    
    #Extract values
    question_key = body["question_key"]
    options = body["options"]
    audio = body["audio"]
    
    #Evaluate answer
    ans = []
    if(question_key == "q1"):
        ans = health_reply(options, audio)
    elif(question_key == "q2"):
        ans = income_reply(options, audio)
    elif(question_key == "q3"):
        ans = dob_reply(options, audio)
    else:
        ans = ["Invalid question key"]
    
    #Format response
    response = dict()
    response["answers"] = ans
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
