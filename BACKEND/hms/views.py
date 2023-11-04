from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model
from hms.models import Booking,Room, Rooms_details
from datetime import date, timezone
import datetime, re
from functools import reduce
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



User = get_user_model()


# Create your views here.
def Welcome (request):
    return render(request, 'Welcome.html')

def rooms (request):
    return render(request, 'room_details.html')

def booking (request):
    return render(request, 'Booking.html')

def blogs (request):
    return render(request, 'blogs_reviews.html')

def offers (request):
    return render(request, 'offers.html')

def gallery (request):
    return render(request, 'gallery.html')


def signup(request):
    if not request.user.is_anonymous:
        return redirect("/")
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if not name or not email or not password:
            messages.error(request, 'Please fill out all the fields.')
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already signed up. Head to the login page.')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=name).exists():
            messages.error(request, 'Username already taken. Please try something else.')
            return render(request, 'signup.html')
        
        user = User.objects.create_user(username=name, email=email, first_name=name, password=password)
        messages.success(request, f'Your account is created, {name}. Head to the login page!')
        return redirect('signin')  
    
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)

    return redirect('/')  # Change 'Welcome' to the appropriate view name or URL pattern

def signin(request):
    if not request.user.is_anonymous:
        return redirect('/booking') 

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, f'Welcome back, {username}!')
            return redirect('/booking')
        else:
            messages.error(request, 'Wrong username or password')
    return render(request, 'signin.html')


def cleaning_manager(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        try:
            room = Room.objects.get(room_number=room_number)
            if room.current_status == 'Checked Out':
                room.current_status = 'Checked Out & Clean'
                room.save()
        except Room.DoesNotExist:
            pass  # Handle the case where the room does not exist if necessary
    rooms = Room.objects.all()
    return render(request, 'cleaningmanager.html', {'rooms': rooms})

def book_room(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        try:
            room = Room.objects.get(room_number=room_number)
            if room.current_status == 'Checked Out & Clean':
                room.username = request.user.username
                room.current_status = 'Checked Out'
                room.save()
                return redirect('/booking')
        except Room.DoesNotExist:
            pass  # Handle the case where the room does not exist if necessary
    rooms = Room.objects.all()
    return render(request, 'receptionmanager.html', {'rooms': rooms})

def checkout_room(request):
    if request.method == 'POST':
        room_number = request.POST.get('room_number')
        try:
            room = Room.objects.get(room_number=room_number)
            if room.current_status == 'Checked In':
                room.current_status = 'Checked Out'
                room.save()
        except Room.DoesNotExist:
            pass  # Handle the case where the room does not exist if necessary
    rooms = Room.objects.all()
    return render(request, 'receptionmanager.html', {'rooms': rooms})

def reception_manager(request):
    rooms = Room.objects.all()
    return render(request, 'receptionmanager.html', {'rooms': rooms})

def room_info(request):
    rooms = Room.objects.filter(current_status='Checked Out & Clean')

    if not rooms:
        no_data_message = "No rooms are currently checked out."
    else:
        no_data_message = 'Hotel Is Full'

    return render(request, 'receptionmanager.html', {'rooms': rooms, 'no_data_message': no_data_message})


def staff_manager(request):
    return render(request,'staff_manager.html')
def booking_confirm(request):
    return render(request,'booking_confirm.html')
        # room_no =
def booking_verification (request):

    if request.method=='POST':
        checkin=request.POST.get('checkin')
        checkout=request.POST.get('checkout')
        Rooms=request.POST.get('Rooms')
        guest_count=int(request.POST.get('guestCount'))
        username=request.user.username
        
    

        date1 = date(int(checkin[0:4]), int(checkin[5:7]), int(checkin[8:]))
        date2 = date(int(checkout[0:4]), int(checkout[5:7]), int(checkout[8:]))
        couponcode=request.POST.get('Offers')

        roomprice=calculatedPrice(Rooms,couponcode)
        total_amount=(date2 - date1).days * guest_count * roomprice

        booking =Booking(
            checkin=date1,
            checkout=date2,
            room_type=Rooms,
            guest_count=guest_count,
            username=username,
            coupon=couponcode,
            total_price=total_amount
        )
        booking.save()
        dic={'Checkin':checkin, 'Checkout':checkout, 'RoomType':Rooms, 'Guest_count':guest_count, 'Username':username, 'Coupon Code' :couponcode,'Totalprice':total_amount}
        return render(request, 'booking_verification.html', dic)
    
    return render(request, 'booking_verification.html')

def calculatedPrice(room,coupon):
    # Define a dictionary mapping div classes to room prices
    room_prices = {
'Superior King Bed Garden': 8140 ,
'Superior Twin Bed Garden':8140,
'Superior King Bed Pool':10187,
'Deluxe':11187,
'Executive Suite':34187,
'Luxury Suite':36846,
'Premium Suite':48187    }
    coupon_codes = {
    'BEACH2023':25,
    'ROMANCE2023':25,
    'FAMILYADVENT':25,
    'WINTER2023':25,
    'GOLFPARADISE':28,
    'SPARELAX':25,
    'FOODIE2023':18,
    'SKI2023':25,
    'BUSINESSPLUS':35,
    'TROPICS2023':25,
    'SUMMER2023':15,
    'FAMILYFUN':35
}   
    price=room_prices[room]
    if room in room_prices and coupon in coupon_codes:
        price = room_prices[room] - (room_prices[room]*coupon_codes[coupon]/100)

    return price