from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from posts.models import Post, Comment
from django.test import TestCase

User = get_user_model()

class PostEndpointsTestCase(TestCase):

    def setUp(self):
        """Set up a test user and post."""
        # Kullanıcı oluşturuluyor
        self.user = User.objects.create_user(
            username="testuser", 
            email="testuser@example.com",
            password="testpassword"
        )
        # Post oluşturma
        self.post_data = {
            "userId": self.user.id,
            "title": "Test Post",
            "body": "This is a test post body."
        }
        
    def test_create_post(self):
        # Yeni post ekleme
        url = reverse('post-list')  # 'post-list' endpointi
        response = self.client.post(url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
    
    def test_get_post(self):
        # Önceden eklenmiş postu alma
        post = Post.objects.create(userId=self.user, title="Test Post", body="This is a test post body.")
        url = reverse('post-detail', args=[post.id])  # 'post-detail' endpointi
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)
    
    def test_update_post(self):
        # Postu oluştur
        post = Post.objects.create(userId=self.user, title="Old Title", body="Old body")
        
        # URL'yi oluştur
        url = reverse('post-detail', args=[post.id])  # 'post-detail' endpointi
        
        # Güncellenmiş veriyi hazırla
        updated_data = {
            "title": "Updated Title",
            "body": "Updated body",
            "userId": self.user.id
        }
        
        # PUT isteği gönder ve JSON formatında veriyi gönder
        response = self.client.put(url, updated_data, content_type='application/json')  # content_type='application/json'
        
        # Veritabanını güncelle
        post.refresh_from_db()
        
        # Yanıtın doğru olup olmadığını kontrol et
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(post.title, "Updated Title")
    
    def test_delete_post(self):
        # Postu silme
        post = Post.objects.create(userId=self.user, title="Test Post", body="This is a test post body.")
        url = reverse('post-detail', args=[post.id])  # 'post-detail' endpointi
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)


class CommentEndpointsTestCase(TestCase):

    def setUp(self):
        """Set up a test user, post, and comment."""
        # Kullanıcı oluşturuluyor
        self.user = User.objects.create_user(
            username="testuser", 
            email="testuser@example.com",
            password="testpassword"
        )        
        self.post = Post.objects.create(userId=self.user, title="Test Post", body="This is a test post body.")
        
        # Comment oluşturma
        self.comment_data = {
            "postId": self.post.id,
            "name": "Test Commenter",
            "email": "test@example.com",
            "body": "This is a test comment."
        }
        

    def test_create_comment(self):
        # Yeni yorum ekleme
        url = reverse('comment-list')  # 'comment-list' endpointi
        response = self.client.post(url, self.comment_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_get_comment(self):
        # Önceden eklenmiş yorumu alma
        comment = Comment.objects.create(postId=self.post, name="Test Commenter", email="test@example.com", body="This is a test comment.")
        url = reverse('comment-detail', args=[comment.id])  # 'comment-detail' endpointi
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], comment.name)
    
    def test_update_comment(self):
        comment = Comment.objects.create(postId=self.post, name="Old Name", email="old@example.com", body="Old comment body.")
        url = reverse('comment-detail', args=[comment.id])  # 'comment-detail' endpointi
        updated_data = {
            "name": "Updated Name",
            "email": "updated@example.com",
            "body": "Updated comment body.",
            "postId": self.post.id
        }
        response = self.client.put(url, updated_data, content_type='application/json')  # content_type='application/json'
        comment.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(comment.name, "Updated Name")
    
    def test_delete_comment(self):
        # Yorumu silme
        comment = Comment.objects.create(postId=self.post, name="Test Commenter", email="test@example.com", body="This is a test comment.")
        url = reverse('comment-detail', args=[comment.id])  # 'comment-detail' endpointi
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
