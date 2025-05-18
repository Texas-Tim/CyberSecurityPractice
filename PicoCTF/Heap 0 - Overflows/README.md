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

if we take a look at the downloadable `chall.c` file and look at the main function and take a closer look at our Print Flag case. Within, it prints the 

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



<details><summary>Flag</summary>
    <pre>
    picoCTF{}
    </pre>
   </details>