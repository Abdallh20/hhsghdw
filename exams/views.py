from django.shortcuts import render,redirect
from .models import question
from .forms import questionform
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = questionform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = questionform()
    context = {'form': form}
    return render(request,'index.html',context)