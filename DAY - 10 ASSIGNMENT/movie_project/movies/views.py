from django.shortcuts import render
from django.http import JsonResponse 

# Dummy Movie data

movies = [
    {
        'id': 1,
        'title': 'Inception',
        'year': 2010,
        'poster': 'inception',
    },
    {
        'id': 2,
        'title': 'Interstellar',
        'year': 2014,
        'poster': 'interstellar',
    },
    {
        'id': 3,
        'title': 'The Dark Knight',
        'year': 2008,
        'poster': 'the_dark_knight',
    },
    {
        'id': 4,
        'title': 'Avengers: Endgame',
        'year': 2019,
        'poster': 'avengers_endgame',
    },
    {
        'id': 5,
        'title': 'Titanic',
        'year': 1997,
        'poster': 'titanic',
    },
    {
        'id': 6,
        'title': '3 Idiots',
        'year': 2009,
        'poster': '3_idiots',
    },
    {
        'id': 7,
        'title': 'Jawan',
        'year': 2023,
        'poster': 'jawan',
    },
]
def movie_list(request):
    return render(request,'movies/movie_list.html')

def movie_list_view(request):
    return render(request,'movies/movie_list.html',{'movies':movies})

def movie_detail_view(request,id):
    movie = None 
    for m in movies:
        if m[id] == id: 
            movie = m 
            break

    return render(request,'movies/movie_details.html',{'movie':movie})

def movie_json_view(request):
    return JsonResponse({'movies':movies})
