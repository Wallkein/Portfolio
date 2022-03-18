import random
import time

computer_score = 0
player_score = 0
print("Камень давит ножницы, ножницы режут бумагу, бумага накрывает камень.")
computer_attack = ["камень","ножницы","бумага"]


while True:
    if player_score == 10:
        print("Вы победили")
        print("У вас:", player_score, "\nУ компьютера:", computer_score)
        time.sleep(10)
        break
    elif computer_score == 10:
        print("Вы проиграли")
        print("У вас:", player_score, "\nУ компьютера:", computer_score)
        time.sleep(10)
        break
        
    
    print("У вас:", player_score, "\nУ компьютера:", computer_score)
    player = input("Выберете: камень, ножницы или бумага (выйти)? ").lower()
    computer = random.choice(computer_attack)
    print("Твой выбор:", player, "\nкомпьютер выбрал:", computer)

    if player == computer:
        print("Ничья!")
    elif player == "бумага":
        if computer == "камень":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер")
            computer_score = computer_score + 1
    elif player == "камень":
        if computer == "ножницы":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер")
            computer_score = computer_score + 1
    elif player == "ножницы":
        if computer == "бумага":
            print("Ты победил!")
            player_score = player_score + 1
        else:
            print("Победил компьютер")
            computer_score = computer_score + 1
    elif player == "Выйти":
        print("Вы вышли из игры")
        break
    else:
        print("Произошла ошибка...")
