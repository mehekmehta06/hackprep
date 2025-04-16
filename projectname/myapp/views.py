from django.shortcuts import render
from .models import ToDo, ToDoForm

def todo_create(request):
    context={'form': ToDoForm()}
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
    context['data']= ToDo.objects.order_by('todo_type')
    return render(request, 'base.html', context)


        

# Create your views here.
