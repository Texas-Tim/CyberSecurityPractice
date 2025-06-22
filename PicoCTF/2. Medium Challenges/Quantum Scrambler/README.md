**Challenge:** Quantum Scrambler

**Level:** Medium

**Challenge Author:** Michael Crotty

### Description: 
We invented a new cypher that uses "quantum entanglement" to encode the flag. Do you have what it takes to decode it?

netcat: `nc verbal-sleep.picoctf.net 54825`

### Step-by-Step Walkthrough:
Connecting to our instance, we immediately see a large collection of random hex values in various stages of lists. We'll quickly save it to a local file as it will likely come in handy later. 

## Investigation - Scrambler
Next, we look at our `quantum_scrambler.py` file. The code is a bit confusing at first glance, but it's small, so that's a plus. The flag text gets inserted into an encompassing list, then put through a scrambler, which seems to append a bunch of lists to the main list. Each character will be represented by some sort of hex value in the list somewhere. 

That's about as far as we can go for now, so let's move on. Since we have access to the source code for the scrambler, we can perform what's called a `known plaintext attack`. 

## Learning - Known Plaintext Attack (KPA)
A known-plaintext attack (KPA) is a type of cryptanalysis where the attacker has access to both the plaintext and its corresponding ciphertext. This allows the attacker to analyze the relationship between the two to potentially deduce the encryption key or the algorithm's weaknesses. 

To run the cipher, just create a local `flag.txt` file and put some text in there. We'll keep it simple with a `p` for now, then slowly add more characters as we build the text `password`. Running the file through the scrambler each time may help us understand more about how to reverse it.

## Investigation - Reverse Engineering
Performing this method, we see an interesting pattern start to emerge. Each index of the encompassing main list is another list. This secondary list has a hex character that represents the next character of the flag in the first index, then a list, then the last index represents the next character of the flag. This should be simple to reverse engineer. Just iterate through the indexes of the main list, grab the first and last values, append to a new list, then convert from hex to text.

Hint, the saved cipher text is likely a string, not a list, but it would be very difficult to transform it using `list`. Use the command `eval` to first transform it to a `list` object quickly then work on reverse engineering it

#### Note
There was something else strange going on, and the final result had the flag repeated twice. But I was able to print the flag before my code errored out. I'm not going to bother fixing it any further and just submit the flag


<details><summary>Flag</summary>
    <pre>
    picoCTF{python_is_weird63e6d9bb}
    </pre>
   </details>