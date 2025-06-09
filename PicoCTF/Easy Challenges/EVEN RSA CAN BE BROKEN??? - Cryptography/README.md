**Challenge:** EVEN RSA CAN BE BROKEN???

**Level:** Easy

**Challenge Author:** Michael Crotty

### Description: 
This service provides you an encrypted flag. Can you decrypt it with just N & e?

- webshell: ```nc verbal-sleep.picoctf.net 52407```

### Step-by-Step Walkthrough:
The webshell host gives us N and e and then quits. Connecting additional times provides us with a new value of N and e each time. I'm not as familiar with RSA as I could be, so I relied on Github CoPilot to help me with the steps. I'll provide the steps and attempt to explain what's going on. My variables for this puzzle I used was:

N: 22676125927086140667609347516529909554756457877786909205642696299234458896535525596298160022820418011501793592227590346161977221584544540547913348062440766 

e: 65537

cipher: 9636682935258649179130909110747459727231888165011746758069407739205500025175900947974232789596737805227400882981230970611996750623457231492215973082253413


### What is RSA
RSA (Rivest–Shamir–Adleman) is a widely used public-key cryptographic algorithm that relies on the mathematical properties of large prime numbers. It is used for secure data transmission, digital signatures, and key exchange. RSA encryption works as follows:

#### Key Generation:

Two large prime numbers, p and q, are chosen.
Their product, N = p * q, is calculated. N is called the modulus.
The totient of N, denoted as φ(N), is calculated as (p - 1) * (q - 1).
A public exponent e is chosen such that 1 < e < φ(N) and gcd(e, φ(N)) = 1.
The private key d is computed as the modular multiplicative inverse of e modulo φ(N), i.e., d ≡ e⁻¹ (mod φ(N)).
The public key is (N, e), and the private key is (N, d).

Refer to the "gen_key" function in the attached source code

#### Encryption:

A plaintext message M is converted into an integer m such that 0 ≤ m < N.
The ciphertext c is computed as ```c = m^e mod N```

Refer to the "encrypt" function in the attached source code

#### Decryption:
The ciphertext c is decrypted using the private key d as ```m = c^d mod N```
The original plaintext message M is then recovered from m.

The math behind why this works, is deeper than I intend to go into today, for now, it suffices me to explain this as the process. If you come across this however, I encourage you to become more familiar with prime factorization, modulus arithmetic, etc.. as a lot of common algorithms are based on these concepts

#### Why RSA is Difficult to Decrypt
The security of RSA relies on the difficulty of factoring large integers. Specifically, the challenge lies in deriving the private key d without knowing the prime factors p and q of N. 

If N is chosen poorly, we would be able to determine p and q quite simply and then cracking RSA would be trivial.

#### Mathematical Assumptions:

RSA's security is based on the assumption that no efficient algorithm exists for factoring large integers. While quantum computers could theoretically break RSA using Shor's algorithm, such computers are not yet practical at the required scale.

#### Why RSA Can Be Broken in This Challenge
We mentioned that the process to break the RSA cipher is trivial with a poor choice of N. In this specific challenge, the RSA implementation is flawed because one of the prime factors of N is p = 2, which is trivial to identify. This makes factorization of N extremely easy, allowing the attacker to compute φ(N), derive the private key d, and decrypt the ciphertext. Proper RSA implementations avoid such weaknesses by ensuring that both p and q are large, random, and odd primes.

### Decrypting RSA token
To decrypt the RSA token generated in the current code file, you need the private key ```d```, which is calculated using the formula:

Here, ```p``` and ```q``` are the prime factors of ```N```. Without ```p``` and ```q```, it is computationally infeasible to calculate d directly, as factoring ```N``` is the core difficulty of RSA encryption.

1. Factorize N:

You need to find the prime factors ```p``` and ```q``` of ```N```. This is the hardest part of breaking RSA encryption. If ```N``` is small or poorly generated, you might use tools like YAFU or Msieve to factorize it.

I used native python tools to find the important factors, I'll post my code here

```
from sympy import factorint

N = 22676125927086140667609347516529909554756457877786909205642696299234458896535525596298160022820418011501793592227590346161977221584544540547913348062440766

# Factorize N
factors = factorint(N)
print(factors)  # This will return {p: 1, q: 1} if successful
```

the result returned immediately, and it's not hard to understand why. I'll post the results.

```
p = 2
q = 11338062963543070333804673758264954777378228938893454602821348149617229448267762798149080011410209005750896796113795173080988610792272270273956674031220383
```

As you can imagine, p = 2 is atypical. The factors are supposed to be odd to avoid simple cracking of the RSA cipher. This is the hidden detail that makes this not just possible, but actually very simple


2. Compute φ(N):

```phi = (p - 1) * (q - 1)```

3. Calculate d

```d = inverse(e, phi)```

4. Decrypt the ciphertext

```
plaintext = pow(ciphertext, d, N)
print(long_to_bytes(plaintext).decode('utf-8'))
```

All of the code above was simply generated by github copilot, making it easy to quickly identify the problem and code up a solution. It was even correct the first time ha.

### Notes:
- If N is large and properly generated, factorization is computationally infeasible without significant resources.
- If you cannot factorize N, you cannot decrypt the ciphertext without access to the private key.

<details><summary>Flag</summary>
    <pre>
    picoCTF{tw0_1$_pr!m3605cd50e}
    </pre>
   </details>
