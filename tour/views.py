from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.template import loader
import random,time

def index(request):

    listall = webuser.objects.all()
    template = loader.get_template('tour/index.html')

    if request.session.get('username',None):
        username = request.session['username']
        context = {'authusername': username}
    else:
        context = {
            'listall': listall,
        }

    return HttpResponse(template.render(context, request))

def reindex(request):
    return render(request,'tour/reindex.html')


def signup(request):
    if request.method == 'POST':
        print("sign up post")
        username = request.POST.get('username')
        if webuser.objects.filter(username=username).exists():
            return HttpResponse('The Username have exist!<a href="/">Back</a>')
        else:
            password = request.POST.get('password')
            introduction = request.POST.get('introduction')
            email = request.POST.get('email')
            password = (password)
            webuser.objects.create(username=username, password=password,introduction=introduction,email=email)
            #webuser.objects.
            return HttpResponseRedirect('/SignIn')
    else:
        print("sign up get")
        #raise Http404("Question does not exist")
        return render(request,'tour/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = (password)
        if webuser.objects.filter(username=username).exists():
            dbuser = webuser.objects.get(username=username)
            if (password == dbuser.password):
                request.session['username'] = username
                context={'authusername':username}
                return render(request,'tour/index.html',context)
            else:
                raise Http404("Username does not exist")
            #
        else:
            raise Http404("Username does not exist")
    else:
        #raise Http404("Question does not exist")
        return render(request,'tour/signin.html')

def signout(request):
    del request.session['username']
    return render(request,'tour/index.html')

def allattract(request):
    listall = webuser.objects.all()
    output = ', '.join([one.username for one in listall])
    return HttpResponse("Hello, world. You're at the  index.list"+str(output))

def results(request, aid):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % aid)

def profile(request):
    listall = webuser.objects.all()
    template = loader.get_template('tour/profile.html')
    if request.session.get('username',None):
        username = request.session['username']
        if webuser.objects.filter(username=username).exists():
            dbuser = webuser.objects.get(username=username)
            context = {'authusername': dbuser.username,
                       'introduction':dbuser.introduction,
                       'email':dbuser.email}
    else:
        context={}
    return HttpResponse(template.render( context,request))

def allattractions(request):
    listall = attraction.objects.all()
    template = loader.get_template('tour/allattractions.html')
    context = {
        'allattraction': listall,
    }
    return HttpResponse(template.render(context, request))

def intro(request,aid):
    listall = attraction.objects.all()
    template = loader.get_template('tour/attraction.html')
    context = {
        'listall': listall,
    }
    rlist=[]
    if attraction.objects.filter(aid=aid).exists():
        oneat=attraction.objects.get(aid=aid)
        if reviewlist.objects.filter(attractionid=aid).exists:
            rlist=reviewlist.objects.filter(attractionid=aid)
        if request.session.get('username',None):
            username = request.session['username']
        context = { "authusername":username,
                    "aid":oneat.aid,
                    "attractionname":oneat.aname,
                    "allrecommend":rlist
                  }
    return HttpResponse(template.render(context, request))

def tour(request,aid):
    listall = webuser.objects.all()
    if attraction.objects.filter(aid=aid).exists():
        oneat=attraction.objects.get(aid=aid)
        
        context = {
                    'atour': oneat.tour,
                 }
    template = loader.get_template('tour/tour.html')
    
    return HttpResponse(template.render(context, request))
#recommendhotel
def recommendhotel(request,aid):
    listall = webuser.objects.all()
    if attraction.objects.filter(aid=aid).exists():
        oneat=attraction.objects.get(aid=aid)
        
        context = {
                'ahotel': oneat.hotel,
                }
    template = loader.get_template('tour/recommendhotel.html')

    return HttpResponse(template.render(context, request))
def addreview(request):
    if request.method == 'POST':
        print("addreview")
        rid=len(reviewlist.objects.filter())+1
        print(rid)
        aid = request.POST.get('attractionid')
        username = request.POST.get('username')
        reviewcontent = request.POST.get('reviewcontent')

        reviewlist.objects.create(reviewid=rid,attractionid=aid,reviewuser=username, reviewcontent=reviewcontent)
        
        return HttpResponseRedirect('/ChosenAttraction/Intro/'+aid)
    else:
        print("addreview get")
        #raise Http404("Question does not exist")
        return render(request,'tour/signup.html')

def init(request):
    e=""
    try:
        webuser.objects.all().delete()
        webuser.objects.create(username="admin",password="admin",introduction="hello world!",email="admin@admin.com")
        webuser.objects.create(username="tests",password="tests",introduction="hello world!",email="admin@admin.com")    
        attraction.objects.all().delete()
        attraction.objects.create(aid=1,aname="tour test1",tour="good tour1",hotel="good hotel1")
        attraction.objects.create(aid=2,aname="tour test2",tour="good tour2",hotel="good hotel2")
        reviewlist.objects.all().delete()
        reviewlist.objects.create(reviewid=1,attractionid=1,reviewuser="admin",reviewcontent="good place1")
        reviewlist.objects.create(reviewid=2,attractionid=1,reviewuser="test",reviewcontent="good place t")
    
    except Exception as e:
        raise e
    return HttpResponse("ok"+e)

