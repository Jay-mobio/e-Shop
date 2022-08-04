from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    def get(self, request):
        return render(request,'authentication/home.html')