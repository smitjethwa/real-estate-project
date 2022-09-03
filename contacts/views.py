import re
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from accounts.message_choice import message_dict as msg
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing'] 
        name = request.POST['name'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        message = request.POST['message'] 
        user_id = request.POST['user_id'] 
        realtor_email = request.POST['realtor_email'] 

        # check the user has inquery already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,msg['inqueryalreadysubmitted'])
                return redirect(f"/listings/{listing_id}")
                

        contact = Contact(
            listing = listing,
            listing_id = listing_id,
            name = name,
            email = email,
            phone = phone,
            message = message,
            user_id = user_id 
        )
        contact.save()

        # send email
        # send_mail(
        #     'Property Listing Inquiry',
        #     'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info.',
        #     'smitjethwa20@gmail.com',
        #     [realtor_email, 'smitjethwa20@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, msg['enquirysubmitted'])
        return redirect(f"/listings/{listing_id}")
 
