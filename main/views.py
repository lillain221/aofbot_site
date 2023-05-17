from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def achievement(request):
    return render(request, 'achievement.html')

def career(request):
    return render(request, 'career.html')

def contact(request):
    return render(request, 'contact.html')
    
def skill(request):
    return render(request, 'skill.html')