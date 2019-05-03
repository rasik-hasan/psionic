from django.shortcuts import render
from .models import Userdata
from django.contrib import messages

# Create your views here.


def index(request):

    if request.method == "POST":
        name = request.POST['name']
        pnumber = request.POST['pnumber']
        email = request.POST['email']
        address = request.POST['address']
        dob = request.POST['dob']

        entry = Userdata(name=name, pnumber=pnumber,
                         email=email, address=address, dob=dob)

        entry.save()

        entrydata = Userdata.objects.all()

        context = {
            'entrydata': entrydata,
        }

        return render(request, 'pages/index.html', context)

    else:
        entrydata = Userdata.objects.all()

        context = {
            'entrydata': entrydata,
        }

        return render(request, 'pages/index.html', context)
