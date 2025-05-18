**Challenge:** heap 0

**Level:** Easy

**Challenge Author:** Abrxs, pr1or1tyQ

### Description

Are overflows just a stack concern?

### Step-by-Step Walkthrough
Our first step should be to recognize the title of the challenge as usual. `Heap` is a term that refers to memory allocation and is a region of a program's memory used for dynamic memory allocation. It is managed by the operating system or the runtime environment and allows programs to allocate and free memory at runtime using functions like malloc and free in C, or new and delete in C++.

Key Characteristics of the Heap:
- Dynamic Allocation:

- Memory is allocated and deallocated explicitly by the programmer during runtime.
Global Access:

- Memory allocated on the heap is accessible from anywhere in the program, as long as you have a pointer to it.

- Memory on the heap persists until it is explicitly freed by the programmer. If not freed, it can lead to memory leaks.
Slower than Stack:

- Accessing heap memory is slower than stack memory because it involves more complex memory management.

- Unlike the stack, which has a fixed size, the heap can grow or shrink as needed (only limited by system memory)


For this challenge, our first step is to connect to the provided instance. We immediately notice 5 options:

1. Print Heap:          (print the current state of the heap - affected by your input from 2)
2. Write to buffer:     (write to your own personal block of data on the heap)
3. Print safe_var:      (I'll even let you look at my variable on the heap, I'm confident it can't be modified - likely have to modify it by taking advantage of overflow)
4. Print Flag:          (Try to print the flag, good luck)
5. Exit

if we take a look at the downloadable `chall.c` file and look at the main function and take a closer look at our Print Flag case. Within, it prints the `check_win()` function.

```
void check_win() {
    if (strcmp(safe_var, "bico") != 0) {
        printf("\nYOU WIN\n");

        // Print flag
        char buf[FLAGSIZE_MAX];
        FILE *fd = fopen("flag.txt", "r");
        fgets(buf, FLAGSIZE_MAX, fd);
        printf("%s\n", buf);
        fflush(stdout);

        exit(0);
    } else {
        printf("Looks like everything is still secure!\n");
        printf("\nNo flage for you :(\n");
        fflush(stdout);
    }
}
```
The first line has us using a string compare function: `strcmp()`, which compares two strings character by character. If the strings are equal, the function returns 0.

Our task is clear, overflow the heap using the only memory manipulation we have at our disposal. The task thankfully allows us to write to the buffer. Note that:

Overflowing the heap refers to writing more data into a dynamically allocated memory region (on the heap) than it was allocated to hold. This can overwrite adjacent memory, corrupting data or control structures, and potentially leading to unintended behavior or security vulnerabilities.

Using `Write to buffer`, we are allowed to affect the heap. Heap, unlike the Stack, allows us to dynamically allocate memory and it is not Last in First out or LIFO. The memory can be edited freely, assuming you have permissions. Thus, we must overflow the buffer address `0x57b7c305b2b0` in order to affect the addresses around it, specifically the address of our safe_var: `0x57b7c305b2d0`. 

Our next step must be to understand the distance between these two memory addresses. Memory addresses are represnted in Hex, so finding the difference is as simple as finding the difference in Hex values. You can learn Hex math which uses base 16, or you can use an online calculator such as: `https://www.calculator.net/hex-calculator.html`. The function we must perform is: `0x57b7c305b2d0 - 0x57b7c305b2b0 = 0x20`. `0x20` is 32 bytes.



#### Solution
Now we know the distance, our next goal should be to attempt to overflow the memory by 32 bytes. By putting in 32 bytes worth of characters, we can affect the memory address of the `safe_var`: `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`

To check that our solution worked, we can use option 1 to print the heap. We can see that the safe_var has been modified and confidently print the flag!


<details><summary>Flag</summary>
    <pre>
    picoCTF{my_first_heap_overflow_c3935a08}
    </pre>
   </details>