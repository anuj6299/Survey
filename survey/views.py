from django.shortcuts import render, get_object_or_404, HttpResponseRedirect 
from .models import Survey 
from .forms import SurveyForm


def index(request):
    result = Survey.objects.all()

    context = {
        'result' : result,
    }
    form = SurveyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context['form']= form
    return render(request, "index.html", context) 


def result(request):
    result = Survey.objects.all()
    context = {
        'result' : result,
    }
    return render(request, "result.html", context)     

def update(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Survey, id = id) 
  
    # pass the object as instance in form 
    form = SurveyForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/") 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "update_view.html", context) 

def delete(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Survey, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return HttpResponseRedirect("/") 
  
    return render(request, "delete.html", context) 