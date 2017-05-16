from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>This is the Music app homepage</h1>')


def detail(request, album_id):
    return HttpResponse('<h2>Detail for Album </h2>')
