**Challenge:** Pachinko

**Level:** Medium

**Challenge Author:** notdeghost

### Description: 
History has failed us, but no matter.

There are two flags in this challenge. Submit flag one here, and flag two in Pachinko Revisited.

### Step-by-Step Walkthrough:
Upon opening the webpage, you are greeted by a website with various nodes and interactive elements and the title `NAND Simulator`

#### Investigation
All good web page vulnerability inspections will generally comprise of two things:

1. Using the Web Page Inspector
2. Testing all the interactive elements

Let's open up an inspector panel and look at the source element. Although I don't see anything that immediately jumps out, let's check out the `NAND Simulator`. 

#### Learning - NAND
NAND stands for "Not AND" and is a basic logic gate in digital electronics. It outputs false (0) only when all its inputs are true (1); otherwise, it outputs true (1). In other words, it is the opposite of the AND gate.

Truth table:
```
Input A	Input B	NAND Output
0	0	1
0	1	1
1	0	1
1	1	0
```

NAND gates are fundamental in digital circuits and can be combined to create any other logic gate or digital function.

Checking out the board, we have 8 nodes. Nodes `1-4` are "target nodes" while Nodes `5-8` are "intermediate nodes". You can add as many additional intermediate nodes as you wish and connect intermediate nodes to any other nodes, but each node can only have up to two incoming connections. Target nodes can be connected to, but cannot be a source, that is it cannot connect to other nodes itself.

We are given very little information about what the task is, so let's look at the source code that was provided a little more.

#### Investigation - Source Code
The `index.js` file has some promising results. In order for us to obtain the flag, we need to return a result of `0x1337`. Most other results will be `0x3333`, but how do I know what result I'm returning?

Looking a little further up in the code, we have `result = memory[0x1000] | (memory[0x1001] << 8);`

Everything depends on our memory then, which is an input to the current function `doRun`.

`doRun` is only called twice. Once for the admin, presumably when setting up the server, and once for a `/check` which is the path we see in `index.html` on the main webpage. 

In the `doRun` function, there's one function call that stands out. `serializeCircuit`, which can be found in the `utils.js` file. Let's go look there next

I've run into a brick wall. Without understanding the end goal (something to do with NAND I'm sure), I'm going to use Burp for further investigation

Burp let's me better visualize what's occurring, with the submitted `json` file. Each node allows two connections incoming, with the gate not showing up unless there are at least two incoming connections. This is consistent with NAND, as the gate takes two connections and outputs based on the incoming values. The JSON value in the `POST` to `/check` includes the gate numbers as values, but I don't see a submission of the `0 or 1` I mentioned.

#### Investigation - Confusion
Honestly, I just played around with the UI and randomly got the flag. The UI doesn't seem consistent, as near as I can tell. The nodes seem to have random values of `0,1` assigned to them and the output doesn't seem to follow the `NAND` rules. Consider this an unsatisfying conclusion.

A big note, I went online and found some tutorials. Someone introduced this tool to me

`objdump -b binary -m i386:x86-64 -D nand_checker.bin`

which yields the following:

```
nand_checker.bin:     file format binary


Disassembly of section .data:

0000000000000000 <.data>:
   0:   4d 00 00                rex.WRB add %r8b,(%r8)
   3:   30 5d 00                xor    %bl,0x0(%rbp)
   6:   00 10                   add    %dl,(%rax)
   8:   6d                      insl   (%dx),%es:(%rdi)
   9:   00 00                   add    %al,(%rax)
   b:   20 08                   and    %cl,(%rax)
   d:   00 01                   add    %al,(%rcx)
   f:   04 2d                   add    $0x2d,%al
  11:   00 00                   add    %al,(%rax)
  13:   10 1b                   adc    %bl,(%rbx)
  15:   00 04 02                add    %al,(%rdx,%rax,1)
  18:   1c 22                   sbb    $0x22,%al
  1a:   17                      (bad)
  1b:   12 1c 4c                adc    (%rsp,%rcx,2),%bl
  1e:   18 00                   sbb    %al,(%rax)
  20:   1c 14                   sbb    $0x14,%al
  22:   0b 04 44                or     (%rsp,%rax,2),%eax
  25:   02 1b                   add    (%rbx),%bl
  27:   04 44                   add    $0x44,%al
  29:   02 2b                   add    (%rbx),%ch
  2b:   04 44                   add    $0x44,%al
  2d:   02 0c 4c                add    (%rsp,%rcx,2),%cl
  30:   1c 4c                   sbb    $0x4c,%al
  32:   2c 4c                   sub    $0x4c,%al
  34:   01 00                   add    %eax,(%rax)
  36:   11 01                   adc    %eax,(%rcx)
  38:   21 02                   and    %eax,(%rdx)
  3a:   01 06                   add    %eax,(%rsi)
  3c:   11 06                   adc    %eax,(%rsi)
  3e:   21 06                   and    %eax,(%rsi)
  40:   0b 00                   or     (%rax),%eax
  42:   1b 01                   sbb    (%rcx),%eax
  44:   06                      (bad)
  45:   01 29                   add    %ebp,(%rcx)
  47:   00 78 00                add    %bh,0x0(%rax)
  4a:   7c 22                   jl     0x6e
  4c:   0b 05 1d 00 ff ff       or     -0xffe3(%rip),%eax        # 0xffffffffffff006f
  52:   28 02                   sub    %al,(%rdx)
  54:   78 00                   js     0x56
  56:   51                      push   %rcx
  57:   02 61 02                add    0x2(%rcx),%ah
  5a:   3b 05 4b 06 37 73       cmp    0x7337064b(%rip),%eax        # 0x733706ab
  60:   47 74 31                rex.RXB je 0x94
  63:   04 3c                   add    $0x3c,%al
  65:   6c                      insb   (%dx),%es:(%rdi)
  66:   37                      (bad)
  67:   32 3c 6c                xor    (%rsp,%rbp,2),%bh
  6a:   7c 72                   jl     0xde
  6c:   01 01                   add    %eax,(%rcx)
  6e:   0c 7e                   or     $0x7e,%al
  70:   7c 56                   jl     0xc8
  72:   0d 00 33 33 5d          or     $0x5d333300,%eax
  77:   00 00                   add    %al,(%rax)
  79:   10 59 00                adc    %bl,0x0(%rcx)
  7c:   0f 00 0d 00 37 13 5d    str    0x5d133700(%rip)        # 0x5d133783
  83:   00 00                   add    %al,(%rax)
  85:   10 59 00                adc    %bl,0x0(%rcx)
  88:   0f                      .byte 0xf
  ```

  This is the checksum for the flag, but I can't deduce anything except that line `7c` has the `1337` we are looking for. and line `72` has the `3333` that otherwise gets submitted.

  Finally, all the tutorials I watched had folks resubmitting the same answer over and over until they got lucky and received the flag. This is not a good puzzle solution in my opinion

<details><summary>Flag</summary>
    <pre>
    picoCTF{p4ch1nk0_f146_0n3_e947b9d7}
    </pre>
   </details>