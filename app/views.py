# Create your views here.
from django.shortcuts import render, HttpResponse


def base(request):
   return render(request, "base.html")

def home(request):
   content = {
      'title':  'Home',
      'course': 'MSIT210 - DevOps',
   }
   return render(request, "home.html", content)

def about(request):

   studentInfo = {
      'studentName': 'Leo Niño Y. Legitimas',
      'studentNum': '2025-41000',
   }
   return render(request, "about.html", studentInfo)