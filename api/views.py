from django.shortcuts import render, redirect
from registration.models import Donors, Users
from django.contrib import messages

# Create your views here.

def donor(request, id):
    if 'id' in request.session:
        user = Users.objects.get(id=id)
        try:
            donor = Donors.objects.get(email=user.email)
            messages.success(request,"User Already Exist in Donor list. Try another email to add new User")
            return redirect( "/donors")
        except:
            return render(request,"medibridge/donor_add.html")
    return redirect("/login")

def add_donor(request):
    if request.method == "POST":
        email = request.session['email']
        name = request.POST['name']
        contact_no = request.POST['contact_no']
        residence = request.POST['residence']
        blood_group = request.POST['blood_group']

        if not contact_no.isdigit() or len(contact_no) != 10:
            messages.success(request,"Contact number should contain 10 digit only")
            url = "/api/donor/" + str(request.session['id'])
            return redirect(url)

        try:
            donor = Donors(email=email, name=name, contact_no=contact_no, blood_group=blood_group, residence=residence)
            donor.save()
            messages.success(request,"Donor Successfully Added")
        except Exception as e:
            print(e)
        return redirect("/donors")
    
    return render(request,"medibridge/donors.html")


