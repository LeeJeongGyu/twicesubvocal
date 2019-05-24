from django.shortcuts import render

from .models import Twice

def twice(request):
    members = Twice.objects.filter(nationality='일본')

    return render(request, 'home.html',{'japanes' : members})


def twice2(request):
    members = Twice.objects.filter(position__icontains='서브보컬')
    return render(request, 'home2.html', {'sub_vocals' : members})