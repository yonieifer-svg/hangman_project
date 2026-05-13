import random
import time
import os
import subprocess


WORD_DATABASE    = [
    "bottle", "window", "pencil", "scissors", "toothbrush",
    "towel", "blanket", "mirror", "wallet", "backpack",
    "camera", "umbrella", "bucket", "hammer", "screwdriver",
    "basket", "candle", "cushion", "carpet", "sponge",
    "drawer", "shelf", "telescope", "microscope", "compass",
    "notebook", "envelope", "stapler", "calendar", "teapot",
    "fork", "spoon", "plate", "napkin", "matches", "glove",
    "battery", "flashlight", "helmet", "briefcase", "zipper",
    "button", "glasses", "necklace", "bracelet", "perfume",
    "wardrobe", "padlock", "ladder", "whistle", "lantern",
    "chair", "table", "phone", "clock", "shoe", "window", 
    "shirt", "pants", "sock", "coat", "hat", "screen",
    "glass", "plate", "spoon", "knife", "bowl","mouse",
    "brush", "comb", "soap", "towel", "mirror","bottle",
    "couch", "bed", "desk", "lamp", "door","scarf", 
    "book", "pen", "bag", "box", "keys", "plant", "sink",
    "ring", "watch", "coin", "wallet", "card", "rug", 
    "ball", "bike", "car", "oven", "fridge", "belt",
]


def menu_choice():
    choice = -1
    try:
        choice = int(input())
        if choice not in [0, 1]:
            print("please enter number from the menu!")
    except ValueError:
        print("please enter a valid number")
    return choice


def main_menu():
    print("------------------------------")
    print("    - WELCOME TO HANGMAN -    ")
    print("------------------------------")
    time.sleep(1)
    print("1 - play game\n0 - exit\nenter your choice: ")
    choice = -1
    while choice not in [0, 1]:
        choice = menu_choice()
    return choice
    


def choose_word(used_words):
    available_words = [w for w in WORD_DATABASE if w not in used_words]
    if not available_words:
        return None
    word = random.choice(available_words)
    used_words.append(word)
    return word


def show_hidden_word(word, user_letters):
    hidden_word = " ".join([i if i in user_letters else "_" for i in word])
    print("=" * 30)
    print("          THE WORD IS:          ")
    print(f"         {hidden_word.upper()}         ")
    print("=" * 30)
    

def show_attempts_and_letters(attempts, user_letters, word):
    print(f"Attempts left: {attempts}")
    print("Used letters: ")
    print(" ,".join([i for i in user_letters if i not in word]))


def get_letter(user_letters):
    letter = ""
    valid = False 
    while not valid:
        letter = input("Enter letter: ").lower().strip()
        if len(letter) != 1:
            print("Please enter one letter only")
        elif not "a" <= letter <= "z":
            print("Invalid input, Please try again")
        elif letter in user_letters:
            print("You already entered this letter, Please try again")
        else:
            valid = True
            user_letters.append(letter)
    return letter


def letter_processor(letter, word):
    correct = letter in word
    if correct:
        print("Correct!")
    else:
        print("Wrong!")
    time.sleep(1)
    return correct

def word_completed(word, user_letters):
    for i in word:
        if i not in user_letters:
            return False
    print(f"--- YOU WON! ---")
    print(f"--- THE WORD IS ---")
    print(f"      {word.upper()}    ")
    return True

def attempts_left(attempts):
    left = attempts > 0
    if not left:
        print("No attempts left")
    return left

def lose_message(word):
    print(f" --- GAME OVER! --- ")
    time.sleep(1)
    print(f"--- THE WORD WAS ---")
    time.sleep(1)
    print(f"      {word.upper()}    ")
    time.sleep(1)


def leave():
    print("Bye!")
    exit()

def clear_screen():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


def main():

    used_words = []
    choice = -1

    while choice != 0:
        attempts = 10
        user_letters = []

        choice = main_menu()
        if choice == 0:
            continue

        word = choose_word(used_words)

        while not word_completed(word, user_letters):
            clear_screen()
            show_hidden_word(word, user_letters)
            show_attempts_and_letters(attempts, user_letters, word)
            letter = get_letter(user_letters)

            if not letter_processor(letter, word):
                attempts -= 1
                if not attempts_left(attempts):
                    clear_screen()
                    lose_message(word)
                    break

    leave()


if __name__ == "__main__":
    main()


                






    





