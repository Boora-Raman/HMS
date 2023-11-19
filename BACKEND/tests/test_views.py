# hms/tests/test_views.py

from django.test import TestCase, Client
from django.urls import reverse
from hms.views import Welcome, signin, signup, rooms, booking, blogs, offers, gallery, booking_verification, booking_confirm, room_info, staff_manager, cleaning_manager, checkout_room, reception_manager, book_room
from .views import user_logout

class ViewsTestCase(TestCase):

    def test_welcome_view(self):
        response = self.client.get(reverse('Welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/welcome.html')

    def test_signin_view(self):
        response = self.client.get(reverse('signin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/signin.html')

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/signup.html')

    def test_rooms_view(self):
        response = self.client.get(reverse('rooms'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/rooms.html')

    def test_booking_view(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/booking.html')

    def test_blogs_view(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/blogs.html')

    def test_offers_view(self):
        response = self.client.get(reverse('offers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/offers.html')

    def test_gallery_view(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/gallery.html')

    def test_booking_verification_view(self):
        response = self.client.get(reverse('booking_verification'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/booking_verification.html')

    def test_booking_confirm_view(self):
        response = self.client.get(reverse('booking_confirm'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/booking_confirm.html')

    def test_room_info_view(self):
        response = self.client.get(reverse('room_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/room_info.html')

    def test_staff_manager_view(self):
        response = self.client.get(reverse('staff_manager'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/staff_manager.html')

    def test_cleaning_manager_view(self):
        response = self.client.get(reverse('cleaning_manager'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/cleaning_manager.html')

    def test_checkout_room_view(self):
        response = self.client.get(reverse('checkout_room'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/checkout_room.html')

    def test_reception_manager_view(self):
        response = self.client.get(reverse('reception_manager'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/reception_manager.html')

    def test_book_room_view(self):
        response = self.client.get(reverse('book_room'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hms/book_room.html')

