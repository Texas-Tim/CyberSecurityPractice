import hashlib


"""
1. Loop through all 256 permutations of two nibbles (0x00 to 0xFF)
2. For each cheese in the cheese list, iterate through all possible salt values (0x00 to 0xFF)
3. Iterate through all suggested encodings (`utf-8, utf-16-le, utf-16-be, latin-1, ascii`)
4. For each type of salt (`raw byte, hex string`), iterate again
4. For each cheese and salt combination, iterate through all possible string positions when inserting the salt
5. For each combination, compute the hash and check if it matches the target hash
6. If a match is found, print the cheese, salt, and hash and terminate the search
7. If no match is found after all iterations, print a message indicating that no match was found
8. Avoid errors where possible
"""


def find_cheese(encoding, target_hash, match_found=False):
    print("Let's crack the cheese!")

    with open('cheese_list.txt', 'r') as cheese_file: 
        cheese_list = cheese_file.read().splitlines()
        print(f"Target hash: {target_hash}")
        print(f"Total cheeses to check: {len(cheese_list)}")
        
        for cheese in cheese_list:
            for salt_nib in range(256):
                for enc in encoding:
                    #encode the cheese with the current encoding
                    encoded_cheese = cheese.encode(enc)

                    #create the raw salt and hex salt
                    #raw salt is a single byte with the value of salt_nib
                    #hex salt is the hex representation of salt_nib
                    raw_salt = bytes([salt_nib])
                    try:
                        hex_salt = format(salt_nib, '02x').encode(enc)
                    except:
                        #default encryption
                        hex_salt = format(salt_nib, '02x').encode("utf-8")
                    salt_list = [raw_salt, hex_salt]
                    #for each salt, update the hash object with the encoded cheese and the salt
                    for salt in salt_list:
                        #for each cheese string position, insert the salt at every possible index
                        for i in range(len(encoded_cheese) + 1):
                            #check cheese upper and lower case variations
                            cheese_case = [encoded_cheese, encoded_cheese.upper(),encoded_cheese.lower()]
                            
                            for case in cheese_case:
                                #insert the salt at index i
                                cheese_hash = case[:i] + salt + case[i:]

                                #update the hash object with the cheese_hash
                                hash_hex = hashlib.sha256(cheese_hash).hexdigest()

                                # #write all cheese_hash to text.txt (used with single cheese to test implementation)
                                # with open('test.txt', 'a') as f:
                                #     f.write(f"{cheese_hash}\n")
                                
                                if hash_hex == target_hash:
                                    match_found = True
                                    return cheese, salt, enc, hash_hex, match_found


#main function to run the code
if __name__ == "__main__":
    encoding = ["utf-8", "utf-16-le", "utf-16-be", "latin-1", "ascii"]
    target_hash = "b89526eecb7c9ed540613c378c56419c49291a780c34de6e867e914fca7b2a7c"
    
    try:
        cheese, salt, enc, hash_hex, match_found = find_cheese(encoding, target_hash, False)

        # If a match was found, print the cheese, salt, encoding, and hash
        if match_found:
            print(f"Match found! Cheese: {cheese}, Salt: {salt.hex()}, Encoding: {enc}, Hash: {hash_hex}")
        else:
            print("No match found after checking all combinations.")
    except Exception as e:
        print(f"An error occurred: {e}")
