import requests
import os
from pathlib import Path


my_file = Path("category_data")
if my_file.is_dir():
    pass
else:
    os.mkdir('category_data')

path = 'category_data/'


def parse_category():
    response = requests.get('https://jservice.io/api/categories?count=100').json()
    category = {}
    for page in range(len(response)):
        currencies = response[page]
        id_of_category = currencies['id']
        title = currencies['title']
        category[title] = id_of_category
    return category


def parse_questions(category, count):
    categories = parse_category()
    id = categories[category]
    response = requests.get(f'https://jservice.io/api/clues?category={id}')
    questions = []
    page = 0
    while page < count:
        currencies = response.json()[page]
        question = currencies['question']
        if question == '=':
            page += 1
            count += 1
        else:
            with open(path + "/questions.txt", "a") as file:
                file.writelines(f"{str(question)}\n")
            page += 1
    return questions


parse_questions('egypt', 2)
