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
					'class': 'form-control-sm form-group '
					}
            ),

            'difficulty': forms.Select(
				attrs={
					'class': 'form-control-sm form-group '
					}
            ),

            'grade': forms.Select(
				attrs={
					'class': 'form-control-sm form-group '
					}
            ),
            
            
        'take_again': forms.CheckboxInput(
				attrs={
					'class': 'form-check-input form-group ',
                    'type' : 'checkbox'
					}
            ),

            'review': forms.Textarea(
				attrs={
					'class': 'form-control-sm form-group',
                    'rows' : '2',     
                    'cols' : '30'
                    
					}
            ),
            'anonymous': forms.CheckboxInput(
				attrs={
					'class': 'form-control-sm form-group '
					}
            )
            }