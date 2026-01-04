from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Resolution

def index(request):
    return render(request, "main/index.html")

@login_required(login_url='login')
def home(request):
    reso = Resolution.objects.filter(user=request.user)
    context = {'reso':reso}
    return render(request, "main/home.html", context)

@login_required(login_url='login')
def new(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        r = Resolution(user=user, title=title, description=description, start_date=start_date, end_date=end_date)
        
        try:
            r.save()
            messages.success(request, f"You are set to achieve '{title}'!")
            return redirect('home')
        except Exception as e:
            messages.error(request, e)
            
        
        
    return render(request, "main/new.html")

def edit(request, pk):
    pk = Resolution.objects.get(id=pk)
    context = {'pk':pk}
    return render(request, "main/edit.html", context)

def delete(request, pk):
    pk = Resolution.objects.get(id=pk)
    pk.delete()
    return redirect('home')
    # pass
    # return render(request, "main/edit.html")

