class Player:
    """
    Класс для имени пользователя и списка использованных слов пользователя
    """
    def __init__(self, name, correct_words=None):
        self.name = name

        if correct_words is None:
            self.correct_words = []
        else:
            self.correct_words = correct_words

    def get_name(self):
        """
        Возвращает имя пользователя
        """
        return self.name

    def count_correct_words(self):
        """
        Возвращает количество использованных слов
        :return: int
        """
        return len(self.correct_words)

    def add_word(self, word):
        """
        Добавляет слово в список использованных слов
        """
        self.correct_words.append(word)

    def test_word(self, word):
        """
        Проверяет использовалось ли данное слово до этого
        :return: bool
        """
        return word in self.correct_words

    def __repr__(self):
        return f"Player({self.name}, {self.correct_words})"


