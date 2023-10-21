from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Photo , Category

# Create your views here.


def gallery(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    context = {'photos' : photos,
               'categories' : categories}
    return render(request , 'photos/gallery.html' , context)


def photoview(request , pk):
    photo = Photo.objects.get(pk = pk)
    return render(request , 'photos/photo.html' , {'photo':photo})

def categoryview(request , pk):
    category = Category.objects.get(pk = pk)
    categories = Category.objects.all()
    photos = Photo.objects.filter(category = category)
    context = {'photos' : photos,
               'categories' : categories}
    
    return render(request , 'photos/gallery.html' , context= context)

@login_required
def addphoto(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(pk = data['category'])
        elif data['category_new'] !='none':
            category , created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        photo = Photo.objects.create(
            category = category,
            description = data['description'],
            image = image
        )
        return redirect('gallery')
    context = {'categories' : categories}
    return render(request , 'photos/add.html' , context)