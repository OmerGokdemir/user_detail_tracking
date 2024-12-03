from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Address, Geo, Company
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse

class CustomUserModelTest(TestCase):
    
    def setUp(self):
        # Geo, Address ve Company nesnelerini oluşturuyoruz
        geo = Geo.objects.create(lat="39.950289", lng="32.7732722")
        address = Address.objects.create(
            street="Çamlıca Mahallesi",
            suite="Apt. 556",
            city="Ankara",
            zipcode="06200",
            geo=geo
        )
        company = Company.objects.create(name="N2Mobil Araç Takip Sistemleri A.Ş")
        
        # Kullanıcıyı oluşturuyoruz
        self.user = get_user_model().objects.create_user(
            email="muslum.turk@n2mobil.com.tr",
            password="securepassword",
            username="muslum.turk",
            name="Müslüm Türk",
            address=address,
            phone="+90 555 555 55 55",
            website="https://www.n2mobil.com.tr",
            company=company
        )

    def test_create_user(self):
        """Geçerli bir kullanıcı oluşturulabiliyor mu?"""
        user = self.user
        self.assertEqual(user.email, "muslum.turk@n2mobil.com.tr")
        self.assertEqual(user.username, "muslum.turk")
        self.assertEqual(user.phone, "+90 555 555 55 55")
        self.assertEqual(user.website, "https://www.n2mobil.com.tr")
        self.assertEqual(user.name, "Müslüm Türk")
        self.assertTrue(user.check_password("securepassword"))

    def test_invalid_email(self):
        """Geçersiz e-posta ile kullanıcı oluşturulamaz."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email="",  # E-posta boş
                password="securepassword",
                username="invalid.user"
            )

    def test_phone_regex_valid(self):
        """Geçerli telefon numarasıyla kullanıcı oluşturulabilir."""
        user = get_user_model().objects.create_user(
            email="valid.phone@n2mobil.com.tr",
            password="securepassword",
            username="valid.phone",
            name="Valid User",
            phone="+90 555 555 55 55"
        )
        self.assertEqual(user.phone, "+90 555 555 55 55")

    def test_phone_regex_invalid(self):
        """Geçersiz telefon numarasıyla kullanıcı oluşturulamaz ve ValidationError alınmalı."""
        invalid_user = get_user_model()(
            email="invalid.phone@n2mobil.com.tr",
            password="securepassword",
            username="invalid.phone",
            name="Invalid User",
            phone="555-555-5555",  # Geçersiz telefon numarası
            website="https://www.n2mobil.com.tr",
            company=self.user.company,
            address=self.user.address
        )
        
        # `full_clean()` metoduyla doğrulamayı tetikleyelim
        with self.assertRaises(ValidationError):
            invalid_user.full_clean()  # Burada ValidationError bekliyoruz

    def test_create_superuser(self):
        """Superuser doğru şekilde oluşturulabilir mi?"""
        superuser = get_user_model().objects.create_superuser(
            email="admin@n2mobil.com.tr",
            password="adminpassword",
            username="adminuser"
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    def test_user_address(self):
        """Kullanıcının adres bilgileri doğru şekilde ilişkilendirilmiş mi?"""
        user = self.user
        self.assertEqual(user.address.street, "Çamlıca Mahallesi")
        self.assertEqual(user.address.city, "Ankara")
        self.assertEqual(user.address.zipcode, "06200")
        self.assertEqual(user.address.geo.lat, "39.950289")
        self.assertEqual(user.address.geo.lng, "32.7732722")

    def test_user_company(self):
        """Kullanıcının şirketi doğru şekilde ilişkilendirilmiş mi?"""
        user = self.user
        self.assertEqual(user.company.name, "N2Mobil Araç Takip Sistemleri A.Ş")


User = get_user_model()



class UserViewSetTests(TestCase):
    def setUp(self):
        # Testlerde kullanılacak örnek kullanıcı oluşturuluyor
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='Test321.'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        url = reverse('users-list')
        data = {
            "name": "John Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "Test321.",
            "address": {
                "street": "123 Elm St",
                "suite": "Apt 4",
                "city": "Anytown",
                "zipcode": "12345",
                "geo": {
                    "lat": 40.7128,
                    "lng": 74.0060
                }
            },
            "company": {
                "name": "Example Corp"
            },
            "phone": "123-456-7890",
            "website": "www.johndoe.com"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['detail'], "User has been created.")

    def test_login_user(self):
        url = reverse('login-list')
        data = {
            "email": "testuser@example.com",
            "password": "Test321."
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def test_change_password(self):
        url = reverse('change-password')
        data = {
            "old_password": "Test321.",
            "new_password": "NewTest123.",
            "confirm_password": "NewTest123."
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], "Password has been changed.")

    def test_get_active_users(self):
        active_user = User.objects.create_user(
            email='activeuser@example.com', password='Test321.'
        )
        active_user.is_active = True
        active_user.save()

        inactive_user = User.objects.create_user(
            email='inactiveuser@example.com', password='Test321.'
        )
        inactive_user.is_active = False
        inactive_user.save()

        url = reverse('users-active-users')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only active users should be returned
        self.assertEqual(response.data[0]['email'], 'activeuser@example.com')