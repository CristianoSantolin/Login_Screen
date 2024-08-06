from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login 




def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        return render(request, 'register.html', {'user_form': user_form})
    
    else:
        user_form = UserCreationForm()
        return render(request, 'register.html', {'user_form': user_form})
    

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    errors = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('register')  
            else:
                errors = form.non_field_errors()
        else:
            errors = form.non_field_errors()
    
    return render(request, 'login.html', {'form': form, 'errors': errors})
