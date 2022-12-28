from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from random import randint
from django.db.models import Q

# Create your views here.
@api_view(['GET'])
def home(request):
    friends = Friends.objects.all()
    print(type(friends))
    serializer = FriendSerializer(friends, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def reset(request):
    friends = Friends.objects.all()
    pair = Pair.objects.all().delete()
    for i in friends:
        i.selected = False
        i.hasAFriend = False
        i.save()
    return Response({"msg":"success"})

@api_view(['GET', 'POST'])
def random(request):
    if request.method == 'POST':
        count = Friends.objects.all().count()
        num1 = randint(1,count)
        friend = Friends.objects.get(id=num1)
        friend2 = Friends.objects.get(name=request.data['name'])
        if(not friend2.hasAFriend):
            while(friend.name==request.data['name'] or friend.selected):
                num1 = randint(1,count)
                friend = Friends.objects.get(id=num1)
            friend.selected = True
            friend.save()
            
            friend2.hasAFriend = True
            friend2.save()
            pair = Pair(name1=friend2, name2=friend)
            pair.save()
            serializer = FriendSerializer(friend, many=False)
            return Response(serializer.data)
        else:
            return Response({"msg":"has a friend"})
    else:
        friends = Friends.objects.all()
        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def search(request,val):
    friend = Friends.objects.filter(Q(name__icontains=val))
    serializer = FriendSerializer(friend, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def count(request):
    count = Friends.objects.all().count()
    hasFriend = Friends.objects.filter(hasAFriend=True).count()
    select = Friends.objects.filter(selected=True).count()
    return Response({
        "whoSelected": hasFriend,
        "remaining": count-select
    })