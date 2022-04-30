from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .services import predict
from .services import train_model
from django.templatetags.static import static
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import uuid
from django.core.files.base import ContentFile
import base64
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html');

def predict_image(request):
    if request.method == 'POST' and request.POST['digitImage']:
        data = request.POST['digitImage']
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]

        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        file_name = str(uuid.uuid4())[:12] + '.' +ext
        fs = FileSystemStorage()
        filename = fs.save(file_name, data)

        img_path = os.path.join(settings.MEDIA_ROOT, filename)
        result = predict(img_path)

        context = { 'result' : str(result) }
        return JsonResponse({'result': str(result)})
    return render(request, 'index.html')

def train(request):
    train_model()
    return HttpResponseRedirect(reverse('digits:index'))

def predict_uploaded_image(request):
    context = {}
    if request.method == 'POST' and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        img_path = os.path.join(settings.MEDIA_ROOT, filename)
        result = predict(img_path)
        messages.add_message(request, messages.INFO, str(result), extra_tags='result')
        messages.add_message(request, messages.SUCCESS, uploaded_file_url)
        return HttpResponseRedirect(reverse('digits:index'))

    return render(request, 'index.html', context)

