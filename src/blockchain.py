from genesis import create_genesis_block
from new_block import next_block

"""
Create the blockchain, a Python list. Add the first element of the list (the genesis block). 
Add the 20 succeeding blocks using a for loop.
"""
def runBlockChain():
	blockchain = [create_genesis_block()]
	previous_block = blockchain[0]
	num_of_blocks_to_add = 20

	for i in range(0, num_of_blocks_to_add):
		block_to_add = next_block(previous_block)
		blockchain.append(block_to_add)
		previous_block = block_to_add
		print("Block #{} has been added to the blockchain!\n{}".format(block_to_add.index, block_to_add))


"""
Run the code when the file is loaded.
"""
if __name__ == "__main__":
    runBlockChain()