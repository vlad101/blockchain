from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import BlockSerializer, TransactionSerializer, UserSerializer
from .models import Block, Transaction
import datetime as date
import hashlib as hasher
import inflect

def create_genesis_block():
	"""
	First block, or genesis block, is a special block. 
	it’s added manually or has unique logic allowing it to be added.
	A function returns a genesis block. This block is of index 0, current timestamp, 
	an arbitrary data value and an arbitrary value of the previous hash.
	"""
	last_block = Block.objects.create(
								index=0,
								timestamp=date.datetime.now(),
								data='Genesis Block',
								previous_hash='0'
							)
	last_block.save()
	return last_block

class CreateTransactionView(generics.ListCreateAPIView):
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
		"""Any user can let the nodes know that a new transaction has occurred."""
		validated_data = serializer.validated_data
		print('New transaction')
		for key, value in validated_data.items():
			if(key == 'sender'):
			    print('FROM: {}'.format(value))
			if(key == 'recipient'):
			    print('TO: {}'.format(value))
			if(key == 'amount'):
			    print('AMOUNT: {}'.format(value))
		print('Transaction submission successful')
		serializer.save(owner=self.request.user)

class DetailsTransactionView(generics.RetrieveUpdateDestroyAPIView):
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

class CreateBlockView(generics.ListCreateAPIView):
	"""This class defines the create behavior of the rest api."""
	queryset = Block.objects.all()
	serializer_class = BlockSerializer
	permission_classes = (permissions.IsAuthenticated, )

	def perform_create(self, serializer):
		"""Save the post data when creating a new block.
		After a genesis block is created, this function will generate succeeding 
		blocks in the blockchain. This function will take the previous block in the 
		chain as a parameter, create the data for the block to be generated, and 
		return the new block with its appropriate data. When new blocks hash information 
		from previous blocks, the integrity of the blockchain increases with each new block. 
		This chain of hashes acts as cryptographic proof and helps ensure that once a block 
		is added to the blockchain it cannot be replaced or removed.
		"""

		# get the last_block or create it if it does not exist
		last_block = {}
		try:
		    last_block = Block.objects.latest('id')
		except Block.DoesNotExist:
		    last_block = create_genesis_block()
		# save the next block
		validated_data = serializer.validated_data
		for key, value in validated_data.items():
			if(key == 'data'):
				serializer.save(
					index=last_block.index + 1,
					timestamp=date.datetime.now(),
					data='{}'.format(str(value)),
					previous_hash=last_block.current_hash
		   		)

class AddBlockView(generics.ListCreateAPIView):
	"""This class defines the create block behavior of the rest api."""
	serializer_class = BlockSerializer
	permission_classes = (permissions.IsAuthenticated, )

	def list(self, request, num_of_blocks_to_add):
		# get number of blocks to add integer value
		num_of_blocks_to_add = int(num_of_blocks_to_add)
		# pluralize
		p = inflect.engine()
		# save the next block
		for i in range(0, num_of_blocks_to_add):
			# get the last_block or create it if it does not exist
			last_block = {}
			try:
			    last_block = Block.objects.latest('id')
			except Block.DoesNotExist:
			    last_block = create_genesis_block()
		    # increment index
			this_index = last_block.index + 1
			block = Block.objects.create(
							index=this_index,
							timestamp=date.datetime.now(),
							data='Hey! I\'m block {}'.format(str(this_index)),
							previous_hash=last_block.current_hash
			    			)
			block.save()
			print("Block #{} has been added to the blockchain!\n{}".format(this_index, block))
		dict = {'detail' : '{} {} added successfully'.format(num_of_blocks_to_add, p.plural("block", num_of_blocks_to_add))}
		return Response(dict)

class DetailsBlockView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the HTTP GET, PUT and DELETE requests."""
	queryset = Block.objects.all()
	serializer_class = BlockSerializer
	permission_classes = (permissions.IsAuthenticated, )

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer