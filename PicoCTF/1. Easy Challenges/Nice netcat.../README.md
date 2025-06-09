**Challenge:** Nice netcat...

**Level:** Easy

**Challenge Author:** syreal

### Description: 
There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 7449, but it doesn't speak English...

### Step-by-Step Walkthrough:
connecting to the instance, we get lines of numbers. After attempting to connect multiple times, they do not seem random:
```
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
102 
50 
100 
55 
99 
97 
102 
97 
125 
10
```

The numbers are most likely in ASCII. For the life of me, I could not make a CLI tool work for me. I poked around the internet and saw a lot of solutions that utilized the command `chr(int(i))` which definitely would work. I just pasted into Copilot for fast translation.

<details><summary>Flag</summary>
    <pre>
    picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
    </pre>
   </details>