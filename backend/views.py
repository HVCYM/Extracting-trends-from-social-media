from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from .models import Card,HashtagList,Uploadfile
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import CardSerializer
import json
from io import BytesIO

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

@api_view(["GET","POST"])
def tasklist(request):
    if request.method == 'POST':
        # print(request.POST)
        if len(list(request.POST))==12:
            # print(len(l))
            category = request.POST["category"]
            url = request.POST["url"]
            tweet_Text = request.POST["tweet"] 
            trend_score = request.POST["score"]
            iMAGE_URL= request.POST["image"] 
            video_url=request.POST["video"] 
            id=request.POST["item_id"] 
            brand=request.POST["brand"] 
            sub_category=request.POST["sub"] 
            flipkart_url=request.POST["flipkart_url"] 
            product_image=request.POST["product_image"] 
            title=request.POST["product_title"] 
            form = Card(Category= category,url=url, Tweet_Text=tweet_Text,  Trend_score=trend_score,  IMAGE_URL=iMAGE_URL,
                video_img_url=video_url, item_id=id, Brand=brand, Sub_Category=sub_category,
                Flipkart_url=flipkart_url, product_image_link=product_image, product_title=title)
            form.save()
        elif request.FILES["file"]:
            # print("dddddddddd")
            request_file = request.FILES
            my_file = request_file['file']
            filename = BytesIO(my_file.read())
            data=filename.read().decode()
            data=json.loads(data)
            for obj in data:
                form = Card(Category= obj["Category"],url=obj["url"], Tweet_Text=obj["Tweet_Text"],  Trend_score=obj["Trend_score"],  IMAGE_URL=obj["IMAGE_URL"],
                video_img_url=obj["video_img_url"], item_id=obj["item_id"], Brand=obj["Brand"], Sub_Category=obj["Sub_Category"],
                Flipkart_url=obj["Flipkart_url"], product_image_link=obj["product_image_link"], product_title=obj["product_title"])
                form.save()
                # print(type(obj))
            # form.save()
        else:
            id=request.POST["item_id"] 
            hashtagList=request.POST["hashtag"]
            form = HashtagList(item_id=id, hash_tag=hashtagList)
            # print(request.POST)
            form.save()
    # print(list(HashtagList.objects.filter(item_id=1552349349283250177)))
    tasks =Card.objects.all()
    serialize=CardSerializer(tasks,many=True)
    return Response(serialize.data)

@api_view(["GET","POST"])
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





