import hashlib
import datetime
import time

class Block:
    def __init__(self, index, data, previousHash=''):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.previousHash = previousHash
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        content = f'{self.index}{self.timestamp}{self.data}{self.previousHash}{self.nonce}'
        return hashlib.sha256(content.encode()).hexdigest()

    def mineBlock(self, difficulty):
        print(f"⛏️ Mining block with difficulty {difficulty}...")
        target = '0' * difficulty
        start_time = time.time()
        attempts = 0

        while self.hash[:difficulty] != target:
            self.nonce += 1
            attempts += 1
            self.hash = self.calculateHash()

        end_time = time.time()
        print(f"✅ Block mined: {self.hash}")
        print(f"⏱️ Time: {end_time - start_time:.4f} seconds | Attempts: {attempts}")

# Mining example
difficulty = 4
block = Block(1, "Transaction Data", "0000abcdef")
block.mineBlock(difficulty)
