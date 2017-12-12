import datetime as date

from block import Block

def create_genesis_block():
	"""
	First block, or genesis block, is a special block. 
	it’s added manually or has unique logic allowing it to be added.
	A function returns a genesis block. This block is of index 0, current timestamp, 
	an arbitrary data value and an arbitrary value of the previous hash.
	"""
	return Block(0, date.datetime.now(), "Genesis Block", "0")