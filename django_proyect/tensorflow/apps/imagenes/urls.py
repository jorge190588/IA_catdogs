from django.conf.urls import url
from .views import index, simple_upload


urlpatterns = [
    url(r'^$', index,name='home'),
    url(r'^simple_upload$', simple_upload,name='cargar_imagen'),
]