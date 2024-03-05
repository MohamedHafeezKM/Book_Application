from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import BookAddModelForm,RegisterationForm,SignInForm
from myapp.models import Books
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

# Create your views here.
#building decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,'Invalid session,Sign In')
            return redirect('signin')
        else:
            return fn(request,*args,**kwargs)
    return wrapper



@method_decorator(signin_required,name='dispatch')
class BookAddView(View):
    def get(self,request,*args,**kwargs):
        form=BookAddModelForm()
        return render(request,'add_book.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=BookAddModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            # Books.objects.create(**form.cleaned_data)
            form.save()
            messages.success(request,'The Book has been added successfully')


            return redirect('all_books')

        else: 
            messages.error(request,'Failed to add book')
            return render(request,'add_book.html',{'form':form})

@method_decorator(signin_required,name='dispatch')
class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        all_catogarys=Books.objects.all().values_list('catogary',flat=True).distinct()
        if 'catogary' in request.GET:
            catogary=request.GET.get('catogary')
            qs=qs.filter(catogary__iexact=catogary)
        return render(request,'all_books.html',{'data':qs,'all_catogarys':all_catogarys})
    
    def post(self,request,*args,**kwargs):
        name=request.POST.get('box')
        qs=Books.objects.filter(name__icontains=name)
        lst=[i for i in qs]
        if lst==[]:
            messages.error(request,'Book not found')
            return render(request,'all_books.html',{'data':qs})
        else:
            messages.success(request,'Books found')
            return render(request,'all_books.html',{'data':qs})
        
@method_decorator(signin_required,name='dispatch')
class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Books.objects.get(id=id)
        return render(request,'details_book.html',{'data':qs})
    
@method_decorator(signin_required,name='dispatch')
class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Books.objects.get(id=id).delete()
        messages.success(request,'This book has been deleted')
        return redirect('all_books')
    
@method_decorator(signin_required,name='dispatch')
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Books.objects.get(id=id)
        form=BookAddModelForm(instance=qs)
        return render(request,'update_books.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Books.objects.get(id=id)
        form=BookAddModelForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'The book had been updated')
            return redirect('detail_book',pk=id)
        else:
            messages.error(request,'Failed to update the book')
            return render(request,'update_books.html',{'form':form})

class RegistrationFormView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterationForm()
        return render(request,'signup.html',{'form':form})
     
    def post(self,request,*args,**kwargs):
        form=RegisterationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'Account created')
            return render(request,'signup.html',{'form':form})
        
        else:
            messages.error(request,'Failed to create an account')
            return render(request,'signup.html',{'form':form})
        
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=SignInForm()
        return render(request,'signin.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get('username')
            pass_word=form.cleaned_data.get('password')
            user_obj=authenticate(request,username=user_name,password=pass_word)
            if user_obj:
                login(request,user_obj)
                messages.success(request,'Succesfully logged in')
                return redirect('all_books')
        messages.error(request,'Wrong credentials')
        return render(request,'signin.html',{'form':form})

@method_decorator(signin_required,name='dispatch')    
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,'Successfully logged out')
        return redirect('signin')




    


