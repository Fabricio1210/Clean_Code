import random

class Game:
    def __init__(self):
        self.number_to_guess = random.randint(1, 20)
        self.current_guess = 0
        self.attempts = 0

    def get_guess(self):
        try:
            guessed_number = int(input("Adivina el número: "))
            self.current_guess = guessed_number
            return True
        except ValueError as e:
            print(e)
            return False

    def get_attempts(self):
        try:
            self.attempts = int(input("Cuantos intentos quieres? "))
            return True
        except ValueError as e:
            print(e)
            return False

    def validate_guess(self):
        if self.current_guess < self.number_to_guess:
            print("Muy bajo")
        elif self.current_guess > self.number_to_guess:
            print("Muy alto")
        elif self.current_guess == self.number_to_guess:
            print("¡Correcto!")
        else:
            print("Error")
            print("Número de intentos:", self.attempts)

    def start(self):
        attempts_failed = 1
        print("Adivina el número entre 1 y 20")
        while not self.get_attempts():
            print("Intentalo denuevo")
        while self.current_guess != self.number_to_guess:
            while not self.get_guess():
                print("Intentalo denuevo")
            attempts_failed += 1
            self.validate_guess()
            if self.attempts < attempts_failed:
                print("Te quedaste sin intentos")
                break


if __name__ == "__main__":
    Game().start()