import os
import shutil
import numpy as np
import threading
import requests

path_ = 'user_data/'

def parse_users(users, path_to_save):
    for user in users:
        try:
            img = requests.get(user['picture']['large'], stream=True)
            path = path_to_save + str(user['location']['postcode'])
            os.mkdir(path)
            with open(path + '/avatar.png', 'wb') as f:
                shutil.copyfileobj(img.raw, f)

            with open(path + "/user_info.txt", "w") as file:
                file.writelines(f"{str(user['gender'])}, "
                                f"{str(user['name']['first'])} {str(user['name']['last'])}")

        except OSError:
            continue




def get_users(count):
    users = []
    for page in range(count+1):
        response = requests.get('https://randomuser.me/api')
        currencies = response.json()['results']
        users.extend(currencies)
    return users


def start_thread(path_to_save, users):
    users = get_users(users)
    threads = []
    for list_slice in np.array_split(users, 4):
        thread = threading.Thread(target=parse_users, args=(list(list_slice), path_to_save))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


start_thread(path_, 12)
