class Movie:
    """
    Базовый класс для всех фильмов.
    
    Атрибуты:
    title: Название фильма.
    director: Режиссёр фильма.
    genre: Жанр фильма.
    release_year: Год выпуска фильма.
    
    Методы:
    __init__(self, title: str, director: str, genre: str, release_year: int): Инициализирует объект фильма.
    __str__(self): Возвращает строковое представление фильма (название, режиссёр, жанр, год выпуска).
    __repr__(self): Возвращает официальное строковое представление объекта фильма.
    """
    
    def __init__(self, title: str, director: str, genre: str, release_year: int) -> None:
        """
        Инициализирует объект фильма с его названием, режиссёром, жанром и годом выпуска.
        
        :param title: Название фильма.
        :param director: Режиссёр фильма.
        :param genre: Жанр фильма.
        :param release_year: Год выпуска фильма.
        """
        self.title = title
        self.director = director
        self.genre = genre
        self.release_year = release_year
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление фильма.
        
        :return: Строка с названием фильма, режиссёром, жанром и годом выпуска.
        """
        return f"Фильм '{self.title}', режиссёр: {self.director}, жанр: {self.genre}, год выпуска: {self.release_year}."
    
    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление фильма.
        
        :return: Строка с названием класса и аттрибутами.
        """
        return f"Movie(title='{self.title}', director='{self.director}', genre='{self.genre}', release_year={self.release_year})"


class Documentary(Movie):
    """
    Класс для представления документального фильма, наследуется от класса Movie.
    
    Дополнительный атрибут:
    topic: Тема документального фильма.
    
    Перегруженные методы:
    __str__(self): Представление документального фильма с указанием темы.
    __repr__(self): Официальное строковое представление документального фильма.
    
    Расширенные методы:
    narration_style(self): Описание стиля повествования в документальном фильме.
    """
    
    def __init__(self, title: str, director: str, genre: str, release_year: int, topic: str) -> None:
        """
        Инициализирует объект документального фильма, расширяя атрибуты базового класса Movie.
        
        :param title: Название фильма.
        :param director: Режиссёр фильма.
        :param genre: Жанр фильма.
        :param release_year: Год выпуска фильма.
        :param topic: Тема документального фильма.
        """
        super().__init__(title, director, genre, release_year)
        self.topic = topic
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление документального фильма с указанием темы.
        
        :return: Строка с названием, режиссёром, жанром, годом выпуска и темой.
        """
        return f"Документальный фильм '{self.title}', режиссёр: {self.director}, жанр: {self.genre}, год выпуска: {self.release_year}, тема: {self.topic}."
    
    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление документального фильма.
        
        :return: Строка с названием класса и аттрибутами.
        """
        return f"Documentary(title='{self.title}', director='{self.director}', genre='{self.genre}', release_year={self.release_year}, topic='{self.topic}')"
    
    def narration_style(self) -> str:
        """
        Описание стиля повествования в документальном фильме.
        
        :return: Строка с описанием стиля повествования.
        """
        return "Документальные фильмы обычно используют объективное и информативное повествование, подчеркивающее факты."


class FeatureFilm(Movie):
    """
    Класс для представления художественного фильма, наследуется от класса Movie.
    
    Дополнительный атрибут:
    cast: Список актеров, снимающихся в фильме.
    
    Перегруженные методы:
    __str__(self): Представление художественного фильма с указанием актеров.
    __repr__(self): Официальное строковое представление художественного фильма.
    
    Расширенные методы:
    plot_summary(self): Описание сюжета художественного фильма.
    """
    
    def __init__(self, title: str, director: str, genre: str, release_year: int, cast: list) -> None:
        """
        Инициализирует объект художественного фильма, расширяя атрибуты базового класса Movie.
        
        :param title: Название фильма.
        :param director: Режиссёр фильма.
        :param genre: Жанр фильма.
        :param release_year: Год выпуска фильма.
        :param cast: Список актеров, снимающихся в фильме.
        """
        super().__init__(title, director, genre, release_year)
        self.cast = cast
    
    def __str__(self) -> str:
        """
        Возвращает строковое представление художественного фильма с указанием актеров.
        
        :return: Строка с названием, режиссёром, жанром, годом выпуска и актёрами.
        """
        return f"Художественный фильм '{self.title}', режиссёр: {self.director}, жанр: {self.genre}, год выпуска: {self.release_year}, актёры: {', '.join(self.cast)}."
    
    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление художественного фильма.
        
        :return: Строка с названием класса и аттрибутами.
        """
        return f"FeatureFilm(title='{self.title}', director='{self.director}', genre='{self.genre}', release_year={self.release_year}, cast={self.cast})"
    
    def plot_summary(self) -> str:
        """
        Описание сюжета художественного фильма.
        
        :return: Строка с кратким описанием сюжета.
        """
        return "Художественные фильмы обычно имеют вымышленный сюжет, ориентированный на развлечение зрителя."
