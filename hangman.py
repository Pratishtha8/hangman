import random
words = ["parakeet", "meerkat", "beaver", "platypus", "orangutan", "armadillo", "hippopotamus", "labradoodle" "hyena", "jackal", "parrot", "woodpecker", "kingfisher", "ferret", "flamingo", "penguin" ]

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}
def display_man(wrong_guesses):
   print("************************")
   for line in hangman_art[wrong_guesses]:
      print(line)
   print("************************")
def display_answer(answer):
   print(" ".join(answer))
def display_hint(hint):
   print(" ".join(hint))
def main():
    answer= random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses= 0

    guessed_letter = set()
    is_running= True
    while is_running:
         display_man(wrong_guesses)
         display_hint(hint)
         guess= input("Enter a letter you wanna guess: ").lower()
         if guess in answer:
            for i in range(len(answer)):
               if answer[i] == guess:
                  hint[i] = guess
         else:
            wrong_guesses += 1
         if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running= False
         elif wrong_guesses >= len(hangman_art) -1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("looooossseerrrr")
            is_running= False


if __name__ == '__main__':
  main()
