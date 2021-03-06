# Riskcovry-Speech-Analysis
Speech Analysis Web API for Riskcovry Hackathon

## Team : AutoSquad_R10 / RSA_

## Members:
* Risiraj Dey
* Santosh Vasisht
* Akhil Eppa

## Problem Statement 1

Create a speech analysis module (Web Based) where certain questions such as
below could be asked by the system(text form), and the specific intent of the
answer should be displayed.
```
E.g.,
Question:- “Do you suffer from any health diseases?”
Possible Speech Answers:- “Yes, I suffer from Diabetes”, “Diabetes”, “No, i don’t have
any diseases”, “I have heart disease and diabetes”, etc.
Output Scenarios:-
For UI - output can be presented in any way.
For API - Response (attached at the end (Note(1.a))
Question SET
1. Do you suffer from any health diseases?
2. What’s your annual income?
3. What is your dob?
Bonus:- Users can have multiple ways of answering, try to cover most of the common
intents.
```
## Problem Statement 1 Test Cases:

Note(1.a)
```
question: Do you suffer from any health diseases?
case 1)
Request:
{
“question_key”: "q1",
“options”:["Diabetes","Thyroid","Cancer"]
“audio”: base {} audio // "I have cancer and thyroid
}
Response:
{
“answers”: ["Cancer","Thyroid"]
}
case 2)
Request:
{
“question_key”:"q1",
“options”:["Diabetes","Thyroid","Cancer","Others","None"]
“audio”: base {} audio // "I have no disease"
}
Response:
{
“answers”:["None"]
}
case 3)
Request {
“question_key”:"q1",
“options”:["Diabetes","Thyroid","Cancer","Others","None"]
“audio”: base {} audio // "I have Thyroid and High Blood pressure "
}
Response:
{
“answers”:["Thyroid","Others"]
}case 4)
Request:
{
“question_key”:"q1",
“options”:["Diabetes","Thyroid","Cancer","None"]
“audio”: base {} audio // "I have High Blood pressure "
}
Response:
{
“answers”:[]
}
Question: What’s your annual income?
Disclaimer:"All answers will be in lakh"
case 1)
Request {
“question_key”:"q2",
“options”:[<2lakh,"2lakh-5lakh","5lakh-10lakh","10lakh>"]
“audio”: base {} audio // "7lakh"
}
Response:{
“answers”:["5lakh-10lakh"]
}
case 2)
Request {
“question_key”:"q2",
“options”:["<5lakh","5lakh-15lakh","15lakh-20lakh","20lakh>"]
“audio”: base {} audio // "3lakh"
}
Response:{
“answers”:["<5lakh"]
}
Question:"What is your dob?"Disclaimer:"All the answers be DD/MM/YYYY format"
case 1)
Request:
{
“question_key”:"q3",
“options”:[],
“audio”: base {} audio // 23rd december 1998
}
Response:
{
“answers”:["23/12/1998"]
}
case 2)
Request:
{
“question_key”:"q3",
“options”:[],
“audio”: base {} audio // "22 10 1998"
}
Response:
{
“answers”:["22/10/1998"]
}
case 3)
Request:
{
question_key:"q3",
options:[],
audio: base {} audio // "1998 10 22"
}
Response:
{
“answers”:["22/10/1998"]
}
```
## Proposed Solution
* According to the given JSON, the options are generated as the user speaks about health diseases/dob/salary.
* The audio file is a .ogg one encoded in base64. Since .ogg files are difficult to process, it's converted to .wav format.
* From then on, after getting the text from speech, we extract certain keywords/alphanumeric characters from dob response, disease response, and income response to display the result.
## API endpoint
https://a7lpc4ud64.execute-api.us-east-1.amazonaws.com/beta


