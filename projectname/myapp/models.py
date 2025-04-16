from django.db import models
from django import forms

# Create your models here.
todo_type = (
    (0, "easy"),
    (1, "medium"),
    (2, "hard")
)

class ToDo(models.Model):
    author= models.CharField(max_length=10, default="unicode")
    title=models.CharField(max_length=15)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField() 
    todo_type=models.IntegerField(choices= todo_type)
    
    def __str__(self):
        return f"{self.author}'s {self.title}"

class ToDoForm(forms.ModelForm):
    class Meta():
        model= ToDo
        fields= "__all__"
        widgets= {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        

