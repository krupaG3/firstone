from django.shortcuts import render

# Create your views here.
def Temp_View(request):
    return render(request,'testapp/second.html')