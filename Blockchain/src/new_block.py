import datetime as date

from block import Block

def next_block(last_block):
	"""
	After a genesis block is created, this function will generate succeeding 
	blocks in the blockchain. This function will take the previous block in the 
	chain as a parameter, create the data for the block to be generated, and 
	return the new block with its appropriate data. When new blocks hash information 
	from previous blocks, the integrity of the blockchain increases with each new block. 
	This chain of hashes acts as cryptographic proof and helps ensure that once a block 
	is added to the blockchain it cannot be replaced or removed.
	"""
	this_index = last_block.index + 1
	this_timestamp = date.datetime.now()
	this_data = "Hey! I'm block {}".format(str(this_index))
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)