# created by Me....
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html")
    # return HttpResponse("Home")
def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    countnoword = request.POST.get('countnoword', 'off')
    remspc = request.POST.get('remspc', 'off')
    capitalfirst = request.POST.get('capitalfirst', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)
    elif (fullcaps=='on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalize Your given Paragraphs:', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)

    # elif newlineremover == "on":
    #     analyzed = ""
    #     for char in djtext:
    #         if char != "\n":
    #             analyzed = analyzed + char.upper()
    #     params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'REMOVE THE NEW LINES:', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)

    elif countnoword == 'on':
        x = len(djtext)
        params = {'purpose': 'COUNT NUMBER OF WORDS:', 'analyzed_text': x}
        return render(request, 'analyse.html', params)

    elif remspc == 'on':
        analyzed = djtext.replace(" ","")
        params = {'purpose': 'REMOVE THE NEW LINES:', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)

    elif (capitalfirst=='on'):
        analyzed = djtext.capitalize()
        params = {'purpose': 'Capitalize Your given Paragraphs:', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', params)

    else:
        return HttpResponse('Error')
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def spaceremove(request):
#     return HttpResponse("spaceremover <a href='/' >Back</a>")
# def charcount(request):
#     return HttpResponse("charcount ")
