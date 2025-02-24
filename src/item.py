import csv

class Item:
    """Класс для представления товара в магазине."""

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.all.append(self)


    @classmethod
    def instantiate_from_csv(cls, filename: str):
        """Метод для работы с csv файлом и обработкой исключений"""
        try:
            with open(filename, encoding='UTF-8', newline='') as file:
                file_info = csv.DictReader(file)
                for info in file_info:
                    if list(info.keys()) == ["name", "price", "quantity"]:
                        cls(info['name'], float(info['price']), int(info['quantity']))

                    else:
                        raise InstantiateCSVError

        except FileNotFoundError:
                print("Отсутствует файл items.csv")
                return "Отсутствует файл items.csv"

        except InstantiateCSVError as error:
            print(error)
            return error.__str__()

class InstantiateCSVError(Exception):
    """Создан класс для исключений"""
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"

        def __str__(self):
            return self.message

    @staticmethod
    def string_to_number(line):
        numb = int(float(line))
        return numb


    @property
    def name(self):
        """Геттер для работы с .__name"""
        return self.__name


    @name.setter
    def name(self, name_inp: str) -> None:
        """Сеттер для записей атрибутов класса"""
        if len(name_inp) <= 10:
            self.__name = name_inp
        else:
            raise Exception("Наименование товара превышает 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        #return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> float:
        """Применяет установленную скидку для конкретного товара."""
        return self.price * self.pay_rate


    def __repr__(self):
        """Метод repr возвращает строку с данными, которые мы зададим. Ввел данные по требованиям в файле main"""
        return f"{self.__class__.__name__}('{self.name}', \'{self.price}', \'{self.quantity}')"


    def __str__(self):
        """Вывод пользовательской информации"""
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return int(self.quantity) + int(other.quantity)
        raise ValueError("Складывать можно только экземпляры классов Item и Phone")

item = Item('name', 0, 0)
print(repr(item))
