# from django import forms  # Import the forms module if not already imported
# from django.test import TestCase
# from django.urls import reverse
# from hms.views import Welcome, signin, signup, rooms, booking, blogs, offers, gallery, booking_verification, booking_confirm, room_info, staff_manager, cleaning_manager, checkout_room, reception_manager, book_room

# class UrlsTest(TestCase):
#     def test_open_all_urls(self):
#         # Define a list of URL names and corresponding views
#         url_views = [
#             ('Welcome', Welcome),
#             ('signin', signin),
#             ('signup', signup),
#             ('rooms', rooms),
#             ('booking', booking),
#             ('blogs', blogs),
#             ('offers', offers),
#             ('gallery', gallery),
#             ('booking_verification', booking_verification),
#             ('booking_confirm', booking_confirm),
#             ('room_info', room_info),
#             ('staff_manager', staff_manager),
#             ('cleaning_manager', cleaning_manager),
#             ('checkout_room', checkout_room),
#             ('reception_manager', reception_manager),
#             ('book_room', book_room),
#         ]

#         # Iterate through the URLs and simulate form submissions
#         for url_name, view in url_views:
#             url = reverse(url_name)
#             response = self.client.get(url)
#             self.assertEqual(response.status_code, 200, f"Failed to open URL: {url}")

#             # If there's a button to click (e.g., a form submit), simulate the action
#             if hasattr(view, 'form_class') and issubclass(view.form_class, forms.Form):
#                 form_data = {}  # Provide form data if needed
#                 response = self.client.post(url, data=form_data)
#                 self.assertEqual(response.status_code, 200, f"Failed to submit form on URL: {url}")

#                 # Additional checks based on your application requirements
#                 # For example, check for specific content in the response
#                 self.assertContains(response, "Success Message", status_code=200, msg_prefix=f"Form submission failed on URL: {url}")
