from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Block, Transaction

class TransactionSerializer(serializers.ModelSerializer):
	"""Serializer to map the transaction model instance into JSON format."""

	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		"""Meta class to map serializer's fields with the transaction model fields."""
		model = Transaction
		fields = ('id', 'sender', 'recipient', 'amount', 'owner', 'date_created', 'date_modified', )
		read_only_fields = ('date_created', 'date_modified', )

class BlockSerializer(serializers.ModelSerializer):
	"""Serializer to map the block model instance into JSON format."""

	class Meta:
		"""Meta class to map serializer's fields with the block model fields."""
		model = Block
		fields = ('id', 'index', 'timestamp', 'data', 'previous_hash', 'current_hash', 'date_modified', )
		read_only_fields = ('index', 'date_modified', 'previous_hash', 'current_hash', )

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    transaction = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'transaction')