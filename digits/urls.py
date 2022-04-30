from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'digits'
urlpatterns = [
    path('', views.index, name='index'),
    path('predict', views.predict_image, name='predict_image'),
    path('train', views.train, name='train'),
    path('predict_uploaded_image', views.predict_uploaded_image, name='predict_uploaded_image'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

