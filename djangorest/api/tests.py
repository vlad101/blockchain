from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Transaction

class ModelTestCase(TestCase):
	"""This class defines the test suite for the transaction model."""

	def setUp(self):
		"""Define the test client and other test variables."""
		user = User.objects.create(username='nerd')
		self.transaction_sender = 'First1 Last1'
		self.transaction_recipient = 'First2 Last2'
		self.transaction_amount = '999.99'
		self.transaction = Transaction(
										sender=self.transaction_sender,
										recipient=self.transaction_recipient,
										amount=self.transaction_amount,
										owner=user)

	def test_model_can_create_a_transaction(self):
		"""Test the transaction model can create a transaction."""
		old_count = Transaction.objects.count()
		self.transaction.save()
		new_count = Transaction.objects.count()
		self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
	"""Test suite for the api views."""

	def setUp(self):
		"""Define the test client and other test variables."""
		user = User.objects.create(username='nerd')
		# Initialize client and force it to use authentication
		self.client = APIClient()
		self.client.force_authenticate(user=user)
		self.transaction_data = {
									'sender': 'First1 Last1',
									'recipient': 'First2 Last2',
									'amount': '999.99',
									'owner': user.id
								}
		self.response = self.client.post(
							reverse('create'),
							self.transaction_data,
							format='json'
						)

	def test_api_can_create_a_transaction(self):
		"""Test the api has transaction creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

	def test_authorization_is_enforced(self):
		"""Test that the api has user authorization."""
		transaction = Transaction.objects.get()
		response = self.client.get(
								reverse('details', kwargs={'pk': transaction.id}), 
								format='json'
					)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_api_can_get_a_transaction(self):
		"""Test the api can get a given transaction by id."""
		transaction = Transaction.objects.get()
		response = self.client.get(
						reverse('details', kwargs={'pk': transaction.id}), 
						format='json'
					)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, transaction)

	def test_api_can_update_transaction(self):
		"""Test the api can update a given transaction."""
		transaction = Transaction.objects.get()
		change_transaction = {
			'sender': 'First1 Last1',
			'recipient': 'First2 Last2',
			'amount': '999.99'
		}
		response = self.client.put(
						reverse('details', kwargs={'pk': transaction.id}),
						change_transaction,
						format='json'
					)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_api_can_delete_transaction(self):
		"""Test the api can delete a transaction."""
		transaction = Transaction.objects.get()
		response = self.client.delete(
						reverse('details', kwargs={'pk': transaction.id}),
						format='json',
						follow=True
					)
		self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)