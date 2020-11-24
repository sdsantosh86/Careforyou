from django.shortcuts import render

def get_view(request):
    
    return render(request, 'password.html')