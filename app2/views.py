from django.shortcuts import render

# Create your views here.
def  a2_first(request):
    d={'a':30, 'b':60, 'c':80}
    return render(request,'a2_first.html',d)

def a2_second(request):
    d={'name':'Ashu'}
    return render(request,'a2_second.html',d)    