from django.shortcuts import render, redirect

from main.forms import ContactForm
from django.http import JsonResponse


def index(request):
    form = ContactForm(request.POST or None)

    if request.is_ajax():
    	if form.is_valid():
    		form.save()
    		data['name'] = form.cleaned_data.get('name')
    		data['status'] = 'ok'
    		return JsonResponse(data)
    context = {'form': form}
    return render(request, 'main/index.html', context)



