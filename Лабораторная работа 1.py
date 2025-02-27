import doctest


class Phone:
    def __init__(self, brand: str, model: str, year: int, battery_level: float):
        """
        Создание объекта "Телефон"

        :param brand: Марка телефона
        :param model: Модель телефона
        :param year: Год выпуска телефона
        :param battery_level: Уровень заряда батареи в процентах

        Примеры:
        >>> phone = Phone("Apple", "iPhone 12", 2020, 75.0)
        >>> phone.brand
        'Apple'
        >>> phone.battery_level
        75.0
        """
        if not isinstance(brand, str):
            raise TypeError("Марка телефона должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель телефона должна быть строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год выпуска телефона должен быть положительным целым числом")
        if not isinstance(battery_level, (int, float)) or not (0 <= battery_level <= 100):
            raise ValueError("Уровень заряда должен быть числом от 0 до 100")

        self.brand = brand
        self.model = model
        self.year = year
        self.battery_level = battery_level

    def call(self, phone_number: str) -> None:
        """
        Совершить звонок на указанный номер телефона.

        :param phone_number: Номер телефона для звонка

        Примеры:
        >>> phone = Phone("Apple", "iPhone 12", 2020, 75.0)
        >>> phone.call("+1234567890")
        """
        if not isinstance(phone_number, str):
            raise TypeError("Номер телефона должен быть строкой")
        print(f"Звонок на номер: {phone_number}")

    def charge(self, charge_amount: float) -> None:
        """
        Зарядить телефон.

        :param charge_amount: Количество заряда в процентах для добавления

        Примеры:
        >>> phone = Phone("Apple", "iPhone 12", 2020, 50.0)
        >>> phone.charge(30)
        """
        if not isinstance(charge_amount, (int, float)) or charge_amount <= 0:
            raise ValueError("Количество заряда должно быть положительным числом")
        self.battery_level = min(self.battery_level + charge_amount, 100)


class Laptop:
    def __init__(self, brand: str, processor: str, ram_size: int, storage: int):
        """
        Создание объекта "Ноутбук"

        :param brand: Марка ноутбука
        :param processor: Тип процессора
        :param ram_size: Размер оперативной памяти в ГБ
        :param storage: Размер хранения (SSD/HDD) в ГБ

        Примеры:
        >>> laptop = Laptop("Dell", "Intel i7", 16, 512)
        >>> laptop.brand
        'Dell'
        >>> laptop.ram_size
        16
        """
        if not isinstance(brand, str):
            raise TypeError("Марка ноутбука должна быть строкой")
        if not isinstance(processor, str):
            raise TypeError("Тип процессора должен быть строкой")
        if not isinstance(ram_size, int) or ram_size <= 0:
            raise ValueError("Размер оперативной памяти должен быть положительным целым числом")
        if not isinstance(storage, int) or storage <= 0:
            raise ValueError("Размер хранилища должен быть положительным целым числом")

        self.brand = brand
        self.processor = processor
        self.ram_size = ram_size
        self.storage = storage

    def run_program(self, program_name: str) -> None:
        """
        Запуск программы на ноутбуке.

        :param program_name: Название программы

        Примеры:
        >>> laptop = Laptop("Dell", "Intel i7", 16, 512)
        >>> laptop.run_program("Photoshop")
        """
        if not isinstance(program_name, str):
            raise TypeError("Название программы должно быть строкой")
        print(f"Запуск программы: {program_name}")

    def upgrade_storage(self, additional_storage: int) -> None:
        """
        Улучшение хранилища (например, установка дополнительного SSD).

        :param additional_storage: Размер дополнительного хранилища в ГБ

        Примеры:
        >>> laptop = Laptop("Dell", "Intel i7", 16, 512)
        >>> laptop.upgrade_storage(256)
        """
        if not isinstance(additional_storage, int) or additional_storage <= 0:
            raise ValueError("Количество добавляемого хранилища должно быть положительным числом")
        self.storage += additional_storage


class SmartWatch:
    def __init__(self, brand: str, model: str, year: int, battery_level: float):
        """
        Создание объекта "Умные часы"

        :param brand: Марка умных часов
        :param model: Модель умных часов
        :param year: Год выпуска
        :param battery_level: Уровень заряда батареи в процентах

        Примеры:
        >>> watch = SmartWatch("Samsung", "Galaxy Watch 3", 2020, 60.0)
        >>> watch.brand
        'Samsung'
        >>> watch.battery_level
        60.0
        """
        if not isinstance(brand, str):
            raise TypeError("Марка часов должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель часов должна быть строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год выпуска часов должен быть положительным целым числом")
        if not isinstance(battery_level, (int, float)) or not (0 <= battery_level <= 100):
            raise ValueError("Уровень заряда должен быть числом от 0 до 100")

        self.brand = brand
        self.model = model
        self.year = year
        self.battery_level = battery_level

    def track_heart_rate(self) -> None:
        """
        Запуск измерения пульса с помощью умных часов.

        Примеры:
        >>> watch = SmartWatch("Samsung", "Galaxy Watch 3", 2020, 60.0)
        >>> watch.track_heart_rate()
        """
        print("Измеряем пульс...")

    def charge(self, charge_amount: float) -> None:
        """
        Зарядить умные часы.

        :param charge_amount: Количество заряда в процентах для добавления

        Примеры:
        >>> watch = SmartWatch("Samsung", "Galaxy Watch 3", 2020, 30.0)
        >>> watch.charge(50)
        """
        if not isinstance(charge_amount, (int, float)) or charge_amount <= 0:
            raise ValueError("Количество заряда должно быть положительным числом")
        self.battery_level = min(self.battery_level + charge_amount, 100)


if __name__ == "__main__":
    doctest.testmod()
