from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .permissions import IsOwner
from .serializers import BlockSerializer, TransactionSerializer, UserSerializer
from .models import Block, Transaction
import datetime as date
import hashlib as hasher
import inflect
import requests

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
		proof_of_work = 0
		try:
		    last_block = Block.objects.latest('id')
		except Block.DoesNotExist:
		    last_block = create_genesis_block()
		# save the next block
		validated_data = serializer.validated_data
		for key, value in validated_data.items():
			if(key == 'proof_of_work'):
				proof_of_work = value
			if(key == 'data'):
				serializer.save(
							index=last_block.index + 1,
							timestamp=date.datetime.now(),
							data='{}'.format(str(value)),
							previous_hash=last_block.current_hash,
							proof_of_work=proof_of_work 
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

class MineBlockView(generics.ListCreateAPIView):
	"""This class defines the create block behavior of the rest api."""
	serializer_class = BlockSerializer
	permission_classes = (permissions.IsAuthenticated, )

	def list(self, request):
		# Get the last_block or create it if it does not exist
		last_block = {}
		try:
		    last_block = Block.objects.latest('id')
		except Block.DoesNotExist:
		    last_block = create_genesis_block()
		last_proof = last_block.proof_of_work
		# Find the proof of work for the current block being mined.
		# Note: The program will hang until a new proof of work is found.
		proof = proof_of_work(last_proof)
		# Gather the data needed to create the new block.
		new_block_index = last_block.index + 1
		new_block_timestamp = this_timestamp = date.datetime.now()
		last_block_hash = last_block.current_hash
		# Create the new Block
		block = Block.objects.create(
									index=new_block_index,
									timestamp=new_block_timestamp,
									data='Hey! I\'m block {}'.format(str(new_block_index)),
									previous_hash=last_block.current_hash,
									proof_of_work=proof
				    			)
		block.save()

		# Once a valid proof of work is found, mine a block so the miner 
		# gets rewarded by adding a transaction.
		miner_address = 'q3nf394hjg-random-miner-address-34nf3i4nflkn3oi'
		block.transaction_set.create(
									sender='network',
									recipient=miner_address,
									amount=1,
									owner=request.user
								)
		dict = {'detail' : 'Blocked mined successfully'}
		return Response(dict)

class ControlBlockView(generics.ListCreateAPIView):
	"""This class defines the create block behavior of the rest api."""
	serializer_class = BlockSerializer
	permission_classes = (permissions.IsAuthenticated, )

	def list(self, request):
		"""
		If blockchains are decentralized, the same chain must be on every node. Each node have to 
		broadcast its version of the chain to the others and allow them to receive the chains of other nodes.
		Each node has to verify the other nodes’ chains so that the every node in the network can come to a 
		consensus of what the resulting blockchain will look like. This is called a consensus algorithm.
		Consensus algorithm: if a node’s chain is different from another’s (i.e. there is a conflict), 
		then the longest chain in the network stays and all shorter chains will be deleted. If there is no conflict 
		between the chains in our network, then we carry on.
		"""
		self.consensus()
		dict = {'detail' : 'Blockchain controlled successfully'}
		return Response(dict)

	def consensus(self):
		# Get the blocks from other nodes
		other_chains = self.find_new_chains()
		# if the current chain is not the longest,
		# store the longest chain

		for chain in other_chains:
			print('!!!!!!!!!!!!!')
			print(len(chain))
			print('!!!!!!!!!!!!!')
			for obj in chain:
				# block data
				for k,v in obj.items():
					# transaction data
					print(k, v)
					if k == 'transaction':
						for tr in v:
							for k1,v1 in tr.items():
								print(k1, v1)
					else:
						print(k, v)

		#longest_chain = blockchain
		#for chain in other_chains:
		#	if len(longest_chain) < len(chain):
		#		longest_chain = chain
		# If the longest chain wasn't ours,
		# then we set the current chain to the longest
		#blockchain = longest_chain

	def find_new_chains(self):
		other_chains = []
		headers = {'Authorization': 'Token 1707e0e2f23bca6e1dfb90faab10bc88108c4197'}
		peer_nodes = ['http://localhost:8000', ]
		for node_url in peer_nodes:
			# create new chain
			curr_chain = []
			# Get the chains using a GET request
			r = requests.get(node_url + '/blocks/', headers=headers)
			if r.status_code == 200:
				for block in r.json():
					if ('id' in block and 'current_hash' in block and 
						'index' in block and 'proof_of_work' in block and 
						'date_modified' in block and 'timestamp' in block and 
						'data' in block and 'previous_hash' in block and 
						'transactions' in block):
						# get translation data
						transactions = []
						for transaction_id in block.get('transactions'):
							# Get the transaction using a GET request
							r = requests.get(node_url + '/transactions/' + str(transaction_id), headers=headers)
							if r.status_code == 200:
								for transaction in r.json():
									# get transaction data
									if('id' in transaction and 'sender' in transaction and 
										'recipient' in transaction and 'amount' in transaction and 
										'owner' in transaction and 'block' in transaction and 
										'date_modified' in transaction and 'date_created' in transaction):
										new_transaction = {
											'id': block.get('id'),
											'sender': block.get('sender'),
											'recipient': block.get('recipient'),
											'amount': block.get('amount'), 
											'owner': block.get('owner'),
											'block': block.get('block'),
											'date_modified': block.get('date_modified'), 
											'date_created': block.get('date_created')
										}
										transactions.append(new_transaction)
						# get block data
						new_block = {
								'id': block.get('id'),
								'current_hash': block.get('current_hash'),
								'index': block.get('index'),
								'proof_of_work': block.get('proof_of_work'),
								'date_modified': block.get('date_modified'),
								'timestamp': block.get('timestamp'),
								'data': block.get('data'),
								'previous_hash': block.get('previous_hash'),
								'transaction': transactions
						}
						curr_chain.append(new_block)
			# Add it to the list
			other_chains.append(curr_chain)
		return other_chains

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

def proof_of_work(last_proof):
	"""
	A Proof-of-work algorithm is an algorithm that generates an item that is difficult 
	to create but easy to verify. The item is called the proof because it is a proof that 
	a computer performed a certain amount of work. To create a new block, a miner's computer 
	will have to increment a number. When that number is divisible 9 and the proof number of the 
	last block, a new block will be mined and the miner will be given a new coin.
	"""
	# Create a variable that we will use to find the next proof of work
	incrementor = last_proof + 1
	# Keep incrementing the incrementor until it's equal to a number divisible by 9 
	# and the proof of work of the previous block in the chain.
	while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
		incrementor += 1
	# Once that number is found, return it as a proof of the work
	return incrementor