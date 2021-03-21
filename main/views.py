from django.shortcuts import render, redirect

from main.forms import ContactForm
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from main.models import Contact


def index(request):
	form = ContactForm(request.POST or None)
	data = {}
	if request.is_ajax():
		if form.is_valid():
			form.save()
			data['name'] = form.cleaned_data.get('name')
			data['status'] = 'ok'
			return JsonResponse(data)
	context = {'form': form}
	return render(request, 'main/index.html', context)


			# def create(request):
			# 	if request.method == 'POST':
			# 		name = request.POST['name']
			# 		email = request.POST['email']
			# 		subject = request.POST['subject']
			# 		message = request.POST['message']
			# 		new_user = Contact(name=name, email=email, subject=subject, message=message)
			# 		messages.success(request, 'Thank for visiting the site')
			# 		new_user.save()
			# 		return redirect('main/index.html')
