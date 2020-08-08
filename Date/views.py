from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import datetime


@api_view(["POST"])

def Prime(Date):
    try:
        for i in range(2,Date):
                if Date%i==0:
                    break
                else:
                    return JsonResponse(Date)
    except:
        return Response("today date is not a prime number")

currentdate = datetime.datetime.now()
# currentdate= datetime.datetime(2020, 5, 19)
date=currentdate.day
Prime(date)
