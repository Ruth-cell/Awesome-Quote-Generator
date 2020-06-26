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
    elif int(number) == 21:
        quote = "Learn from yesterday,Live Today,Hope for tomorrow"
        image="http://www.relatably.com/q/img/hope-quotes/-Hope-quotes-36913174-462-587.jpg"
    elif int(number) == 22:
        quote = "Don't let todays disapointment cast a shadow on tomorrow's dream"
        image="https://th.bing.com/th/id/OIP.wqoIn9vR_g6tT09eUvPxcQHaL2?pid=Api&rs=1"
    elif int(number) == 23:
        quote = "Success is a journey not a destination."
        image="https://cdn.wallpapersafari.com/19/29/i2ukFe.jpg"
    elif int(number) == 24:
        quote = "Your mistakes don't define you"
        image="https://www.prettydesigns.com/wp-content/uploads/2015/05/Positive-Quotes-1.jpg"
    elif int(number) == 25:
        quote = "Be your own kind of beautiful"
        image="https://i.pinimg.com/originals/b4/07/99/b40799e262f919a9fcfe468a804797f3.jpg"
    elif int(number) == 26:
        quote = "The storms might be rough, but sunshine always returns"
        image="https://i.kym-cdn.com/photos/images/newsfeed/001/652/874/f70.gif"
    elif int(number) == 27:
        quote = "Better things are coming"
        image="data:image/jpeg;base64,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"
    elif int(number) == 28:
        quote = "I'm sending postive vibes your way and you can't stop them.You're already feeling happier"
        image="https://i.pinimg.com/originals/50/70/44/507044723a4145a74a589c4ff3dcddca.jpg"
    elif int(number) == 29:
        quote = "You can do it!You've got this!"
        image="https://ift.tt/2pEpHZg"
    elif int(number) == 30:
        quote = "Positive Mind,Positive Vibes,Positive Vibes"
        image="https://www.yourtango.com/sites/default/files/styles/body_image_default/public/2018/Positiveattitude5.jpg"
    elif int(number) == 31:
        quote = "When you've had a rough day but you're trying to stay postive.I'm fine. it's fine.Everything's just fine."
        image="https://meme.xyz/uploads/posts/t/l-9694-when-youve-had-a-rough-date-but-youre-trying-to-stay-positive.jpg"
    elif int(number) == 32:
        quote = "Train your mind to see good in every situation"
        image="https://thinkingmeme.com/wp-content/uploads/2018/04/Positive-thinking-meme7.jpg"
    elif int(number) == 33:
        quote = "Your limitation-it's only your imagination"
        image="https://www.success.com/wp-content/uploads/legacy/sites/default/files/1_16.jpg"
    elif int(number) == 34:
        quote = "Push yourself, because no one is going to do it for you"
        image="https://www.success.com/wp-content/uploads/legacy/sites/default/files/new2.jpg"
    elif int(number) == 35:
        quote = "Do one thing everyday that scares you"
        image="https://ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=1729186165&Format=_SL160_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=contentmentqu-20&language=en_US"
    elif int(number) == 36:
        quote = "Don't let anyone dull your sparkle"
        image="https://40zf3x2a45us1qbee83qm619-wpengine.netdna-ssl.com/wp-content/uploads/dontletanyonedullyoursparkle.png"
    elif int(number) == 37:
        quote = "You're braver than you believe, and stonger than you seem,and smarter than you think"
        image="https://40zf3x2a45us1qbee83qm619-wpengine.netdna-ssl.com/wp-content/uploads/youarebraverthanyoubelieveandstrongerthanyouseemandsmarterthanyouthink.png"
    elif int(number) == 38:
        quote = "When it rains look for rainbows, when its dark look for stars"
        image="https://40zf3x2a45us1qbee83qm619-wpengine.netdna-ssl.com/wp-content/uploads/whenitrainslookforrainbowswhenitsdarklookforstars.png"
    elif int(number) == 39:
        quote = "No one can make you feel inferior without your consent"
        image="https://image.shutterstock.com/image-photo/quote-best-inspirational-motivational-quotes-600w-1434337010.jpg"
    elif int(number) == 40:
        quote = "Time moves in one direction,Memory is another"
        image="https://hips.hearstapps.com/wdy.h-cdn.co/assets/16/41/wd22.jpg?crop=1xw:1.0xh;center,top&resize=768:*"
    elif int(number) == 41:
        quote = "You must be the change you see in the world"
        image="https://hips.hearstapps.com/wdy.h-cdn.co/assets/16/41/wd19.jpg?crop=1xw:1.0xh;center,top&resize=768:*"
    elif int(number) == 42:
        quote = "Never give up because great things take time"
        image="https://image.freepik.com/free-vector/lettering-typography-quote-poster-inspiration-motivation-never-give-up-because-greate-things-take-time_206410-23.jpg"
    elif int(number) == 43:
        quote = "Never be afarid to say what you feel"
        image="https://i2.wp.com/www.shihoriobata.com/wp-content/uploads/2019/01/never-be-afraid-to-say-what-you-feel.jpg?w=736&ssl=1"
    elif int(number) == 44:
        quote = "Every morning, you have the opportunity to becmoe a happier version of youself."
        image="https://i1.wp.com/www.shihoriobata.com/wp-content/uploads/2019/01/36049c8d3a540e6c582d548afb6260b4.jpg?w=564&ssl=1;;;;;;;"
    elif int(number) == 45:
        quote = "The challenge is not to be perfect... it's to be whole"
        image="https://www.ftd.com/blog/content/uploads/2019/02/inspirational-quotes-women-jane-fonda.jpg"
    elif int(number) == 46:
        quote = "If you obey all the rules, you miss all the fun"
        image="https://www.ftd.com/blog/content/uploads/2019/02/inspirational-quotes-women-katharine-hepburn.jpg"
    elif int(number) == 47:
        quote = "Learn fomr the mistkes of others.You can't live long enough to make them all yourself"
        image="https://www.ftd.com/blog/content/uploads/2019/02/inspirational-quotes-women-eleanor-roosevelt.jpg"
    elif int(number) == 48:
        quote = "Everyone shines,givin the best lighting"
        image="https://www.ftd.com/blog/content/uploads/2019/02/inspirational-quotes-women-susan-cain.jpg"
    elif int(number) == 49:
        quote = "if you don't risk anything,you risk even more"
        image="https://www.ftd.com/blog/content/uploads/2019/02/inspirational-quotes-women-erica-jong.jpg"
    elif int(number) == 50:
        quote = "To improve is to change.To be perfect is to change often"
        image="https://hips.hearstapps.com/wdy.h-cdn.co/assets/16/41/wd17.jpg?crop=1xw:1.0xh;center,top&resize=768:*"
    


    else:
        quote = "Sending Postive vibes your way"
        image="https://66.media.tumblr.com/6a664f2ac632b4691ea9d8ce22567a22/tumblr_pj3benEJ131w9t3l2_1280.jpg"
    props={
        "number": number,"quote":quote,"image":image
    }
    print(number)
    return render_template('results.html', props = props, time=datetime.now())

