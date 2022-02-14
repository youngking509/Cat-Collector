from django.shortcuts import render
# from django.http import HttpResponse
from .models import Cat

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Hello World!!!</h1>')
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



# # Add the Cat class & list and view function below the imports
# class Cat:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age

# cats = [
#   Cat('Lolo', 'tabby', 'foul little demon', 3),
#   Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#   Cat('Raven', 'black tripod', '3 legged cat', 4),
#   Cat('Rocket', 'Siamese', 'looks like rufus from kim possible', 70),
# ]

def cats_index(request):
    cats = Cat.objects.all()
    return render(request,'cats/index.html', { 'cats': cats })


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat })
