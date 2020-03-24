from django.shortcuts import render, get_object_or_404
from django_filters.views import FilterView
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import (
    View,
    CreateView, 
    FormView, 
    ListView, 
    DetailView, 
    UpdateView,
    DeleteView
)

from .forms import CharacterForm
from .filters import CharacterFilter


# Create your views here.

from .models import Character, Location, Episode

def home(request):
    return render(request, 'landing.html')


# CHARACTER VIEWS
class CharacterListView(ListView):
    model = Character
    template_name = "characters/list.html"


    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        characters = CharacterFilter(self.request.GET, queryset=self.get_queryset())
        paginator = Paginator(characters.qs, 15)
        page = self.request.GET.get('page')

        query = self.request.GET.copy()
        # print(query)
        if 'page' in query:
            del query['page']
        # print(query)
        context['query'] = query
        print(query.urlencode())
        context['page'] = paginator.get_page(page)
        context['filter'] = characters
        return context


class CharacterDetailView(DetailView):
    model = Character
    template_name = "characters/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['episodes'] = self.object.episodes.all()
        return context
    
class CharacterDeleteView(DeleteView):
    model = Character
    template_name = "characters/delete.html"

    def get_success_url(self, **kwargs):
        return self.model.get_delete_url(self)
    

class CharacterCreateView(CreateView):
    model = Character
    template_name = "characters/create.html"
    form_class = CharacterForm
    success_url = f'characters/{{self.id}}'

    def get(self, requests, *args, **kwargs):
        context =  {'form': CharacterForm()}
        return render(requests, self.template_name, context)
        



class CharacterUpdateView(UpdateView):
    model = Character
    template_name = "characters/update.html"
    form_class = CharacterForm

    def get_object(self):
        id = self.kwargs.get("pk")
        return get_object_or_404(Character, id=id)



def error404(request, Exception):
    template_name = '404.html'
    return render(request, template_name)


class CharacterObjectMixin(object):
    model = Character #can be none
    lookup = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None

        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj



class LocationListView(ListView):
    model = Location
    template_name = "locations/list.html"
    paginate_by = 15

    ordering = ['id']



class LocationDetailView(DetailView):
    model = Location
    template_name = "locations/detail.html"

    
class EpisodeListView(ListView):
    model = Episode
    template_name = "episodes/list.html"
    paginate_by = 8

    ordering = ['code', 'id']


