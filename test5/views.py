from test5.forms import RateFormmm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader

# Create your views here.
def Rateeee(request):
    # movie = Movie.objects.get(imdbID=imdb_id)
    user = request.user
    
    if request.method == 'POST':
        form = RateFormmm(request.POST)
        if form.is_valid():
            rateeee = form.save(commit=False)
            rateeee.user = user
            # rate.movie = movie
            rateeee.save()
            return HttpResponseRedirect(reverse('movie-details'))
            # return HttpResponseRedirect(reverse('movie-details', args=[imdb_id]))
    else:
        form = RateFormmm()
        
    template_name = loader.get_template('rate.html')
    
    context = {
        'form': form, 
        # 'movie': movie,
    }
    
    return HttpResponse(template_name.render(context, request))
    