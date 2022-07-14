from django.shortcuts import render

def initialize(request):
    # Set initial values here.
    
    url_name = request.resolver_match.url_name
    context = {
        'sample_value' : 'xyz456',
        'url_name': url_name
    }
    return context
    