from django.http import Http404
from django.shortcuts import render
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})
    # We can use context = {'all_albums': all_albums}, but as its used only once, lets condense

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('Album Does not exits')
    return render(request, 'music/detail.html', {'album': album})
