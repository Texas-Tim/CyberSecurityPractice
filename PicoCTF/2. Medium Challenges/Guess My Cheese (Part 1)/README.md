**Challenge:** Guess My Cheese (Part 1)

**Level:** Medium

**Challenge Author:** aditin

### Description: 
Try to decrypt the secret cheese password to prove you're not the imposter!

netcat: `nc verbal-sleep.picoctf.net 49406`

### Step-by-Step Walkthrough:
starting up the instance, we are presented with a story. Guess the encrypted cheese (ie decrypt the message) to prove you're Squeexy. Unfortunately, they only give you three chances. I'm not good enough at game theory and since we don't know the rules, I'm curious if it's even possible to figure this out in three moves, but luckily we can always just restart.

## Investigation - Known Cipher
We are presented with two choices:

1. Guess the name of the encrypted cheese
2. Encrypt a cheese

The game allows us to use `chosen plaintext` to encrypt the value. We can use this to potentially deduce the algorithm and crack the code.

## Learning - Chosen-Plaintext Attack (CPA)
A `Chosen-Plaintext Attack (CPA)` is a model in cryptanalysis where an attacker can choose arbitrary plaintexts, have them encrypted using a secret key or algorithm, and then observe the resulting ciphertexts to gain information about the encryption scheme.

Key aspects of a `CPA`:
* Attacker control over plaintexts:
* The attacker can select specific messages (plaintexts) to be encrypted. 
* Access to corresponding ciphertexts:

## Investigation - Analyzing the cipher
Everytime you log in, you're provided with a random cipher text that's different each time. I tried encrypting a couple of cheeses

* gouda
* cheddar

I noticed that the `d` and the `a` were encrypted exactly the same. I suspect this is going to be a substitution cipher, with each letter being mapped to another letter. If so, we might be able to deduce what the correct phrase is by encrypting the phrase `abcdefghijklmnopqrstuvwxyz` and analyzing the result.

Unfortunately, it seems that we need to input names of actual cheeses. So we need some cheese that uses a lot of letters. Ideally, we could map each letter with only two different cheeses. Although, if we had the letters in the encrypted phrase, we don't need to map "every" letter, just the ones in the phrase. It's worth noting that I tried `cream cheese` next and the space is also part of the encryption, also, the algorithm only accepts certain cheeses so the check-sum list isn't exhaustive. Here's a list of various cheeses, mostly for my own convenience

* gouda
* cheddar
* cream cheese
* monterey jack
* cottage cheese
* wensleydale

After a bit of practice, I was able to net myself the flag, but I believe that I was provided a `ROT cipher` for one of the encryptions. It seems like the encryptions change, not just the number of rotations. My solve ended up being a `ROT 11 cipher`, but reconnecting to the instance again, the cipher had changed and was no longer simply a `ROT cipher`


<details><summary>Flag</summary>
    <pre>
    picoCTF{ChEeSyb3e5eba8}
    </pre>
   </details>