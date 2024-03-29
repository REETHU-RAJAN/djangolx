"""
URL configuration for olxapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from olxvehicle.views import OlxDeleteView,OlxDetailView,OlxListView,OlxCreateView,OlxUpdateView,SignInView,SignUpView,signout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('olx/add',OlxCreateView.as_view(),name="olx-add"),
    path('olx/all',OlxListView.as_view(),name="olx-list"),
    path('olx/<int:pk>',OlxDetailView.as_view(),name="olx-detail"),
    path('olx/<int:pk>/remove/',OlxDeleteView.as_view(),name="olx-remove"),
    path('olx/<int:pk>/change/',OlxUpdateView.as_view(),name='olx-change'),
    path('register',SignUpView.as_view(),name='register'),
    path('signin',SignInView.as_view(),name='signin'),
    path('signout',signout_view,name='signout'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
