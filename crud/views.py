from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import Member
from django.db.models import Q

def index_redirect(request):
    return  redirect('/crud/')
     
def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)
 
def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'], dni=request.POST['dni'], fecha_Nacimiento=request.POST['fecha_Nacimiento'])
    member.save()
    return redirect('/')
 
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)
 
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/crud/')
 
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')
def search(request):
    members = Member.objects.filter(Q(dni=request.GET.get('search')))
    return render(request, 'crud/index.html', {'members': members})
