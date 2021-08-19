from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'a':20,'b':10,'c':90}
    return render(request,'hai.html',d)