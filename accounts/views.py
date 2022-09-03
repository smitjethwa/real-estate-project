from email import message
from operator import truediv
import re
from urllib.request import Request
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .message_choice import message_dict as msg
from contacts.models import Contact

# Create your views here.


def username_check(request, username):
    if User.objects.filter(username=username).exists():
        return True
    else:
        return False


def email_check(request, email):
    if User.objects.filter(email=email).exists():
        return True
    else:
        return False

def register(request):
    if request.method == "POST":
        # get_form_values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        # phone = request.POST['phone']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # password match
        if password == password2:
            if username_check(request, username):
                messages.error(request, msg['usernametaken'])
                return redirect('register')
            else:
                if email_check(request, email):
                    messages.error(request, msg['emailtaken'])
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        # phone=phone
                    )

                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, msg['logginsuccess'])
                    # return redirect('index')

                    # manual login after register
                    user.save()
                    messages.success(request, msg['registeredmsg'])  
                    return redirect('login')

        else:
            messages.error(request, msg['passwordnotmatched'])
            return redirect('register')

        # messages.error(request,'Testing')
        # return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request,user)
            messages.success(request,msg['logginsuccess'])
            return redirect('dashboard')
        else:
            messages.error(request,msg['invalidcreds'])
            return redirect('login')
    else:

        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, msg['logoutmsg'])
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts' : user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)
