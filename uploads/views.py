from django.shortcuts import render

def base(request):
    return render(request, 'mobile_uploads/base.html')