import random 
import sys 

def main():
    secret_number = generate_number()
    while(True):
        guess = int(input("Guess what the random number is "))
        output = validate_guess(guess, secret_number)
        print(output)
        if output == ['fermi', 'fermi', 'fermi']:
            sys.exit("You figured it out")
        



def validate_guess(guess:int, secret_number:int) -> list: 
    secret_list = [int(d) for d in str(secret_number)]
    guess_list = [int(d) for d in str(guess)]
    answer_list = []
    for i, guess in enumerate(guess_list): 
        if guess == secret_list[i]:
            answer_list.append("fermi")
        elif guess in secret_list:
            answer_list.append("pico")
    
    if len(answer_list) == 0:
        return ["Bagels"]
    else: 
        return answer_list

        


# Okay for now but not flexible 
def generate_number() -> int:
    return random.randint(100,999)



if __name__ == "__main__":
    main()