from django.urls import reverse
from rest_framework.test import APITestCase


class ViewTests(APITestCase):
	def test_string_data(self):
	"""
	Ensures that language is string in Snippet.
	"""
	data = {'language': 'python'}
	response = self.client.get(reverse(data, format=json))
	self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	self.assertEqual(Account.objects.get().language, 'python')
