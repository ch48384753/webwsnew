import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webws.settings")# project_name 项目名称
django.setup()

from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from tour.models import *
from django.template import loader
import random,time

try:
    #create user
    userlist=['admin','nico','jack','harris','herman','king']
    introductionlist=['People do not start out with the search for facts，they start out with an opinion.',
                      'As I grow older, I pay less attention to what men say. I just watch what they do.',
                      'Everybody does something good, so there\'s something in there that we could do.',
                      'Without face-to face conversations, people are missing out on learning social skills.',
                      'Only those who have the patience to do simple things perfectly ever acquire the skill to do difficult things easily.',
                      'I am not judged by the number of times I fail, but by the number of times I succeed: and the number of times I succeed is in direct proportion to the number of times I fail and keep trying.']
    webuser.objects.all().delete()
    for i in range(len(userlist)):
        webuser.objects.create(username=userlist[i],password=userlist[i],introduction=introductionlist[i],email=userlist[i]+"@"+"google.com")
    #create attraction
    attractionlist=['Glasgow Cathedral Glasgow','Celtic Park','George Square']
    tourlist=["Glasgow Cathedral, also called the High Kirk of Glasgow or St Kentigern's or St Mungo's Cathedral, is the oldest cathedral on mainland Scotland and is the oldest building in Glasgow. Since the Reformation the cathedral continues in public ownership, within the responsibility of Historic Environment Scotland. The congregation is part of the established Church of Scotland's Presbytery of Glasgow and its services and associations are open to all. The cathedral and its kirkyard are at the top of High Street, at Cathedral Street. Immediately neighbouring it are Glasgow Royal Infirmary, opened in 1794, and the elevated Glasgow Necropolis, opened in 1833. Nearby are the Provand's Lordship, Glasgow`s oldest house and its herbal medical gardens, the Barony Hall, University of Strathclyde, Cathedral Square, Glasgow Evangelical Church, and St Mungo Museum.",
              "Celtic Park is a football stadium in the Parkhead area of Glasgow, and is the home ground of Celtic Football Club. With a capacity of 60,411, it is the largest football stadium in Scotland and the fifth-largest football stadium in the United Kingdom. It is commonly known by Celtic fans as either Parkhead or Paradise.",
              "George Square is the principal civic square in the city of Glasgow, Scotland. It is one of six squares in the city centre, the others being Cathedral Square, St Andrew's Square, St Enoch Square, Royal Exchange Square, and Blythswood Square on Blythswood Hill. It is the Pantheon of Glasgow and the perpetual summer and winter palace of the people."
              ]
    hotellist=["citizenM Glasgow:Very comfortable bed with crisp linen and an easily adjustable climate all combined to provide an excellent night's sleep. Very comfortable range of places to eat and drink. Great location … ",
               "Jurys Inn Glasgow:What can i say i got rhe room on a good rate but to be honest i would rather have now paid an extra £20 for a better hotel and nights sleep.I was asked where i wanted a room and i asked for …",
               "Hotel Du Vin Glasgow:Was treated to a night dinner bed and breakfast here via a voucher received as a present. I love Victorian buildings so it was right up my street. First impressions were a touch chaotic as new carpets… ",]
    attraction.objects.all().delete()
    for j in range(len(attractionlist)):
        attraction.objects.create(aid=j,aname=attractionlist[j],tour=tourlist[j],hotel=hotellist[j])
    #create review
    reviewline=["Fabulous Cathedral - amazing this building survived the The Reformation intact. Last resting place of St Kentigern (Mungo - Glasgows patron Saint) whose grave is in the undercroft. Awe inspiring high, ceiling - just beautiful!",
                "Well, a cathedral. Beautiful stained glass windows, lots of history panels to read. If you like visiting cathedrals, you'll enjoy a visit.",
                "Lovely medieval cathedral at the centre of Scottish history since the seventh century. Great relaxed feel, good explanatory plaques. There is some fantastic mid-twentieth century stained glass.",
                "The Glasgow cathedral shows the long history of Glasgow. Well mainitained and access to many areas including the impressive with its large number of columns. The Necropolis next to the catherdral make this a well worth visit.",
                "Amazing place full of interesting history I had passed hundreds of times but never visited until entertaining family from France. Across from Provands Lordship which is also very interesting and worth a visit.",
                "Glasgow Cathedral, also called the High Kirk of Glasgow or St Kentigern's or St Mungo's Cathedral is the oldest cathedral on mainland Scotland and is the oldest building in Glasgow.I was a real treat, with many details, and an underground level with plenty of history. It is even bigger than what it looks!",
                "Stunning cathedral and a must see when in Glasgow along with the Necropolis behind it. I visit here every time I am in Glasgow.",
                "The cathedral and the grave yard was a sight for sore eyes , a must see it was absolutely beautiful.",
                "We really enjoyed visiting the cathedral on our stay in Glasgow. Gives you a wonderful look into religious and architectural history. And be sure to walk down into the lower level rooms and up on the hill behind to see the Necropolis.It is magnificent!",
                "Nice building,lots of heritage going back in time,good visitor attraction and probably a must see if visiting Glasgow.",
                "We went for a day to Glasgow and we went to visit this amaizing cathedral. It's massive and impressive. Ded worth a visit if you visiting Glasgow.",
                "Eventually got round to visiting the cathedral after visiting Glasgow for many years A must see, very impressive,beautiful stained glass windows and a lot of Scottish religious history under one huge roof.",
                "In winter, this magnificent building looks all the more impressive. Some stained glass windows and stonework to compete with the best of cathedrals and without the arrogance. Wonderful and beautiful place to visit."]
    reviewlist.objects.all().delete()
    for n in range(len(userlist)*len(attractionlist)):
        reviewlist.objects.create(reviewid=n,attractionid=random.randint(1,len(attractionlist)),reviewuser=random.choice(userlist),reviewcontent=random.choice(reviewline))
    #reviewlist.objects.create(reviewid=2,attractionid=1,reviewuser="test",reviewcontent="good place t")
    print('Run population script success!')
except Exception as e:
    #raise e
    print('Error:',e)
