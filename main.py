import email
from http import client
import sys


clients = [
    {
    'name':'Pablo',
    'company': 'Google',
    'email': 'pablo@google.com',
    'position': 'Software engineer',
    },
    {
    'name':'Ricardo',
    'company': 'Facebook',
    'email': 'ricardo@facebook.com',
    'position': 'Data engineer',

    }
]
def get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

        return field

def get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client\'s name? ')
        if client_name=='exit':
            break
        if not client_name:
            sys.exit()
    return client_name

def create_client(client_name):
    global clients

    if client not in clients:
        clients.append(client)
        
    else:
        print('Client is already is in the client\'s list')

def list_clients():
    for idx, client in enumerate(client):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))

def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = update_client
    else:
        print('Client is not in client\'s list ')

def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in clients list')

def search_client(client_name):

    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')



if __name__ == '__main__':
    print_welcome()
    command = input()
    command = command.upper()

    command = input()

    if command == 'C':
        client = {
            'name': get_client_field('name'),
            'company': get_client_field('company'),
            'email': get_client_field('email'),
            'position': get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'D':
        client_name = get_client_name()
        delet_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = get_client_name()
        found = serch_client(client_name)
        if found :
            print('The client is in the client\'s list')
        else:
            print('the client: {} is not in our client\'s list')
    elif command == 'U':
        client_name = get_client_name()
        update_client_name = input('What is the update client name')
        update_client(client_name, update_client_name)
        list_clients()
    else:
        print('Invalid command')
