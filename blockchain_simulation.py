import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previousHash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        content = f'{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}'
        return hashlib.sha256(content.encode()).hexdigest()

    def __str__(self):
        return f'Block {self.index}:\nData: {self.data}\nHash: {self.hash}\nPreviousHash: {self.previousHash}\n'

# Create blockchain
blockchain = []

def create_genesis_block():
    return Block(0, datetime.datetime.now(), 'Genesis Block', '0')

def create_next_block(previous_block, data):
    return Block(previous_block.index + 1, datetime.datetime.now(), data, previous_block.hash)

# Generate 3 blocks
blockchain.append(create_genesis_block())
blockchain.append(create_next_block(blockchain[-1], 'Block 1 Data'))
blockchain.append(create_next_block(blockchain[-1], 'Block 2 Data'))

# Display blocks
for block in blockchain:
    print(block)

# Tamper Block 1
print("\n--- Tampering Block 1 ---\n")
blockchain[1].data = "Tampered Data"
blockchain[1].hash = blockchain[1].calculateHash()

# Re-check the chain
for block in blockchain:
    print(block)
