from rest_framework.permissions import BasePermission
from .models import Transaction

class IsOwner(BasePermission):
	"""Custom permission class to allow only transaction owners can edit them."""

	def has_object_permission(self, request, view, obj):
		"""Return True if permission is granted to the transaction owner."""
		if isinstance(obj, Transaction):
			return obj.owner == request.user
		return obj.owner == request.user

	def has_permission(self, request, view):
		"""Return True if permission is granted to the transaction owner."""
		"""Check permission here since has_object_permission() is not called."""
		#print(view.get_queryset().count())
		#print(view.get_queryset()[0])
		#print(request.user)
		#if view.get_queryset().count() > 0:
		#	obj = view.get_queryset()[0]
		#	if isinstance(obj, Transaction):
		#		return obj.owner == request.user
		#	return obj.owner == request.user
		#else:
		#	return False
		#return True
		return True