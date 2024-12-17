from random import randint

class Bank:
    name = 'ICICI Bank'
    clients = []

    def update_db(self, client):
        self.clients.append(client)

    def authentication(self, name, account_number):
        for client in self.clients:
            if client.account['name'] == name and client.account['account_number'] == account_number:
                print("Authentication successful!")
                return client
        print("Authentication failed!")
        return None
