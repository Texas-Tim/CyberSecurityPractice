**Challenge:** The Numbers

**Level:** Easy

**Challenge Author:** Danny

### Description: 
The numbers... what do they mean?

### Step-by-Step Walkthrough:
These numbers seem pretty familiar, if the list of numbers are all less than 26, it's likely going to be encoded with a substitution cipher.

#### Learning - Substitution Cipher
A substitution cipher is a type of encryption where each letter or symbol in the plaintext is replaced with another letter or symbol according to a fixed system. The mapping is one-to-one, meaning each character in the original message is always replaced by the same character in the ciphertext. Common examples include the Caesar cipher and monoalphabetic substitution ciphers.

In this case, the characters are simply the letters of the alphabet. Online has some quick tools, or we can simply use `unicode` to quickly convert the numbers into their character form.

#### Action

first, make a list of the numbers in the image, there's no simple method to extract, so you'll have to write them down:

`numbers=[16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]`

Then, for each number, convert from their unicode value using `chr`:

`letters = [chr(n + 96) for n in numbers]  # 97 is 'a'`

Next, print them, joining each of the letters to an empty string:

`print(''.join(letters))  # Output: 'abc'`

Voila! I discovered from this challenge, that the submission is actually not case sensitive, but I changed the result just because it looks better

<details><summary>Flag</summary>
    <pre>
    picoCTF{thenumbersmason}
    </pre>
   </details>