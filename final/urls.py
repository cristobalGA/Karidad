"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *
from django.contrib.auth.views import *
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio_sesion/$',inicio_sesion,{'template_name': 'inicio_sesion.html'},name='inicio_sesion'),
    url(r'^logout/$',logout_then_login,name='logout'),
    url(r'^registrarse/$',Registrarse.as_view(),name='registrarse_view'), #<--- "Registrarse" es de la clase(form view) que esta en las vistas
    url(r'^$',index_view.as_view(),name='index_view'), #Index_view
    url(r'^educacion/$',educacion,name='educacion_view'),
    url(r'^salud/$',salud,name='salud_view'),
    url(r'^servicio_comunitario/$',servicio_comunitario,name='servicio_comunitario_view'),
    url(r'^todas_categorias/$',todas_categorias,name='todas_categorias_view'),
    url(r'^editar_perfil/$',editar_perfil,name='editar_perfil_view'),
    url(r'^editar_post/$',editar_post,name='editar_post_view'),
    url(r'^mensaje/$',mensaje,name='mensaje_view'), #hasta el final
    url(r'^perfil/$',perfil,name='perfil_view'),
    url(r'^publicar_post/$',publicar_post.as_view(),name='publicar_post_view'),
    #admin dashboard
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
