import concurrent.futures as pool
import requests
import os

path = os.getcwd()
dir_photos = os.mkdir(path + '/photos')

url = 'https://aws.random.cat/meow'

def download_photo(number_photo):
    json_photo = requests.get(url).json()['file']
    bytes_photo = requests.get(json_photo).content
    with open('photos' + f'/photo_number{number_photo}.jpg', 'wb') as file:
        file.write(bytes_photo)

with  pool.ThreadPoolExecutor(4) as executor:
    for number_photo in range(50):
        executor.submit(download_photo(number_photo))
