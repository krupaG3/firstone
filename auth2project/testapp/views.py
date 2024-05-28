from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .import forms
from django.http import HttpResponseRedirect
# Create your views here.

def Home_View(request):
    return render(request,'testapp/home.html')

@login_required
def Java_View(request):
    return render(request,'testapp/java.html')

def Signup_View(request):
    if request.method == 'POST':
        form = forms.Signup_Form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create a new user object from the form but don't save to the database yet
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user to the database
            return HttpResponseRedirect('/accounts/login')
    else:
        form = forms.Signup_Form()
    return render(request, 'testapp/signup.html', {'form': form})