from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('About this website <br><a href=/><button>Back to Homepage</button></a>')


def contactus(request):
    return HttpResponse("Contact Us @9898989898 or abcxyz@mail.com <br><a href=/><button>Back to Homepage</button></a>")


def analyze(request):
    # get the text
    dtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    nlineremove = request.POST.get('nlineremove', 'off')
    spacerem = request.POST.get('spacerem', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        dtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == 'on':
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        dtext = analyzed
        # return render(request, 'analyze.html', params)

    if nlineremove == 'on':
        analyzed = ""
        for char in dtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        dtext = analyzed
        # return render(request, 'analyze.html', params)

    if spacerem == 'on':
        analyzed = ""
        for num, char in enumerate(dtext):
            if not (dtext[num] == " " and dtext[num + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        dtext = analyzed
        # return render(request, 'analyze.html', params)

    if charcount == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        count = 0
        for num, char in enumerate(dtext):
            if char not in punctuations and not (dtext[num] == " " and dtext[num + 1] == " ") and not char == " ":
                count += 1

        analyzed = "Number of Characters in the text : " + dtext + " is " + str(count)
        params = {'purpose': 'Counting The Characters', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if charcount != 'on' and spacerem != 'on' and nlineremove != 'on' and fullcaps != 'on' and removepunc != "on":
        return HttpResponse("Select any operation and try again !")

    return render(request, 'analyze.html', params)
