from django.urls import path

from django.views.generic import RedirectView
from . import views

urlpatterns = [
    #index

    path('', views.index, name='index'),
    path('homepage', views.index, name='index'),

    path('Homepage', views.index, name='index'),
    #SignUp
    path('SignUp', views.signup, name='SignUp'),
    #LogIn
    path('SignIn', views.signin, name='SignIn'),
    path('SignOut', views.signout, name='SignOut'),
    #ChosenAttraction
    path('Attraction', views.allattractions, name='allattractions'),
    path('ChosenAttraction/Attraction', views.allattractions, name='allattractions'),
    path('ChosenAttraction', views.allattractions, name='allattractions'),

    #AddReview
    path('AddReview', views.addreview, name='AddReview'),

    path('ChosenAttraction/Intro/<int:aid>', views.intro, name='Intro'),
    path('ChosenAttraction/Intro/Tour/<int:aid>', views.tour, name='Tour'),
    path('ChosenAttraction/Intro/RecommendHotel/<int:aid>', views.recommendhotel, name='RecommendHotel'),
    path('ChosenAttraction/<int:aid>', views.intro, name='intro'),
    #Profile
    path('Profile', views.profile, name='Profile'),


    path('init', views.init, name='init'),




]