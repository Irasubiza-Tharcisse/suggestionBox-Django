from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"suggestion_form.html")

        else:
            return render(request, 'account/login.html', {'error': 'Invalid username or password'})

    return render(request, 'account/login.html')

def register_view(request):
        
    return render(request, 'account/register.html')