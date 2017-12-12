import hashlib as hasher

class Block:
	"""
	Block is the container for the new data.
	Each block has a timestamp, an index (optional), hash, 
	previous hash (each block requires information from the previous block) and data.
	Hash ensures integrity throughout the blockchain. 
	"""
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def hash_block(self):
			"""
			Block's hash is a cryptographic hash of the block's index, 
			timestamp, data, hash, and the hash of the previous block.
			"""
			sha = hasher.sha256()
			sha.update((str(self.index) + 
						str(self.timestamp) + 
						str(self.data) +
						str(self.previous_hash)).encode('utf-8'))
			return sha.hexdigest()

	def __str__(self):
		"""
		Custom string representation of the block object.
		"""
		retVal = 'Block {{index={}, timestamp={}, data={}, previous_hash={}, hash={}}}'.format(
																								str(self.index), 
																								str(self.timestamp), 
																								str(self.data), 
																								str(self.previous_hash), 
																								str(self.hash))
		return retVal