from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, UpdateForm
from myapp.views import get_global_queryset 

from myapp.models import Rating
# Create your views here.

def register (request):

    if request.method == "POST": 
         form = RegisterForm(request.POST)
         if form.is_valid():
             form.save()
             # get username 
             name = form.cleaned_data.get('first_name')
             # log user in 
             new_user = authenticate (username = name, password = form.cleaned_data.get('password1'),)
             login(request, new_user)
             messages.success(request, f'Account created for { name }!')
             return redirect('home')         

    else:
        form = RegisterForm()

    return render(request, "users/register.html", {'form': form} )
    
# decorator 
@login_required
def profile (request):
    context = {
        'title': 'Profile',
    }

    # Regular context stuff
    my_ratings = Rating.objects.filter (author = request.user)
    context['ratings'] = my_ratings

    if request.method == "POST": 
        update_form = UpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            # get username 
            name = update_form.cleaned_data.get('username')
            # log user in 
            new_user = authenticate (username = name, password = update_form.cleaned_data.get('password1'),)
            login(request, new_user)
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        update_form = UpdateForm(instance=request.user)

    # add profile update form to context
    context['update_form'] = update_form 

    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

        context['title'] = 'Search: ' + str(query) 

        # get queryset
        courses, profs = get_global_queryset(query)
        # add to context
        context['courses'] = courses
        context['profs']   = profs

        # render search page
        return render(request, "myapp/search_results.html",  context)

    return render(request, 'users/profile.html', context)
