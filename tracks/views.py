from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title

from .models import Music


def home(request):
    return render(request, 'index.html')

def track_list(request):
    tracks = Music.objects.all()
    ctx = {'tracks': tracks}
    return render(request, 'tracks/music-list.html', ctx)

def track_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        date = request.POST.get('date')
        image = request.FILES.get('image')
        audio = request.FILES.get('audio')
        if title and artist and album and genre and date and image and audio:
            Music.objects.create(
                title = title,
                artist = artist,
                album = album,
                genre = genre,
                date = date,
                image = image,
                audio = audio,
            )
            return redirect('tracks:list')
    return render(request,'tracks/music-create.html')

def track_detail(request, pk):
    tracks = get_object_or_404(Music, pk=pk)
    ctx = {'tracks': tracks}
    return render(request,'tracks/music-detail.html', ctx)

def track_delete(request, pk):
    tracks = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        tracks.delete()
        return redirect('tracks:list')
    ctx = {'tracks': tracks}
    return render(request, 'tracks/music-delete-confirm.html', ctx)

def track_update(request, pk):
    tracks = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        date = request.POST.get('date')
        image = request.FILES.get('image')
        audio = request.FILES.get('audio')
        if title and artist and album and genre and date and image and audio:
            tracks.title = title
            tracks.artist = artist
            tracks.album = album
            tracks.genre = genre
            tracks.date = date
            if image:
                tracks.image = image
            if audio:
                tracks.audio = audio
            tracks.save()
            return redirect('tracks:list')
    ctx = {'tracks': tracks}
    return render(request,'tracks/music-create.html', ctx)

def track_video(request):
    return render(request,'tracks/video-list.html')