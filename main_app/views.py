import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# this is just like our req inside of express
def index(request):
    return render(request, 'cats/index.html')

def cat_index(request):
    return render(request, 'cats/all_cats.html', { 'cats': cats })

class Cat:
    def __init__(self, name, breed, des, age):
        self.name = name
        self.breed = breed
        self.des = des
        self.age = age

cats = [
    Cat('Arya', 'Main Coon', 'Bites', '14'),
    Cat('Tootsie', 'Siamse', 'Small cat but cute', '17'),
    Cat('Tofu', 'SIC Short hair', 'hair elemental', '13'),
    Cat('Lucyfur', 'SIC Black hair', 'sits on laptops', '6')
]