from block import Block

class Blockchain:
   def __init__(self, transaction):
      self.last_block_hash = None
      self.chain = list()
      self.add([transaction])
   
   def add(self, transactions ):
      block = Block(transactions, self.last_block_hash)
      self.last_block_hash = hash(block)
      self.chain.append(block)

   def print (self):
      print ("Number of blocks in the chain: " + str(len(self.chain)))
      for index, block in enumerate(self.chain):
         print ("block # " + str(index) + " Nonce: " + str(block.Nonce) )
         block.print()
         print ('=====================================')