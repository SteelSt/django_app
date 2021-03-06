from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, blog_id): # For example /15 should display a message 'placeholder to display blog 15'.
    response = "placeholder to display blog %s"%(blog_id), 
    return HttpResponse(response)

def edit(request, blog_id): #display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
    response = "placeholder to edit blog %s"%(blog_id), 
    return HttpResponse(response)

def destroy(response, blog_id):
    return redirect('/')