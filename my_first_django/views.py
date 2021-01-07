
# Django.
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_word(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')

def sort_numbers(request):
    sorted_numbers = sorted([int(number) for number in request.GET['numbers'].split(',')])
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message' : 'numbers sorted successfully.'
    }
    return JsonResponse(data)

def say_hi(request, name, age):
    """ return a greeting """
    if age < 12:
        message = f'Sorry {name}, you are not allowed here'
    else:
        message = f'Hello {name}, welcome'

    return HttpResponse(message)