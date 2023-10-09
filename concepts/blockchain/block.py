from miner import Miner
miner = Miner(3)

class Block:
   def __init__(self,transactions=list(), previous_block_hash=None,Nonce=None ):
      self.transactions = transactions
      self.previous_block_hash = previous_block_hash
      self.Nonce =  miner.mine(self)

   def print(self):
      for transaction in self.transactions:
         transaction.print()
         print ('--------------')