import random


def get_word():
    word_list = ["apple", "banana", "orange"]  # Lista de palavras exemplo
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Vamos jogar!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Por favor, tente outra letra ou palavra: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Você já tentou essa letra:", guess)
            elif guess not in word:
                print(guess, "não faz parte da palavra.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Bom trabalho,", guess, "é uma letra correta!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Você já tentou essa palavra:", guess)
            elif guess != word:
                print(guess, "não é a palavra correta.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Tentativa inválida.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Parabéns! Você acertou todas as letras.")
    else:
        print("Desculpe, suas tentativas acabaram. A palavra era: " + word + ". Talvez na próxima!")

def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Jogar novamente? (S/N) ").upper() == "S":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
