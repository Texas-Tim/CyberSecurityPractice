**Challenge:** vault-door-training

**Level:** Easy

**Challenge Author:** Mark E. Haase

### Description: 
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. 

### Step-by-Step Walkthrough:
We are provided with a scenario. Crack the password to the vault to succeed.

The `Java` file provided to us gives us the source code to a password checker, which we can use to deduce the code and test that it works.

## Learning - Java
Java is a high-level, object-oriented programming language designed to be platform-independent, meaning code written in Java can run on any system with a Java Virtual Machine (JVM). Java is widely used for building web applications, mobile apps (especially Android), desktop software, and enterprise systems. It is known for its portability, reliability, and strong community support.

## Investigation - compiling with Java
To run a `Java` program, we first need to compile it. We can do so with:

`javac VaultDoorTraining.java`

We're left with another object, this one we can run with:

`java VaultDoorTraining`

Now we have a working vault door! However, it doesn't do anything to provide us with the password. Luckily, we have access to the source code directly, let's investigate

## Investigation - password authentication
We can see that the password is provided on line 24, but inserting it on its own isn't working. Let's consider the whole code. AhHa! On line 9, it's checking the password with the string base `picoCTF{}`. This makes sense, it's also our flag. 

Input it into the vault door to gain access and then submit it to get credit for this challenge

<details><summary>Flag</summary>
    <pre>
    picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}
    </pre>
   </details>