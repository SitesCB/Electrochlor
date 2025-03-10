from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')), # news/...


]

if settings.DEBUG: # DEBUG укзаывает на то, что сайт находится в разработке
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

