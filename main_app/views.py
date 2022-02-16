from nis import cat
from pyexpat import model
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat, Toy
from .forms import FeedingForm


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


# def cats_detail(request, cat_id):
#     cat = Cat.objects.get(id=cat_id)
#     return render(request, 'cats/detail.html', {'cat': cat })

# update this view function
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    # include the cat and feeding_form in the context
    'cat': cat, 'feeding_form': feeding_form
  })



# add this new function below cats_detail
def add_feeding(request, cat_id):
  # create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)




class CatCreate(CreateView):
    model = Cat
    fields = '__all__'

    """success_url = '/cats/'"""


class CatUpdate(UpdateView):
    model = Cat
    fields = ('breed', 'description', 'age')

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'


class ToyCreate(CreateView):
    model = Toy
    fields = ('name', 'color')

class ToyUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'