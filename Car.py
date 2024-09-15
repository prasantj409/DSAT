from tkinter.font import names


class Car:
    def __init__(self,speed = 0):
        self.speed = speed
        self.odometer = 0
        self.time=0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer/self.time

if __name__ == '__main__':

    myCar = Car()
    print("I'm a car")

    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()

        if action not in 'ABOS' or len(action) != 1:
            print("I don't know how to do that")
            continue

        if action == "A":
            myCar.accelerate()
            print("Accelerating...")

        elif action == "B":
            myCar.brake()
            print("Braking...")

        elif action == "O":
            print("Your car has driven {} kilometers".format(myCar.odometer))

        elif action == "S":
            print("The car's average speed was {} kph".format(myCar.average_speed()))

        myCar.step()
