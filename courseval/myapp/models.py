from django.db import models
from django.urls import reverse
from django.utils import timezone 
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Departments
MAJORS = (
    ('NA',  'NA'),
    ('ENG', 'English'),
    ('POL', 'Political Science'),
    ('MAT', 'Mathematics'),
    ('ECO', 'Economics'),
    ('HIS', 'History'),
    ('SOA', 'Sociology and Anthro'),
    ('PSY', 'Psychology'),
    ('PHI', 'Philosophy'),
    ('BIO', 'Biology'),
    ('PHY', 'Physics'),
    ('CHM', 'Chemistry'),   
    ('FIN', 'Finance'),
    ('CS',  'Computer Science'),
    ('CC',  'Co-Curricular'),
    ('FC',  'Foundation Course'),
    ('CW',  'Creative Writing'),
    ('ES',  'Environmental Studies'),
    ('ENT', 'Entrepreneurship'),  # bro did I spell that right
    ('MS',  'Media Studies'),
    ('IR',  'International Relations'),
    ('PA',  'Performing Arts'),
    ('VA',  'Visual Arts'),
)

class Professor (models.Model):
    prof_name    = models.CharField(max_length = 50, default = "")
    prof_dep     = models.CharField(max_length=30, default="", choices=MAJORS)
    prof_pic     = models.CharField(max_length=100, default="")

    slug = models.SlugField (unique=True)

    def __str__(self):
        return self.prof_name

    def get_absolute_url(self):
        return reverse ('professor-detail', kwargs = {self.slug} )

class Course (models.Model):
    course_name         =  models.CharField(max_length = 100, default = "")
    course_code         =  models.CharField(default = "", max_length=100)            
    course_type         =  models.CharField(max_length = 5, default = "") # major/ FC/ CC etc
    course_description  =  models.TextField(default="")
    
    # slug
    slug = models.SlugField (unique=True)

    course_listing = models.CharField(max_length=30, default="NA", choices=MAJORS) # which major
    course_cross   = models.CharField(max_length=30, default="", choices=MAJORS, null = True) # cross listed major

    # Foreign Key to Professor model
    course_prof    = models.ForeignKey(Professor, on_delete = models.CASCADE, null = True)

    # course statistics 
    course_rating     = models.FloatField(default = 0) # avg rating
    rating_sum        = models.IntegerField(default=0)
    course_difficulty = models.FloatField(default = 0.0) # avg difficulty
    difficulty_sum    = models.IntegerField(default = 0)
    gp_sum            = models.FloatField(default=0)
    grade_point       = models.FloatField(default=0)
    grade_offered     = models.IntegerField(default=0)
    course_grade      = models.FloatField(default=0.0)
    course_retakers   = models.IntegerField(default=0)
    course_attendance = models.BooleanField(default=True)

    # total number of ratings
    course_number_of_ratings = models.IntegerField(default = 0) 

    # modify the default save function
    def save(self, *args, **kwargs):
        # manage floating point precision for averages
        self.course_rating = round(self.course_rating, 2)
        self.course_difficulty = round(self.course_difficulty, 2)
        self.grade_point=round(self.grade_point,2)
        # call the OG save function with rounded values
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return '{0}-{1}'.format(self.course_listing, self.course_code)

    def get_absolute_url (self):
        return reverse ('course-detail', kwargs = {self.slug} )

class Rating (models.Model):
    course = models.ForeignKey (Course, on_delete = models.CASCADE)
    author = models.ForeignKey (User, on_delete = models.CASCADE)

    ONE_TO_FIVE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )

    rating     = models.IntegerField (default=0, choices=ONE_TO_FIVE)
    difficulty = models.IntegerField (default=0, choices=ONE_TO_FIVE)
    take_again = models.BooleanField (default = False)

    anonymous  = models.BooleanField (default = False)

    GRADES = (
        ('A' , 'A' ),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B' , 'B' ),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C' , 'C '),
        ('C-', 'C-'),
        ('F' , 'F' ),
        ('NA', 'NA'), 
    )

    grade = models.CharField (max_length=3, choices=GRADES, default='NA', null=True, blank=True)

    review = models.TextField (default="", null=True, blank=True)
    date_posted = models.DateTimeField (default=timezone.now)

    helpful = models.IntegerField (default = 0)

    def __str__(self):
        return 'Rating by {0} for {1}'.format(self.author, self.course)