import csv


class Pers:
    def __init__(self, name, nationality, age, height, sex):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.sex = sex
        self.height = height

    def eat_smthg(self, product_name, count):
        Set_info("answer.csv").add_meal(self.name, product_name, count)


class Set_info:
    def __init__(self, file_path, columns = ["Персонаж", "Что скушал", "Количество"]):
        self.file_path = file_path
        self.columns = columns

    def add_meal(self, name, product_name, count):
        with open(self.file_path, 'a') as file:
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=self.columns)
            writer.writerow({"Персонаж" : name, "Что скушал" : product_name, "Количество" : count})

    def get_list_of_meals(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return [line for line in reader]


Samoha = Pers("Samoha", "грузин", 33, 151, "male")
Samoha.eat_smthg("ХХХХинкали", 6)
Samoha.eat_smthg("Пхали", 1)

print(Set_info("answer.csv").get_list_of_meals())
