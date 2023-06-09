from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.


def inquiry(request):
    
    if request.method == 'POST':
        car_id = request.POST.get('car_id',False)
        car_title = request.POST.get('car_title',False)
        user_id = request.POST.get('user_id',False)
        first_name = request.POST.get('first_name',False)
        last_name = request.POST.get('last_name',False)
        customer_need = request.POST.get('customer_need',False)
        city = request.POST.get('city',False)
        state = request.POST.get('state',False)
        email = request.POST.get('email',False)
        phone = request.POST.get('phone',False)
        message = request.POST.get('message',False)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'We alredy recieved you quiry regarding this car, Please wait until we get back to you.')
                return redirect('/cars/'+car_id) 

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
                          last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                "New Car Inquiry",
                "You have new inquiry for the car. " + car_title+ '. Please login to your admin panel for more info.',
                "mnksharma71@gmail.com",
                [admin_email],
                fail_silently=False,
            )

        contact.save()
        messages.success(
            request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)
