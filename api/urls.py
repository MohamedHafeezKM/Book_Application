from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views


router=DefaultRouter()
router.register('v2/books',views.BookViewSet,basename='books_viewset')

for u in router.urls:
    print('----',u,'--------')


urlpatterns = [
    path('books/',views.BookCreateGetApiView.as_view()),
    path('books/<int:pk>/',views.BookUpdateRemoveDetailApiView.as_view())

    ]+router.urls