from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def Home(request):
    return render(request, "drive/drive.html", context={})
    # return HttpResponse("Hello")
