from django.shortcuts import render


def homePage(request):
    page = "home"
    context = {'page':page}
    return render(request, 'home.html', context)


def eventsPage(request):
    page = 'events'
    context = {'page':page}
    return render(request, 'pages/events.html', context)
