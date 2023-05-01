import pickle


class Fruits:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def describe(self):
        print(self.name, self.calories, sep=': ')


if __name__ == '__main__':
    # fruit: Fruits = Fruits('Banana', 100)
    #
    # fruit.calories = 200
    #
    # with open('data.pikle', 'wb') as file:
    #     pickle.dump(fruit, file)

    with open('data.pikle', 'rb') as file:
        fruit: Fruits = pickle.load(file)
        fruit.describe()
