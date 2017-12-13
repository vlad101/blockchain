from rest_framework import generics
from .serializers import TransactionSerializer
from .models import Transaction

class CreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of the rest api."""
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer

	def perform_create(self, serializer):
		"""Save the post data when creating a new transaction."""
		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the HTTP GET, PUT and DELETE requests."""
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer