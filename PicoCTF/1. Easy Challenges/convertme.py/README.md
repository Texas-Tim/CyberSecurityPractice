**Challenge:** convertme.py

**Level:** Easy

**Challenge Author:** LT 'syreal' Jones

### Description: 
Run the Python script and convert the given number from decimal to binary to get the flag.

### Step-by-Step Walkthrough:

## Learning - What is Binary?
Binary is a number system that uses only two digits: 0 and 1. It is the base-2 numeral system, which computers use to represent and process all data. Each digit in binary is called a bit. In binary, numbers are represented by combinations of 0s and 1s, where each position represents a power of 2, moving right to left.

Each position in a binary string is exponential by the power of 2. For example, to represent `2 to the power of 0 = 1` in a binary string of 8 bits we have:

`00000001`

to represent `2 to the power of 1 = 2` we have a 1 in the second position:

`00000010`

to represent 5 we have a 1 in the third position to represent 4, and a 1 in the first position to represent 1. 4+1=5 and we get:

`00000101`

to represent `2 to the power of 7 = 128` we have a 1 in the eighth position:

`10000000`

and so on. Thus, we can quickly find the correct binary number to represent whatever number the `convertme.py` script provides. My number was `83` and was represented in binary by `1010011`

<details><summary>Flag</summary>
    <pre>
    picoCTF{4ll_y0ur_b4535_722f6b39}
    </pre>
   </details>