from django.shortcuts import render

def error_403(request,exception):
    return render(request,"403.html")