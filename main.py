
import utils
from player import Player

words_JSON = "https://www.jsonkeeper.com/b/MOJW"



def main():

    print("Ввведите имя игрока")
    user_name_input = input()
    basic_word = utils.load_random_word(words_JSON)

    player = Player(user_name_input)
    print(f"Привет, {player.get_name()}!")
    print(f"Составьте 8 слов из слова {basic_word.get_word()}\n"
           "Слова должны быть не короче 3 букв\n"
           "Чтобы закончить игру, угадайте все слова или напишите 'stop'\n"
           "Поехали, ваше первое слово?\n"
          )

    while player.count_correct_words() < basic_word.count_subwords():

        user_input = input()
        if user_input in ["stop", "стоп"]:
            break
        elif len(user_input) < 3:
            print("слишком короткое слово")

        elif not basic_word.has_subword(user_input):
            print("неверно")

        elif player.test_word(user_input):
            print("уже использовано")

        else:
            print("верно")
            player.add_word(user_input)


    print(f"Игра завершена, вы угадали {player.count_correct_words()} слов!")



if __name__ == '__main__':
    main()


