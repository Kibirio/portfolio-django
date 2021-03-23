from django.db.models import Q
from django.shortcuts import render, redirect

from main.forms import ContactForm
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

from main.models import Contact, User


def index(request):
    form = ContactForm(request.POST or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = User(user=ip)
    print(ip)
    result = User.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print('user exits')
    elif len(result) > 1:
        print('users exists')
    else:
        u.save()
        print('This is a new user')
    count = User.objects.all().count()
    print('total visitors', count)

    context = {'form': form, 'count': count}
    return render(request, 'main/index.html', context)


