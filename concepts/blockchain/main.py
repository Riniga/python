from transactions import transactions   
from blockchain import Blockchain

blockchain = Blockchain(transactions[0])
blockchain.add(transactions[1:4])
blockchain.add(transactions[4:7])
blockchain.add(transactions[7:10])
blockchain.print()