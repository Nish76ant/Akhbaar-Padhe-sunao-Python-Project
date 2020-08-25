#Akshbaar Padhke Sunao
import requests 
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today ..Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=9b3c070d43054ef99e425c32d0772482"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news..listen carefully")
