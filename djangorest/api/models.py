from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

import datetime as date
import hashlib as hasher

class Transaction(models.Model):
	"""This class represents the transaction model."""
	sender = models.CharField(max_length=255, blank=False, unique=False)
	recipient = models.CharField(max_length=255, blank=False, unique=False)
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	owner = models.ForeignKey('auth.User', related_name='transactions', on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return a human readable representation of the transaction model instance."""
		return 'Transaction{{sender={}, recipient={}, amount={}, owner={}}}'.format(self.sender, 
																					self.recipient,
																					self.amount,
																					self.owner)

class Block(models.Model):
	"""
	This class represents the block model.
	Block is the container for the new data.
	Each block has a timestamp, an index (optional), hash, 
	previous hash (each block requires information from the previous block) and data.
	Hash ensures integrity throughout the blockchain. 
	"""
	index = models.IntegerField(blank=False, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	data = models.CharField(max_length=255, blank=False, unique=False)
	previous_hash = models.CharField(max_length=255, blank=False, unique=False)
	current_hash = models.CharField(max_length=255, blank=False, unique=False)
	date_modified = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		"""
		Block's hash is a cryptographic hash of the block's index, 
		timestamp, data, hash, and the hash of the previous block.
		"""
		sha = hasher.sha256()
		sha.update((str(self.index) + 
						str(self.timestamp) + 
						str(self.data) +
						str(self.previous_hash)).encode('utf-8'))
		self.current_hash = sha.hexdigest()
		super(Block, self).save(*args, **kwargs)

	def __str__(self):
		"""Return a human readable representation of the block model instance."""
		return 'Block {{index={}, timestamp={}, data={}, previous_hash={}, current_hash={}}}'.format(str(self.index), 
																							str(self.timestamp), 
																							str(self.data), 
																							str(self.previous_hash), 
																							str(self.current_hash))

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)