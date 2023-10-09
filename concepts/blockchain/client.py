import binascii
import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
   def __init__(self, name):
      random = Crypto.Random.new().read
      self.name = name
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)
      self.identity = binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')