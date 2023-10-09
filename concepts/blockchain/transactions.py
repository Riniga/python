from transaction import Transaction
from clients import clients

transactions = list()

transactions.append(Transaction(clients[0].identity, clients[0]._private_key, clients[1].identity, 500.0))
transactions.append(Transaction(clients[1].identity, clients[1]._private_key, clients[3].identity, 6.0))
transactions.append(Transaction(clients[2].identity, clients[2]._private_key, clients[4].identity, 2.0))
transactions.append(Transaction(clients[3].identity, clients[3]._private_key, clients[2].identity, 4.0))
transactions.append(Transaction(clients[4].identity, clients[4]._private_key, clients[3].identity, 7.0))
transactions.append(Transaction(clients[2].identity, clients[2]._private_key, clients[3].identity, 3.0))
transactions.append(Transaction(clients[3].identity, clients[3]._private_key, clients[1].identity, 8.0))
transactions.append(Transaction(clients[3].identity, clients[3]._private_key, clients[2].identity, 1.0))
transactions.append(Transaction(clients[4].identity, clients[4]._private_key, clients[1].identity, 5.0))
transactions.append(Transaction(clients[4].identity, clients[4]._private_key, clients[2].identity, 3.0))