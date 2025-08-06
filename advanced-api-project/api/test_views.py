from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Author, Book
from django.urls import reverse
import datetime

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass123')

        # Create an author
        self.author = Author.objects.create(name="Author One")

        # Create books
        self.book1 = Book.objects.create(
            title="Book A", publication_year=2020, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Book B", publication_year=2022, author=self.author
        )

        self.book_list_url = reverse('book-list')  # e.g., /books/
        self.book_detail_url = lambda pk: reverse('book-detail', args=[pk])  # e.g., /books/1/

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        response = self.client.get(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.put(self.book_detail_url(self.book1.pk), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.book_list_url}?title=Book A")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book A")

    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.data[0]['publication_year'], 2020)

    def test_search_books_by_title(self):
        response = self.client.get(f"{self.book_list_url}?search=Book A")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book A")

    def test_unauthenticated_user_cannot_create_book(self):
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2025,
            "author": self.author.id
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)








'''Task Description:
In this task within your advanced_api_project, you will create unit tests for the API endpoints you’ve developed, focusing on testing their functionality, response data integrity, and status code accuracy. This ensures that your API behaves as expected under various conditions and inputs. The tests should be written in the /api/test_views.py file

Step 1: Understand What to Test
Identify Key Areas:
Focus on testing CRUD operations for the Book model endpoints.
Test the filtering, searching, and ordering functionalities to verify they work as intended.
Ensure that permissions and authentication mechanisms are correctly enforcing access controls.
Step 2: Set Up Testing Environment
Configure Test Settings:
Use Django’s built-in test framework which is based on Python’s unittest module.
Configure a separate test database to avoid impacting your production or development data.
Step 3: Write Test Cases
Develop Test Scenarios:
Write tests that simulate API requests and check for correct status codes and response data. This includes:
Creating a Book and ensuring the data is correctly saved and returned.
Updating a Book and verifying the changes are reflected.
Deleting a Book and ensuring it is removed from the database.
Testing each endpoint with appropriate authentication and permission scenarios to ensure security controls are effective.
Step 4: Run and Review Tests
Execute Tests:
Run your test suite using Django’s manage.py command: bash python manage.py test api
Review the outputs and fix any issues or bugs identified by the tests.
Step 5: Document Your Testing Approach
Testing Documentation:
Document your testing strategy and individual test cases.
Provide guidelines on how to run the tests and interpret test results.'''