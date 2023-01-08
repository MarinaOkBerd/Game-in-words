class BasicWord:
    """
    Класс для вводного слова и набора допустимых подслов
    """
    def __init__(self, word="", subwords=None):
        self.word = word
        if subwords is None:
            self.subwords = []
        else:
            self.subwords = subwords

    def get_word(self):
        """
        Возвращает исходное слово
        """
        return self.word

    def count_subwords(self):
        """
        Возвращает количество подслов
        :return: int
        """
        return len(self.subwords)

    def has_subword(self, word):
        """
        Проверяет наличие введенного слова в списке допустимых подслов
        :return: bool
        """
        return word in self.subwords

    def __repr__(self):
        return f"BasicWord({self.word}, {self.subwords})"


