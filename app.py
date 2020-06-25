# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
      return render_template('index.html',time=datetime.now())

@app.route('/results' , methods = ['GET', 'POST'])
def results():
    number = request.form['number']
    quote = ""
    if int(number) == 1:
        quote = "Enjoy the lttle things for one day you might look back and realize they were the big things"
        image="data:image/jpeg;base64,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"
    elif int(number) == 2:
        quote = "Adult hood is like the vet,and we're all dogs that were exicted for the car ride until we realized where we're going."
        image="https://i.pinimg.com/originals/45/cc/e2/45cce24b6cab97034ec5b31c5627122c.jpg"
    elif int(number) == 3:
        quote = "May your choices reflect your hopes, not your fears."
        image="https://christihegstad.com/content/uploads/2017/02/Background-Sunrise-color-quote-mandela-hopes-fears-choices.jpg"
    elif int(number) == 4:
        quote = "Today I will not stress over the things I can not control"
        image="https://i.pinimg.com/564x/b3/ea/e1/b3eae19bf41c4c86bd9f5622712b0dcf.jpg"
    elif int(number) == 5:
        quote = "If ever you find yourself doubting, you can make it through a challenge, to everything you've overcome in the past"
        image="https://img.ifunny.co/images/7840d738529ab67fddd3fa72dc92ffff392b7faeea7aaa114553f6db9c6fa1c0_1.jpg"
    elif int(number) ==6:
        quote = "You only fail when you stop trying."
        image="http://thefunnybeaver.com/wp-content/uploads/2016/08/Great-Inspirational-Quotes-you-are-going-to-love-pictures-007.jpg"
    elif int(number) == 7:
        quote = "Don't let the scale define you.Be Active.Eat Healthy.Be Happy"
        image="https://www.natalieshealth.com/wp-content/uploads/2018/11/Motivational-QUOTES-Monday-Motivation-37.jpg"
    elif int(number) == 8:
        quote = "You're like the ocean,pretty enough on the surface but dive down into your depths,you'll find beauty MOST PEOPLE NEVER SEE."
        image="http://vollanza.com/wp-content/uploads/2014/06/deep-beauty.jpg"
    elif int(number) == 9:
        quote = "Work hard,dream big,never give up"
        image="https://i.pinimg.com/736x/db/60/c9/db60c9ec06a2979ed9d212c0957a0b61.jpg"
    elif int(number) == 10:
        quote = "Stop saying I wish Start saying I will."
        image="https://i.pinimg.com/736x/1f/bf/0c/1fbf0c7594da4727f7ce5c16963a2ffe.jpg"
    elif int(number) == 11:
        quote = "Everyday may not be good But there's good in everyday."
        image="https://i.pinimg.com/originals/c1/6c/22/c16c22f8e255cff3051d1b70d0db7916.jpg"
    elif int(number) == 12:
        quote = "Today is the perfect day to be happy"
        image="https://i.pinimg.com/originals/60/47/18/6047182bb9d9701a67f43335852b3344.jpg"
    elif int(number) == 13:
        quote = "Dream without fear,love without limits."
        image="https://stylishlyme.com/wp-content/uploads/2019/05/cute-love-quotes.jpg"
    elif int(number) == 14:
        quote = "Life changes very quickly,in a very postive way,if you let it,"
        image="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-lindsey-vonn-1562000226.png"
    elif int(number) == 15:
        quote = "We were born to be REAL not to be PERFECT"
        image="https://content.thriveglobal.com/wp-content/uploads/2019/05/beautiful-short-quotes.jpg"
    elif int(number) == 16:
        quote = "Don't let the silly things steal your happiness"
        image="https://cdn.powerofpositivity.com/wp-content/uploads/2015/01/steal-happiness-quote-1024x1024.jpg"
    elif int(number) == 17:
        quote = "Believe in yourself"
        image="http://getwallpapers.com/wallpaper/full/4/3/5/1046197-cute-wallpapers-with-quotes-1242x2208-for-android-tablet.jpg"
    elif int(number) == 18:
        quote = "There are so many beautiful reasons to be happy"
        image="https://th.bing.com/th/id/OIP.6Aq-TvE4K3U-tGrqhkxOxwHaJ3?pid=Api&rs=1"
    elif int(number) == 19:
        quote = "The best is yet to come"
        image="https://i.ytimg.com/vi/VVibaEuuXn4/maxresdefault.jpg"
    elif int(number) == 20:
        quote = "Rise above the storm and you will find the sunshine"
        image="https://www.dreamsquote.com/wp-content/uploads/2019/06/woman-positive-quotes-40-Motivational-Quotes-For-Women-On-Strength-And-Leadership.png"


    else:
        quote = "Sending Postive vibes your way"
        image="https://66.media.tumblr.com/6a664f2ac632b4691ea9d8ce22567a22/tumblr_pj3benEJ131w9t3l2_1280.jpg"
    props={
        "number": number,"quote":quote,"image":image
    }
    print(number)
    return render_template('results.html', props = props, time=datetime.now())

