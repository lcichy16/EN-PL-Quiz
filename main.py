import json
import random


class LearningApp:
    def __init__(self):
        self.words = self.load_words()
        self.points = 0

    def load_words(self):
        try:
            with open("words.json", "r") as file:
                words = json.load(file)
                return words


        except FileNotFoundError:
            print("Error with File")

    def save_words(self,word):
        try:
            with open("learned_words.json", "a") as file:
                json.dump(self.words[word], file, indent=2)

            with open("words.json", "w") as file:
                data = json.load(file)
                if word in data:
                    del data[word]


        except FileNotFoundError:
            print("Error with File")

    def quiz(self):
        for i in range(10):
            word = random.choice(list(self.words.keys()))
            print(f"Przetłumacz {word} na język polski: \n -------------------")
            answer = input("Odpowiedź: ")

            if answer == self.words[word]:
                self.points += 1
                self.save_words(word)
            else:
                print(f"Niepoprawna odpowiedź! Poprawna odpowiedź to {self.words[word]}")
        print(f"Zdobyłeś {self.points}/10 punktów")
        print("Chcesz dalej się uczyć? t/n ")
        if input().lower() == 't':
            self.quiz()
        else:
            exit(1)

    def start_learning(self):
        print("Witaj w programie do nauki angielskiego! \n\n")
        self.quiz()

if __name__ == "__main__":
    app = LearningApp()
    app.start_learning()
