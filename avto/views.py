from django.shortcuts import render
from .models import Avto
 
def avto(request):
	cars = Avto.objects.all()
	return render(request, 'contents/info.html', {"cars": cars})
