
#Django.
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

def hello_word(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')

def sort_numbers(request):
    numbers = sorted([int(number) for number in request.GET['numbers'].split(',')])
    return JsonResponse({'sorted_numbers': numbers})