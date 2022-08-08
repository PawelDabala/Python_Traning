import re
from unittest import result
from django.http import Http404
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect
from django.urls import reverse

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

#REDARETING
# domain.com/first_app/0 ----> domain.com/first_app/finance
def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]

    #uzycie funkcji reverse
    """
    dodaz nazwę w urls.
    - nazwe uzyj w funcji reverse 
    - po nazwie można uzyc args lub kwargs do wyswietlania odpowiedniej strony
    """
    webpage = reverse("topic-page", args=[topic])
    return HttpResponsePermanentRedirect(topic)

#tamplates
def simple_view(request):
    return render(request, 'first_app/example.html')

