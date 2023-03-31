from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')   # render takes 1st argument-->request , 2nd arg--> template's name

    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    charcount=request.GET.get('charcount','off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)

    elif fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif charcount=="on":
        count = 0
        for i in djtext:
            count += 1

        params = {'purpose': 'Number of Characters', 'analyzed_text': count}
        # Analyze the text
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')




# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")
