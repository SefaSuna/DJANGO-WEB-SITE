"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from article.views import index,about,add,detail,commentt,yazılım,desktop
from data.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('About', about),
    path('add', add),
    path('article/24', desktop),
    path('article/<int:id>', detail,name="detail"),
    path('comment/<int:id>', commentt,name="comment"),
    path('YAZILIM-PROJELERİ', yazılım,name="yazılım"),


    # path('', data_index),
    path('VERİ-BİLİMİ-PROJELERİ', veri,name="veri"),
    path('add-veri', add_veri),
    path('veri/9', machine_desktop),
    path('veri/<int:id>', detail_veri,name="detail_veri"),

    path('comment_veri/<int:id>', commentt_veri,name="comment_veri"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)