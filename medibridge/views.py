from django.shortcuts import render, redirect
from registration.models import Doctors,Donors, Users


# Create your views here.
def index(request):
    return render(request, 'medibridge/index.html')

def about_us(request):
    return render(request,'medibridge/about_us.html')

def doctors(request):
    context = {}
    context['doctors'] = Doctors.objects.all()
    return render(request,'medibridge/doctors.html', context)

def donors(request):
    if 'id' in request.session:
        context = {}
        context['donors'] = Donors.objects.all()
        return render(request,'medibridge/donors.html', context)
    else:
        return redirect('/login')

def review(request):
    return render(request,'medibridge/review.html')

def services(request):
    return render(request,'medibridge/services.html')

def book_now(request):
    return render(request,'medibridge/book_now.html')

def blogs(request):
    return render(request,'medibridge/blogs.html')

def logout(request):
    if 'id' in request.session:
        del request.session['id']
        del request.session['email'] 

        if 'role' in request.session:
            del request.session['role']
        elif 'approved' in request.session:
            del request.session['approved']

    return redirect('/')