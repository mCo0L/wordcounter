import operator

from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count = len(wordlist)
    word_count = dict()
    for word in wordlist:
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
    sorted_words = sorted(word_count.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'count': count, 'sorted_words': sorted_words})


def about(request):
    return HttpResponse('Made by Mukul')
