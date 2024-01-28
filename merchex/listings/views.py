from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django1</h1>
        <p>My Favorites Group are:<p>
        <ul>
        <li>{bands[0].name}</li>
        <li>{bands[1].name}</li>
        <li>{bands[2].name}</li>
        </ul>
""")


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
