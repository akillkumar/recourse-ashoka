from django import forms
from django.db import models
from datetime import datetime

from  .models import Rating

class RatingsForm (forms.ModelForm):
    
    class Meta:
        model = Rating
        fields = ['rating', 'difficulty', 'take_again', 'grade', 'review', 'anonymous']
        widgets = {
            'rating': forms.Select(
				attrs={
					    'class': 'form-control col-xs-2'
					}
            ),

            'difficulty': forms.Select(
				attrs={
					    'class': 'form-control col-xs-2'
					}
            ),

            'grade': forms.Select(
				attrs={
					    'class': 'form-control col-xs-2'
					}
            ),
            
            
            'take_again': forms.CheckboxInput(
                    attrs={
                            'class': 'form-check',
                            'type' : 'checkbox'
                        }
                ),

            'review': forms.Textarea(
				attrs={
                        'class': 'form-control col-xs-2',
                        'placeholder': 'Write a review ... ',
                        'rows' : '5',     
                        'cols' : '30',
					}
            ),
            'anonymous': forms.CheckboxInput(
				attrs={
					    'class': 'form-check '
					}
            )
            }