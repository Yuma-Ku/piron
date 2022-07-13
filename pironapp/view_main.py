from django.shortcuts import render

def initialize(request):
    # Set initial values here.
    context = {
        'sample_value' : 'xyz456',
    }
    return context
    