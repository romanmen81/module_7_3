import re


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем имена файлов в атрибуте
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            # Открываем файл и считываем содержимое
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                # Приводим текст к нижнему регистру и удаляем пунктуацию
                content = content.lower()
                content = re.sub(r"[.,!?;:\-]", " ", content)
                # Разбиваем текст на слова
                words = content.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()  # Получаем все слова
        for file_name, words in all_words.items():
            # Ищем индекс первого вхождения слова
            if word in words:
                result[file_name] = words.index(word) + 1  # индексация начинается с 0, а требуется с 1
        return result

    def count(self, word):
        result = {}
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()  # Получаем все слова
        for file_name, words in all_words.items():
            # Считаем количество вхождений слова
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

# Пример использования:
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Вывод всех слов из всех файлов
print(finder.find('TEXT'))      # Позиция первого вхождения
print(finder.count('teXT'))     # Количество вхождений