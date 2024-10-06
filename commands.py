from codeop import compile_command
import json
import classes

class AddCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage


    def execute(self, params: []):
        if len(params) != 2:
            print("More then 2 commands")
            return

        if not params[1].isdigit():
            print("Числа в школе прохodil??")
            return
        self.productStorage.storage.append(classes.Product(params[0], params[1]))

        with open("storage.json", "w") as storage_file:
            packed_product = []
            for product in self.productStorage.storage:
                packed_product.append(product.__dict__())
            json.dump(packed_product, storage_file)



class ListCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params: []):
        for x in self.productStorage.storage:
            print(x)


class DelCommand:
    def __init__(self, productStorage: classes.ProductStorage):
        self.productStorage = productStorage

    def execute(self, params):
        if len(params) != 1:
            print("Ну где же ручки? Ну где же наши ручки?")
            return
        if not params[0].isdigit():
            print("1. Откройте приложение Google \n 2. Наберите в поисковой строке \"Изучение чисел 1-10\" \n3. Посмотрите обучающие ролики \n 4. Вернитесь к начальноц позиции")
            return
        if int(params[0]) >= len(self.productStorage.storage):
            print("Ты памойму перепутал")
            return



        self.productStorage.storage.pop(int(params[0]))


class HelpCommand:
    def __init__(self, prorab: classes.Prorab):
        self.prorab = prorab

    def execute(self, params):
        for i in self.prorab.spisok.keys():
            print(i)

class QuitCommand:
    def __init__(self):
        pass

    def execute(self, params: []):
        quit()