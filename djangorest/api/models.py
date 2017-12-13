from django.db import models



class Transaction(models.Model):
	"""This class represents the transaction model."""
	sender = models.CharField(max_length=255, blank=False, unique=False)
	recipient = models.CharField(max_length=255, blank=False, unique=False)
	amount = models.DecimalField(max_digits=8, decimal_places=2)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "Transaction{{sender={}, recipient={}, amount={}}}".format(self.sender, 
																			self.recipient,
																			self.amount)