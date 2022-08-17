from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat
# Create your views here.
# this is just like our req inside of express
def index(request):
    return render(request, 'cats/index.html')

def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/all_cats.html', { 'cats': cats })

def cat_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/show.html', { 'cat': cat })

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats'
    template_name = 'cats/cat_form.html'

    def form_valid(self, form):
        #commit=False makes sure we don't save to the database
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/cats')

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    template_name = 'cats/cat_form.html'

    def form_valid(self, form):
        #commit=False makes sure we don't save to the database
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/cats/' + str(self.object.pk))

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'
    template_name = 'cats/cat_confirm_delete.html'
