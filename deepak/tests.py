from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import BloodRequest


class BloodRequestPageTests(TestCase):
    def test_apply_page_displays_blood_request_form(self):
        response = self.client.get(reverse('apply'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Blood group needed')
        self.assertContains(response, 'Submit Blood Request')

    def test_valid_request_is_saved_and_confirmation_is_shown(self):
        response = self.client.post(reverse('apply'), {
            'full_name': 'Test Patient',
            'phone': '5551234567',
            'email': 'patient@example.com',
            'blood_group': 'O+',
            'units': '2',
            'hospital': 'Community Hospital',
            'needed_date': '2026-10-10',
            'message': '',
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(BloodRequest.objects.count(), 1)
        request = BloodRequest.objects.get()
        self.assertEqual(request.full_name, 'Test Patient')
        self.assertEqual(request.blood_group, 'O+')
        self.assertEqual(request.units, 2)
        self.assertContains(response, 'Your blood request has been saved.')

    def test_invalid_request_shows_validation_errors(self):
        response = self.client.post(reverse('apply'), {
            'full_name': '',
            'phone': '',
            'blood_group': '',
            'units': '0',
            'hospital': '',
            'needed_date': '',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        self.assertEqual(BloodRequest.objects.count(), 0)


class BloodStockPageTests(TestCase):
    def test_stock_page_displays_all_blood_groups_and_sample_notice(self):
        response = self.client.get(reverse('stock'))

        self.assertEqual(response.status_code, 200)
        for group in ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'):
            self.assertContains(response, group)
        self.assertContains(response, 'Sample data only')
        self.assertContains(response, 'Ready for Urgent Care')
        self.assertEqual(len(response.context['blood_stock']), 8)


class AboutBloodCampPageTests(TestCase):
    def test_about_page_shows_demo_camp_date_and_donor_stories(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bhubaneswar Community Blood Donation Camp')
        self.assertContains(response, '15 November 2026')
        self.assertContains(response, 'Demo event details')
        self.assertContains(response, 'Illustrative stock photos')
        self.assertEqual(response.content.count(b'<img'), 3)


class AdminPageTests(TestCase):
    def test_admin_login_page_loads_without_running_the_server(self):
        response = self.client.get('/admin/login/')

        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard_redirects_to_login_when_signed_out(self):
        response = self.client.get('/admin/')

        self.assertRedirects(response, '/admin/login/?next=/admin/')

    def test_staff_can_view_blood_requests_in_admin(self):
        BloodRequest.objects.create(
            full_name='Admin Test Patient',
            phone='5551234567',
            email='patient@example.com',
            blood_group='O+',
            units=2,
            hospital='Community Hospital',
            needed_date='2026-10-10',
        )
        staff_user = get_user_model().objects.create_superuser(
            username='bloodbankadmin',
            email='admin@example.com',
            password='test-password-123',
        )
        self.client.force_login(staff_user)

        response = self.client.get('/admin/deepak/bloodrequest/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Test Patient')
