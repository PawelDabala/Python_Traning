import re
from unittest import result
from django.http import Http404
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

# Create your views here.
# def sport_view(request):
#     return HttpResponse(articles['sports'])

# def finance_view(request):
#     return HttpResponse(articles['finance'])

def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        #użycie HttpResponseNotFound
        # result = 'No Page for that topic'
        # return HttpResponseNotFound(result)

        raise Http404("404 Generic Error")


def add_view(request, num1, num2):
    #domian.com/my_app/num1/num2  --> num1+num2
    add_result = num1 + num2
    result = f'{num1}+{num2} = {add_result}'
    return HttpResponse(str(result))