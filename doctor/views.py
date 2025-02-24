from django.shortcuts import render
from registration.models import Doctors

# Create your views here.
def d_home(request):
    if request.method == 'GET':
        context = {}
        context['doc'] = Doctors.objects.filter(id = request.session['id']).first()
        return render(request, 'doctor/d_home.html', context)