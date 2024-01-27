from django.shortcuts import render,redirect

from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password1 == password:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                print('Email taken')
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email )
                user.save()
                print("User created")
        else:
            print('Passoword not matching..')
        return redirect('/')
    else:
        return render (request,"register.html")