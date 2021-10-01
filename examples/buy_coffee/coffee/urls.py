from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('coffee', views.coffee_view, name='first_view'),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)