from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book


class AuthorTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_author(self):
        """Test creating an author"""
        data = {'name': 'J.K. Rowling'}
        response = self.client.post('/api/authors/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().name, 'J.K. Rowling')

    def test_list_authors(self):
        """Test listing authors"""
        # Create some authors
        Author.objects.create(name='J.K. Rowling')
        Author.objects.create(name='George R.R. Martin')
        
        response = self.client.get('/api/authors/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'George R.R. Martin')  # Ordered by name
        self.assertEqual(response.data[1]['name'], 'J.K. Rowling')


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create an author for book tests
        self.author = Author.objects.create(name='J.K. Rowling')

    def test_create_book(self):
        """Test creating a book"""
        data = {
            'title': 'Harry Potter and the Philosopher\'s Stone',
            'author': self.author.id,
            'published_year': 1997
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        book = Book.objects.get()
        self.assertEqual(book.title, 'Harry Potter and the Philosopher\'s Stone')
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.published_year, 1997)

    def test_list_books(self):
        """Test listing books"""
        # Create some books
        Book.objects.create(
            title='Harry Potter and the Philosopher\'s Stone',
            author=self.author,
            published_year=1997
        )
        Book.objects.create(
            title='A Game of Thrones',
            author=self.author,
            published_year=1996
        )
        
        response = self.client.get('/api/books/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # Ordered by title
        self.assertEqual(response.data[0]['title'], 'A Game of Thrones')
        self.assertEqual(response.data[1]['title'], 'Harry Potter and the Philosopher\'s Stone')
