from django.shortcuts import render, HttpResponse
from .models import Item

def get_todo_list(request):
    results = Item.objects.all()
    return render(request, "todo_list.html", {'items': results})