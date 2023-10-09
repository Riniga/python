from client import Client

clients = list()
clients.append(Client("Genesis"))
clients.append(Client("Dinesh"))
clients.append(Client("Ramesh"))
clients.append(Client("Seema"))
clients.append(Client("Vijay"))

def GetClientById(id):
    for client in clients:
        if(client.identity==id): return client.name


