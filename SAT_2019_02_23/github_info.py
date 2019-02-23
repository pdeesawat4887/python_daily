import requests
import json
import getpass


class User:

    def __init__(self):
        self.user = input('Insert Username: ')
        self.send_request(self.user, getpass.getpass('Enter password: '))
        self.convert_string_to_dictionary()
        self.information()

    def send_request(self, usr, pwd):
        try:
            self.request = requests.get('https://api.github.com/user', auth=(usr, pwd))
        except Exception as error:
            print(error)

    def convert_string_to_dictionary(self):
        json_acceptable_string = self.request.text.replace("'", "\"")
        self.released = json.dumps(json.loads(json_acceptable_string), indent=10, sort_keys=True)

    def information(self):
        if 'message' in self.released:
            print('Error', self.released['message'])
        else:
            print(self.released)


user = User()
