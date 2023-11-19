# hms/tests/test_urls.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hms.views import Welcome, signin, signup, rooms, booking, blogs, offers, gallery, booking_verification, booking_confirm, room_info, staff_manager, cleaning_manager, checkout_room, reception_manager, book_room
from .views import user_logout

class UrlsTestCase(SimpleTestCase):

    def test_welcome_url_resolves(self):
        url = reverse('Welcome')
        self.assertEqual(resolve(url).func, Welcome)

    def test_signin_url_resolves(self):
        url = reverse('signin')
        self.assertEqual(resolve(url).func, signin)

    def test_signup_url_resolves(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_rooms_url_resolves(self):
        url = reverse('rooms')
        self.assertEqual(resolve(url).func, rooms)

    def test_booking_url_resolves(self):
        url = reverse('booking')
        self.assertEqual(resolve(url).func, booking)

    def test_blogs_url_resolves(self):
        url = reverse('blogs')
        self.assertEqual(resolve(url).func, blogs)

    def test_offers_url_resolves(self):
        url = reverse('offers')
        self.assertEqual(resolve(url).func, offers)

    def test_gallery_url_resolves(self):
        url = reverse('gallery')
        self.assertEqual(resolve(url).func, gallery)

    def test_booking_verification_url_resolves(self):
        url = reverse('booking_verification')
        self.assertEqual(resolve(url).func, booking_verification)

    def test_booking_confirm_url_resolves(self):
        url = reverse('booking_confirm')
        self.assertEqual(resolve(url).func, booking_confirm)

    def test_room_info_url_resolves(self):
        url = reverse('room_info')
        self.assertEqual(resolve(url).func, room_info)

    def test_staff_manager_url_resolves(self):
        url = reverse('staff_manager')
        self.assertEqual(resolve(url).func, staff_manager)

    def test_cleaning_manager_url_resolves(self):
        url = reverse('cleaning_manager')
        self.assertEqual(resolve(url).func, cleaning_manager)

    def test_checkout_room_url_resolves(self):
        url = reverse('checkout_room')
        self.assertEqual(resolve(url).func, checkout_room)

    def test_reception_manager_url_resolves(self):
        url = reverse('reception_manager')
        self.assertEqual(resolve(url).func, reception_manager)

    def test_book_room_url_resolves(self):
        url = reverse('book_room')
        self.assertEqual(resolve(url).func, book_room)

