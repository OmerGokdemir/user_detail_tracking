from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from albums.models import Album, Photo
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from PIL import Image

User = get_user_model()

class AlbumPhotoAPITestCase(APITestCase):
    def setUp(self):
        
        # Veritabanını temizliyoruz
        Album.objects.all().delete()
        Photo.objects.all().delete()
        
        # Kullanıcı oluşturuluyor
        self.user = User.objects.create_user(
            username="testuser", 
            email="testuser@example.com",  # 'email' eklenmeli
            password="testpassword"
        )
        
        # Album verisi oluşturuluyor
        self.album = Album.objects.create(userId=self.user, title="My First Album")
        
        # Fotoğraf verisi oluşturuluyor
        self.photo = Photo.objects.create(albumId=self.album, title="Test Photo", url="images/photo1.jpg")

        # URL'leri tanımlıyoruz
        self.album_url = reverse('album-list')  # AlbumViewSet için URL
        self.photo_url = reverse('photo-list')  # PhotoViewSet için URL
    
    def test_album_list(self):
        # Albumler listelendiğinde doğru yanıt dönmesi
        response = self.client.get(self.album_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.album.title)
    
    def test_create_album(self):
        # Yeni bir kullanıcı oluşturuluyor
        new_user = User.objects.create_user(
            username="newuser",
            email="newuser@example.com",
            password="newpassword"
        )
        
        # Yeni albüm oluşturuluyor
        data = {"userId": new_user.id, "title": "New Album"}
        response = self.client.post(self.album_url, data, format='json')
        
        # Yanıtın 400 yerine 201 olduğundan emin olun
        print(response.data)  # Bu satırı hata mesajlarını görmek için ekledik
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Album")


    
    def test_photo_list(self):
        # Fotoğraflar listelendiğinde doğru yanıt dönmesi
        response = self.client.get(self.photo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.photo.title)
    
    def test_create_photo(self):
        # Geçici bir resim dosyası oluşturuluyor
        image_io = io.BytesIO()
        image = Image.new('RGB', (100, 100), color='red')  # 100x100 piksel kırmızı bir resim
        image.save(image_io, 'JPEG')
        image_io.seek(0)

        # Test için geçici olarak oluşturduğumuz resmi SimpleUploadedFile ile dosya haline getiriyoruz
        image_file = SimpleUploadedFile("testphoto.jpg", image_io.read(), content_type="image/jpeg")

        photo_data = {
            "title": "Test Photo",
            "url": image_file,  # Yüklenen geçici resim burada kullanılmalı
            "albumId": self.album.id
        }

        response = self.client.post(self.photo_url, photo_data, format='multipart')  # multipart format dosya yüklemeleri için gerekli

        # Hata mesajını görmek için yazdırıyoruz
        print(response.data)

        # Yanıtın doğru olduğunu kontrol ediyoruz
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Photo.objects.first().title, "Test Photo")


    
    def test_thumbnail_url_in_photo(self):
        # Fotoğrafın thumbnailUrl alanının doğru olduğunun kontrol edilmesi
        response = self.client.get(self.photo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("thumbnailUrl", response.data[0])
        self.assertTrue(response.data[0]["thumbnailUrl"].startswith("http://127.0.0.1:8000/media/"))

    def test_update_album(self):
        # Album güncellenmesi
        data = {"title": "Updated Album Title"}
        response = self.client.patch(reverse('album-detail', args=[self.album.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Album Title")
    
    def test_delete_album(self):
        # Album silinmesi
        response = self.client.delete(reverse('album-detail', args=[self.album.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Album.objects.count(), 0)

    def test_delete_photo(self):
        # Fotoğraf silinmesi
        response = self.client.delete(reverse('photo-detail', args=[self.photo.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Photo.objects.count(), 0)
