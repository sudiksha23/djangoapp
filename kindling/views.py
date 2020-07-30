from django.shortcuts import render, HttpResponse, redirect
from kindling.models import EntrySignup
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from kindling.forms import EntrySignupForm
from django.core.files import File

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
 
def redirect_view(request):
    response = redirect('/login/')
    return response

def entrylogin(request):
    
    if request.method == 'POST':
        try:
            uname = request.POST["uname"]
            psw = request.POST["psw"]
            for custom_users in EntrySignup.objects.all():
                if str(custom_users.uname) == uname:
                    login_obj = custom_users
                    break
                else:
                    login_obj = None

            if login_obj is not None:
                if str(login_obj.psw) == psw:
                    request.session['session'] = uname
                    return redirect('/login')
                    #return render(request, 'login.html', {'display' : data})
                else:
                    return redirect('/')
            else:
                return redirect('/')
        except:
            return HttpResponse("exception... !!")

def ourusers(request):
    data=EntrySignup.objects.all()
    return render(request, 'login.html', {'display' : data})

def entrysignup(request):
    if request.method == 'POST' or request.FILES == 'file':
        #fname=request.POST["fname"]
        form = EntrySignupForm(request.POST, request.FILES) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('/')
            
    else: 
        form = EntrySignupForm() 
    return render(request, 'kindling/index.html',{'form':form}) 

def searchin(request):
    return render(request, 'searchin.html')

def searchtable1(request):
    
    if request.method == 'POST':
        u = request.POST["u"]
    s=EntrySignup.objects.filter(fname=u)
    return render(request, 'searchin.html', {'set' : s})

def searchtable2(request):
    if request.method == 'POST':
        c = request.POST["c"]
    s=EntrySignup.objects.filter(city=c)
    return render(request, 'searchin.html', {'set1' : s})


def searchtable3(request):
    if request.method == 'POST':
        g = request.POST["g"]
    s=EntrySignup.objects.filter(gender=g)
    return render(request, 'searchin.html', {'set2' : s})

def searchtable4(request):
    if request.method == 'POST':
        m = request.POST["m"]
    s=EntrySignup.objects.filter(marital_status=m)
    return render(request, 'searchin.html', {'set3' : s})