import binascii
import datetime
import collections
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
from clients import GetClientById

class Transaction:
   def __init__(self, senderid, senderkey, recipientid, value):
      self.senderid = senderid
      self.senderkey = senderkey
      self.recipientid = recipientid
      self.value = value
      self.time = datetime.datetime.now()
   
   def to_dict(self):
      return collections.OrderedDict({'sender': self.senderid,'recipient': self.recipientid, 'value': self.value, 'time' : self.time})
   
   def sign_transaction(self):
      signer = PKCS1_v1_5.new(self.senderkey)
      h = SHA.new(str(self.to_dict()).encode('utf8'))
      return binascii.hexlify(signer.sign(h)).decode('ascii')
   
   def print(self):
      dict = self.to_dict()
      print ("Sender:\t\t" + dict['sender'][53:63] + "..." + dict['sender'][-15:] + "("+GetClientById(self.senderid)+")")
      print ("Recipient:\t" + dict['recipient'][53:63] + "..." + dict['recipient'][-15:] + "("+GetClientById(self.recipientid)+")")
      print ("Value: " + str(dict['value']))
      print ("Time: " + str(dict['time']))
      print ("Signature: " + self.sign_transaction())