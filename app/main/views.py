from django.shortcuts import render
from .models import Tasks
def index(request):
    data = Tasks.objects.order_by('datetime_start')
    return render(request, 'main/index.html', {'data': data})
