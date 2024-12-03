from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from django.contrib.auth import get_user_model
from todos.models import Todo

User = get_user_model()

class TodoEndpointsTestCase(TestCase):
    
    def setUp(self):
        """Set up a test user."""
        # Kullanıcı oluşturuluyor
        self.user = User.objects.create_user(
            username="testuser", 
            email="testuser@example.com",
            password="testpassword"
        )
        
        # Test verisi oluşturuluyor
        self.todo_data = {
            "userId": self.user.id,
            "title": "Test Todo",
            "completed": False
        }

    def test_create_todo(self):
        """Test creating a new Todo."""
        url = reverse('todo-list')  # 'todo-list' endpointi
        response = self.client.post(url, self.todo_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test Todo')

    def test_get_todo(self):
        """Test getting an existing Todo."""
        todo = Todo.objects.create(userId=self.user, title="Test Todo", completed=False)
        url = reverse('todo-detail', args=[todo.id])  # 'todo-detail' endpointi
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], todo.title)
        self.assertEqual(response.data['completed'], todo.completed)

    def test_update_todo(self):
        """Test updating an existing Todo."""
        todo = Todo.objects.create(userId=self.user, title="Old Title", completed=False)
        url = reverse('todo-detail', args=[todo.id])  # 'todo-detail' endpointi
        updated_data = {
            "title": "Updated Title",
            "completed": True,
            "userId": self.user.id
        }
        
        # 'Content-Type' başlığını manuel olarak ekle
        response = self.client.put(url, updated_data, format='json', content_type='application/json')
        todo.refresh_from_db()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(todo.title, "Updated Title")
        self.assertEqual(todo.completed, True)


    def test_delete_todo(self):
        """Test deleting a Todo."""
        todo = Todo.objects.create(userId=self.user, title="Test Todo", completed=False)
        url = reverse('todo-detail', args=[todo.id])  # 'todo-detail' endpointi
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)
