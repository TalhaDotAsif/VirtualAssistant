import speech_recognition as sr
import os
from gtts import gTTS 
import datetime
import warnings
import calendar
import random 
import wikipedia

warnings.filterwarnings('ignore')
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print ("say something!")
        audio=r.listen()
    
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said:'+data)
    except sr.UnknownValueError:
        print('Could not understand the audio!')

    except sr.RequestError as e:
        print('Request results from google speech recog. service error'+e)

    return data
#########################################################################

def assistantRes(text):

    print(text)
    myobj = gTTS(text=text,lang='en',slow=False)

    myobj.save('response.mp3')
    os.system('start response.mp3')

def wakeWord(text):
    WAKE_WORDS = ['hey talha','okay talha']

    text=text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    
    return False

def currentDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_day.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January','February','March','April','May','June','July','August','September',
    'October','November','December']
    ordinalNums = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31th']
    return 'Today is '+weekday+''+month_names[monthNum -1]+' the'+ordinalNums[dayNum -1]+'. '

def greeting(text):
    GREETING_INPUT = ['hi','hey','hola','greetings','wassup','hello']

    GREETING_RESPONSES = ['howdy','whats good','hello','hey there']

    for word in text.split():
        if word.lower() in GREETING_INPUT:
            return random.choice(GREETING_RESPONSES)
    
    return ''
def getPreson(text):
    wordlist = text.split()
    for i in range (0,len(wordlist))
        if i+3 <= len(wordlist) -1 and wordlist[i].lower() == 'who' and word [i+1].lower() =='is':
            return wordlist[i+2] + ''+wordlist[i+3]:

while True:
    text = recordAudio()
    response = ''

    if (wakeWord(text)==True):
        #print ('You spoke the wake word or phrase')
        response = response + greeting(text)

        if ('date' in text):
            get_date = getDate()
            response = response + ''+get_date
        
        if ('time' in text):
            now = datetime.datetime.now()
            meridem = ''
            if now.hour >= 12:
                meridem = 'p.m'
                hour = now.hour -12
            else:
                meridem = 'a.m'
                hour = now.hour
            if now.minute < 10:
                minute = '0'+str(now.minute)
            
            response = response + ''+'It is '+str(hour)+':'+minute+''+meridem+' .'
 
        if ('who is ' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person,sentence=2)
            response = response +''+wiki