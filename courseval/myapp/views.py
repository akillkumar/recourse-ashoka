from django.contrib import messages
from django.dispatch import receiver
from django.http import HttpResponse
from django.db.models.signals import post_save
from django.views.generic.edit import DeleteView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.contrib.auth.models import User

from .models import Course, Professor, Rating, MAJORS
from .forms import RatingsForm


def index (request):
    context = {
        'title': 'Home',
    }

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

    # get additional context data
    context['total_ratings'] = len(Rating.objects.all())
    context['courses_rated'] = len(Course.objects.all())
    context['total_users']   = len(User.objects.all())
    
    return render(request, "myapp/index.html", context)

def about (request):
    context = {
        'title': 'About',
    }
    
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

        # get queryset
        courses, profs = get_global_queryset(query)
        # add to context 
        context['courses'] = courses
        context['profs']   = profs

        # render search page
        return render(request, "myapp/search_results.html",  context)

    return render(request, "myapp/about.html", context)



def search (request):
    context = {
        'title': 'Search',
    }

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

#########################################################################
#                              COURSES                                  #
#########################################################################

def list_courses (request):
    context = {
        'title': 'All courses',
        'majors': MAJORS,
    }

    # filtering
    if request.GET.get('Filter') and request.GET.get('Filter') != 'NA':
        featured = request.GET.get('Filter')
        courses = Course.objects.filter(course_listing=featured).order_by('course_name')
        context['filter']  = featured
        context['results'] = len(courses)
    elif request.GET.get('Filter') == 'NA':
        course_list =  Course.objects.all().order_by('course_name')

        # paginate
        page = request.GET.get('page', 1)

        paginator = Paginator(course_list, 10)
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)
    else:
        courses = Course.objects.filter(course_listing='FC').order_by('course_name')
        context['filter']  = "Foundation Course"
        context['results'] = len(courses)
    
    context['courses'] = courses

    
    if request.GET.get('q'):
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
    
    return render(request, "myapp/courses.html", context)

def course_detail (request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course,
        'title': course.course_name,
        'ratings': Rating.objects.filter (course = course),
    }

    retakes = 0
    num_5 = num_4 = num_3 = num_2 = num_1 = 0

    rounder = round(course.course_rating) 

    for rating in context['ratings']:
        if rating.take_again == True:
            retakes += 1
        if rating.rating==5:
            num_5 +=1 
        if rating.rating==4:
            num_4 +=1
        if rating.rating==3:
            num_3 +=1
        if rating.rating==2:
            num_2 +=1
        if rating.rating==1:
            num_1 +=1

    if course.course_number_of_ratings!=0:
        num_1=round((num_1/course.course_number_of_ratings)*100)
        num_2=round((num_2/course.course_number_of_ratings)*100)
        num_3=round((num_3/course.course_number_of_ratings)*100)
        num_4=round((num_4/course.course_number_of_ratings)*100)
        num_5=round((num_5/course.course_number_of_ratings)*100)
        retakes=round((retakes/course.course_number_of_ratings)*100)
        course.course_retakers=retakes  #for retake percentage
    
    # add all of this to context
    context['num_1']   = num_1
    context['num_2']   = num_2
    context['num_3']   = num_3
    context['num_4']   = num_4
    context['num_5']   = num_5
    context['rounder'] = rounder
    context['retakes'] = retakes

    # if we have a GET
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

    return render(request, "myapp/course_detail.html", context)

#########################################################################
#                             PROFESSORS                                #
#########################################################################

def list_profs (request):
    context = {
        'title': 'All Professors',
        'majors': MAJORS,
    }

    # filtering
    if request.GET.get('Filter') and request.GET.get('Filter') != 'NA':
        featured = request.GET.get('Filter')
        profs = Professor.objects.filter(prof_dep=featured).order_by('prof_name')
        context['filter']  = featured
        context['results'] = len(profs)
    else:
        prof_list =  Professor.objects.all().order_by('prof_name')

        # paginate
        page = request.GET.get('page', 1)

        paginator = Paginator(prof_list, 18)
        try:
            profs = paginator.page(page)
        except PageNotAnInteger:
            profs = paginator.page(1)
        except EmptyPage:
            profs = paginator.page(paginator.num_pages)
    
    context['professors'] = profs

    if request.GET.get('q'):
        query = request.GET['q']
        context['query'] = str(query)

        context['title'] = 'Search: ' + str(query) 

        # get queryset
        courses, profs = get_global_queryset(query)
        # add to context
        context['courses'] = courses
        context['profs']   = profs

        return render(request, "myapp/search_results.html",  context)
    
    return render(request, "myapp/professors.html", context)

def prof_detail (request, slug):
    prof = get_object_or_404(Professor, slug=slug)

    context = {
        'professor': prof,
        'title': prof,
    } 

    courses = Course.objects.filter (course_prof = prof)

    course_names = []

    prof_rating     = 0
    prof_difficulty = 0
    prof_retake     = 0
    prof_grade      = 0

    # get cumulative stats from prof's courses
    for course in courses:
        prof_rating     += course.course_rating
        prof_grade      += course.grade_point
        prof_retake     += course.course_retakers
        prof_difficulty += course.course_difficulty

        course_names.append(course.course_name)

    # calculate averages
    if courses:
        prof_rating     =round (prof_rating/len(courses),2)
        prof_grade      = round(prof_grade/len(courses),2)
        prof_retake     = round((prof_retake/len(courses))*100)
        prof_difficulty =round(prof_difficulty/len(courses),2)

    my_courses = zip(courses, course_names)

    # add this shiz to context
    context['my_courses']      = my_courses
    context['prof_rating']     = prof_rating
    context['prof_grade']      = prof_grade
    context['prof_retake']     = prof_retake
    context['prof_difficulty'] = prof_difficulty

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
    
    return render(request, "myapp/professor_detail.html", context)


#########################################################################
#                              RATINGS                                  #
#########################################################################   

# make sure people can only rate if logged in 
@login_required
def RateCourse (request, slug):
    # get the course we are rating
    myCourse = get_object_or_404(Course, slug=slug)

    if request.method == 'POST':
        form = RatingsForm (request.POST)
        if form.is_valid():
            # save it as an object so we can add other stuff
            rating = form.save(commit=False)
            rating.course = myCourse
            rating.author = request.user
            rating.save() # Finally save it!
            messages.success(request, f'Your rating has been recorded!') # send visual confirmation to user
            # also update course stuff
            myCourse.course_number_of_ratings+=1

            if rating.take_again:
                myCourse.course_retakers += 1
             
            # update average rating
            if rating.grade=='A':
                myCourse.gp_sum += 4.0
                myCourse.grade_offered += 1
                
            if rating.grade=='A-':
                myCourse.gp_sum += 3.7
                myCourse.grade_offered += 1
                
            if rating.grade=='B+':
                myCourse.gp_sum += 3.3
                myCourse.grade_offered += 1
                
            if rating.grade=='B':
                myCourse.gp_sum += 3.0
                myCourse.grade_offered += 1
         
            if rating.grade=='B-':
                myCourse.gp_sum += 2.7
                myCourse.grade_offered += 1
          
            if rating.grade=='C+':
                myCourse.gp_sum += 2.3
                myCourse.grade_offered += 1
          
            if rating.grade=='C':
                myCourse.gp_sum += 2.0
                myCourse.grade_offered += 1
            
            if rating.grade=='C-':
                myCourse.gp_sum += 1.7
                myCourse.grade_offered += 1
           
            if rating.grade=='F':
                myCourse.grade_offered +=1
              
            if myCourse.grade_offered != 0:
                myCourse.grade_point=myCourse.gp_sum/myCourse.grade_offered

            myCourse.rating_sum += rating.rating
            myCourse.difficulty_sum += rating.difficulty
            if myCourse.course_number_of_ratings!=0:
                myCourse.course_rating = myCourse.rating_sum/myCourse.course_number_of_ratings
                myCourse.course_difficulty = myCourse.difficulty_sum/myCourse.course_number_of_ratings
            # update average difficulty  
            myCourse.save()
            return redirect('course-detail', slug=slug)
    else:
        form = RatingsForm ()

    context = {
        'title': "Rate {}".format(myCourse),
        'form': form,
        'course': myCourse,
        'n': range(3),
        'roarer' : 5-round(myCourse.course_rating),
    }

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

    # check if user has already rated this 
    context['previous'] = Rating.objects.filter(course=myCourse, author=request.user)

    return render(request, "myapp/rating.html", context)

# make sure people can only delete if logged in 
@login_required
def delete_rating (request, pk):
    rating = get_object_or_404(Rating, id=pk)

    context = {
        'title': 'Delete Rating',
        'rating': rating,
    }

    # if someone other than the author tryna delete xwe throw an error
    if rating.author != request.user:
        context['error'] = 'Segmentation fault, core dumped'


    if request.method == "POST":
        rating.delete()
        return redirect ('profile')
    
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
    
    return render(request, "myapp/delete.html", context)


#########################################################################
#                          HELPER FUNCTIONS                             #
#########################################################################

def get_global_queryset (query=None):
    
    course_list = []
    prof_list   = []

    queries = query.split(" ")

    for q in queries:
        # search for courses
        courses = Course.objects.filter (
            Q(course_name__icontains=q) |
            Q(course_code__icontains=q) |
            Q(course_type__icontains=q) |
            Q(course_description__icontains=q) |
            Q(course_listing__icontains=q)
        ).distinct()

        # search for professors
        profs = Professor.objects.filter (
            Q(prof_name__icontains=q) |
            Q(prof_dep__icontains=q ) 
        ).distinct()

        for course in courses:
            course_list.append(course)

        for prof in profs:
            prof_list.append(prof)

    
    # make sure its unique
    return list(set(course_list)), list(set(prof_list))