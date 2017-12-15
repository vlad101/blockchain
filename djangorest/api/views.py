from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import TransactionSerializer, UserSerializer
from .models import Transaction

class CreateView(generics.ListCreateAPIView):
	"""This class defines the create behavior of the rest api."""
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = (permissions.IsAuthenticated, )

	def list(self, request):
		# The user has to be the owner of the transaction to have that object's permission.
		queryset = Transaction.objects.filter(owner=self.request.user)
		serializer = TransactionSerializer(queryset, many=True)
		return Response(serializer.data)

	def perform_create(self, serializer):
		"""Save the post data when creating a new transaction."""
		serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the HTTP GET, PUT and DELETE requests."""
	queryset = Transaction.objects.all()
	serializer_class = TransactionSerializer
	permission_classes = (permissions.IsAuthenticated, IsOwner, )

	def get(self, request, *args, **kwargs):
		# The user has to be the owner of the transaction to have that object's permission.
		if 'pk' in kwargs:
			queryset = Transaction.objects.filter(pk=kwargs.get('pk')).filter(owner=self.request.user)
			if queryset.count() > 0:
				serializer = TransactionSerializer(queryset, many=True)
				return Response(serializer.data)
			else:
				dict = {}
				dict['detail'] = 'You do not have permission to perform this action.'
				return Response(dict)


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer