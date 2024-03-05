from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import authentication,permissions
from rest_framework.decorators import action
# Create your views here.
from api.serializers import BookSerializer
from myapp.models import Books


class BookCreateGetApiView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        deserializer=BookSerializer(qs,many=True)
        return Response(data=deserializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class BookUpdateRemoveDetailApiView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Books.objects.get(id=id)
        deserializer=BookSerializer(qs)
        return Response(data=deserializer.data)
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        book_object=Books.objects.get(id=id)
        serializer=BookSerializer(data=request.data,instance=book_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        else:
            return Response(data=serializer.errors)
        

    def delete(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Books.objects.get(id=id).delete()
        return Response(data={'message':'This book has been deleted!'})


class BookViewSet(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
        if 'catogary' in request.query_params:
            value=request.query_params.get('catogary')
            qs=qs.filter(catogary__icontains=value)
        deserializer=BookSerializer(qs,many=True)
        return Response(data=deserializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        book_object=Books.objects.get(id=id)
        deserializer=BookSerializer(book_object,many=False)
        return Response(data=deserializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        book_object=Books.objects.get(id=id)
        serializer=BookSerializer(data=request.data,instance=book_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Books.objects.get(id=id).delete()
        return Response({'message':'This book has been deleted'})
    
    @action(methods=['get'],detail=False)
    def all_categories(self,request,*args,**kwargs):
        all_categories=Books.objects.all().values_list('catogary',flat=True).distinct()

        return Response(data=all_categories)


    
        
        

        
