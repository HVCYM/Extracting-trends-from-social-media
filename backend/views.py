from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from .models import Card
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import CardSerializer

# from Tweet_extractor import start_extracting_tweets
from backend.Tweet_extractor import start_extracting_tweets
import time

def print_date_time():
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    return 

@api_view(["GET"])
def over_view(request):
    print("over_view")
    api_urls={
        
        "Phones":"/phones_list",
        "Electronics":"/electronics_list",
        "Fashion":"/fashion_list",
        "Shoes":"/shoes_list",
        
    }
    return Response(api_urls)

def home(request):
    print_date_time()
    print("Extracting has Started!")
    start_extracting_tweets.starting_file()
    return
    # return render(request,"index.html")

@api_view(["GET"])
def tasklist(request):
    tasks =Card.objects.all()
    serialize=CardSerializer(tasks,many=True)
    return Response(serialize.data)

@api_view(["GET"])
def electronics_list(request):
    tasks = Card.objects.filter(Category="Electronics")
    serialize=CardSerializer(tasks,many=True)
    return Response(serialize.data)

@api_view(["GET"])
def fashion_list(request):
    tasks = Card.objects.filter(Category="Fashion")
    serialize=CardSerializer(tasks,many=True)
    return Response(serialize.data)

@api_view(["GET"])
def phones_list(request):
    tasks = Card.objects.filter(Category="Phones")
    serialize=CardSerializer(tasks,many=True)
    return Response(serialize.data)

@api_view(["GET"])
def shoes_list(request):
    tasks = Card.objects.filter(Category="Shoes")
    serialize=CardSerializer(tasks,many=True)
    return Response(serialize.data)





