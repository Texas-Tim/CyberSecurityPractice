"""
1. read in seed value from the command line
2. generate 50 tokens of length 20 using the seed value
3. write the tokens to a file called `tokens.txt`
4. the seed value should be the current epoch time in milliseconds, so we can adjust it
   by a constant value to account for the time taken to run the script and the time taken
   to submit the tokens to the picoCTF server
"""

import random
import sys
import time

def get_random(length, seed=None):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    if seed == None:
        random.seed(int(time.time() * 1000))  # seeding with current time 
    else:
        random.seed(seed)  # seeding with the provided seed value
    token = ""
    for i in range(length):
        token += random.choice(alphabet)
    return token


# main function that takes a single input integer argument for the seed, although integer is not enforced, the code will not work properly otherwise
if __name__ == "__main__":
    # time_ = time.time()

    seed = int(sys.stdin.readline().strip())
    #seed should be the approximate value between this function call and the call to the picoCTF server. We can adjust by 50 as required
    equalizer = 400
    seed += equalizer

    #picoCTF challenge has a max guess count of 50 and generates a token of length 20
    num_guesses = 51
    token_length = 20
    token_list = []

    #call the random token generator function with the seed and token length and write the tokens to a local file, overwriting the file each time
    with open('tokens.txt', 'w') as tokens:
        for i in range(num_guesses):
            token = get_random(token_length, seed=seed)
            token_list.append(token)
            # well need about 50 different tokens. We are trying to identify the exact seed value the server used to generate the token
            seed += 1
        tokens.writelines("\n".join(token_list))

    # time_ = (time.time() - time_) * 1000
    # print(f"\nTime taken to run the program: {time_:.8f} milliseconds")

    

