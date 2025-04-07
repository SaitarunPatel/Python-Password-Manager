import random
import string
import constants

class FileIO:
    file_data_list = []

    def __init__(self):
        self.initial_read_file()

    def initial_read_file(self):
        with open(constants.DATA_PATH, mode="r") as file:
            file_contents = file.readlines()
            for entry_data in file_contents:
                entry_data = entry_data.replace("\n", "")
                split_data = entry_data.split("|")
                self.file_data_list.append({
                    "uid": split_data[0],
                    "website": split_data[1],
                    "email": split_data[2],
                    "password": split_data[3]
                })
        print(self.file_data_list)

    def write_into_file(self, website, email, password):
        self.file_data_list.append({
            "uid": self.generate_uid(),
            "website": website,
            "email": email,
            "password": password
        })
        with open(constants.DATA_PATH, mode="w") as file:
            for entry_data in self.file_data_list:
                file.write(f"{entry_data['uid']}|{entry_data['website']}|{entry_data['email']}|{entry_data['password']}\n")

    def generate_uid(self, chars_len=10):
        # Logic to generate UID
        characters = string.ascii_letters + string.digits
        uid = ''.join(random.choice(characters) for _ in range(chars_len))
        return uid

    def generate_password(self, char_len=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(char_len))
        return password