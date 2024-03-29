"""
URL configuration for book_application project.

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
from django.urls import path,include
from myapp.views import BookAddView,BookListView,BookDetailView,BookDeleteView,BookUpdateView,RegistrationFormView,SignInView,SignOutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/add',BookAddView.as_view(),name='add_book'),
    path('books/all',BookListView.as_view(),name='all_books'),
    path('books/<int:pk>/',BookDetailView.as_view(),name='detail_book'),
    path('books/<int:pk>/remove',BookDeleteView.as_view(),name='delete_book'),
    path('books/<int:pk>/change',BookUpdateView.as_view(),name='update_book'),
    path('signup/',RegistrationFormView.as_view(),name='signup'),
    path('',SignInView.as_view(),name='signin'),
    path('signout/',SignOutView.as_view(),name='signout'),
    path('api/',include('api.urls'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
