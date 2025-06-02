**Challenge:** binhexa

**Level:** Easy

**Challenge Author:** Nana Ama Atombo-Sackey

### Description: 
How well can you perfom basic binary operations?

### Step-by-Step Walkthrough:

#### Binary Operations
This task tests your knowledge of six binary operations. The standard operations for binary are as follows:

```
- AND (&): Each bit is compared; result is 1 if both bits are 1.

- OR (|): Each bit is compared; result is 1 if at least one bit is 1.

- Left Shift (<<): Shifts bits to the left, adding zeros on the right.

- Right Shift (>>): Shifts bits to the right, discarding bits on the right.

- Multiply (*): Binary Multiplication is performed in the same manner as decimal numbers are multiplied.

- Addition (+): Binary addition involves adding two numbers using only the digits 0 and 1. It follows similar rules to decimal addition, but with carrying over when the sum of two digits exceeds 1
```

The running instance provides you with two random binary numbers. We will be working with the following:

```
Binary Number 1: 01110100
Binary Number 2: 10100111
```

#### Question 1/6
Operation 1: '<<'
Perform a left shift of Binary Number 1 by 1 bits.

<details><summary>result</summary>
    <pre>
    11101000
    </pre>
   </details>
Enter the binary result: 11101000


#### Question 2/6
Operation 2: '|'
Perform the operation on Binary Number 1&2.

<details><summary>result</summary>
    <pre>
    11110111
    </pre>
   </details>

#### Question 3/6
Operation 3: '>>'
Perform a right shift of Binary Number 2 by 1 bits.

<details><summary>result</summary>
    <pre>
    01010011
    </pre>
   </details>

#### Question 4/6
Operation 4: '&'
Perform the operation on Binary Number 1&2.

<details><summary>result</summary>
    <pre>
    00100100
    </pre>
   </details>

#### Question 5/6
Operation 5: '*'
Perform the operation on Binary Number 1&2

<details><summary>result</summary>
    <pre>
    100101110101100
    </pre>
   </details>

#### Question 6/6
Operation 6: '+'
Perform the operation on Binary Number 1&2.

<details><summary>result</summary>
    <pre>
    100011011
    </pre>
   </details>

#### Transform to Hex
Enter the results of the last operation in hexadecimal:

<details><summary>result</summary>
    <pre>
    0x11B
    </pre>
   </details>


<details><summary>Flag</summary>
    <pre>
    picoCTF{b1tw^3se_0p3eR@tI0n_su33essFuL_d6f8047e}
    </pre>
   </details>