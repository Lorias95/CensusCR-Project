from django.shortcuts import render, redirect
from census.forms import PeopleForm
from census.models import People
# Create your views here.

def addnew(request):
    if request.method == "POST":
        form = PeopleForm(request.POST)
        if form.is_valid():
            try:
                if request.POST.get('name') and request.POST.get('id_people') and request.POST.get(
                        'place') and request.POST.get('table') and request.POST.get('venc_id'):

                    form.name = request.POST.get('name')
                    form.id_people = request.POST.get('id_people')
                    form.place = request.POST.get('place')
                    form.table = request.POST.get('table')
                    form.venc_id = request.POST.get('venc_id')
                form.save()
                form = PeopleForm()
                return render(request, 'index.html', {'form': form})
                #return redirect('/')
            except:
                pass
    else:
        form = PeopleForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    peoples = People.objects.all()
    return render(request,"show.html",{'peoples':peoples})

def edit(request, id):
    people = People.objects.get(id=id)
    return render(request,'edit.html', {'people':people})

def update(request, id):
    people = People.objects.get(id=id)
    form = PeopleForm(request.POST, instance = people)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'people': people})

def destroy(request, id):
    people = People.objects.get(id=id)
    people.delete()
    return redirect("/")
