import hashlib

class Miner:
   def __init__(self, difficulty=1):
      assert difficulty >= 1
      self.prefix = '1' * difficulty

   def sha256(self, object):
      return hashlib.sha256(object.encode('ascii')).hexdigest()

   def mine(self, object):
      for i in range(100000):
         digest = self.sha256(str(hash(object)) + str(i))
         if digest.startswith(self.prefix):
            #print ("after " + str(i) + " iterations found nonce: "+ digest + " for object " + str(hash(object)))
            return (digest, i)