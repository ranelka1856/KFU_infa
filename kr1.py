

class Gun:
    def __init__(self, caliber, mass):
        self.caliber = caliber
        self.mass = mass
        self.power = self.caliber * self.mass


#Используем стек для класса обоймы
class Oboima(Gun):
    def __init__(self):
        self.mag = []

    def add(self, Gun):
        self.mag.append(Gun)

    def remove(self):
        if len(self.mag > 0):
            self.mag.pop(-1)
        else:
            print("Обойма пуста")

oboima = Oboima()
oboima.add(Gun(1, 0.1))
oboima.add(Gun(2, 0.2))
oboima.add(Gun(123, 0.54321))

def set_info():
    f = open("info.txt", "w")
    global oboima
    f.write("В обойме " + str(len(oboima.mag)) + " снаряда:\n")
    for i in range(len(oboima.mag)):
        f.write("Снаряд " + str(i + 1) + ": " + str(oboima.mag[i].caliber) + ", " + str(oboima.mag[i].mass) + ", " + str(oboima.mag[i].power) + "\n")
    f.close()

set_info()

