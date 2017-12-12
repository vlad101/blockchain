# Blockchain

Python implementation of a Blockchain.

## Getting Started

### Terms

### Test Coin

Each block has a timestamp, an index, data, hash of the previous block, a generated cryptographic hash (the block’s index, timestamp, data, and the hash of the previous block’s hash).

### Genesis Block

The genesis block, first block, is the first manually added block that has a an index 0, a current timestamp, an arbitrary data, and an arbitrary hash value of the previous block.

### Next Block

Next block function will take the previous block in the chain as a parameter, create the data for the block to be generated, and return the new block with the data. When new blocks hash information from previous blocks, the integrity of the blockchain increases with each new block.

### Test Function

Blockchain, a simple python list, is created. The first element of the list is the genesis block. The twenty succeeding blocks are added with a for loop.

## Authors

* **Vladimir Efros** - *Initial work*