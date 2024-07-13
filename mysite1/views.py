# i have created this file - manpreet
#from django.http import HttpResponse
#def index(request):
    #return HttpResponse('''"<h1>instagram login page</h1> <a href=https:/www.instagram.com/accounts/login/>instagram</a>"''')

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyze(request):
    dj_text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!@#$%^&*(){}[]<>?/,.\ ~`_-;:'"'''
        analyzed =""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        dj_text = analyzed


    if (fullcaps ==  "on"):
        analyzed =""
        for char in dj_text:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        dj_text = analyzed

    if (newlineremove ==  "on"):
        analyzed =""
        for char in dj_text:
            if char != "/n" and char!="\r":
              analyzed = analyzed + char

        params = {'purpose': 'Removed NewLine', 'analyzed_text': analyzed}
        dj_text = analyzed


    if (extraspaceremove ==  "on"):
        analyzed =""
        for index, char in enumerate(dj_text):
            if not(dj_text[index] == " " and dj_text[index+1] == " "):
              analyzed = analyzed + char

        params = {'purpose': 'Removed NewLine', 'analyzed_text': analyzed}
        dj_text = analyzed

    if (charcount ==  "on"):
        analyzed =("No of characters given in the text are :"+str(len(dj_text)))
        params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
        dj_text = analyzed

    if(removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on" and charcount != "on" ):
        return HttpResponse("Please Select any Operation and try again")

    return render(request, "analyze.html", params)