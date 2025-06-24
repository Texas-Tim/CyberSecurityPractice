**Challenge:** Rust fixme 2

**Level:** Easy

**Challenge Author:** Taylor McCampbell

### Description: 
The Rust saga continues? I ask you, can I borrow that, pleeeeeaaaasseeeee?

### Step-by-Step Walkthrough:
Once again, we approach Rust, a language with which I have 0 experience! Let's dive in.

## Investigation - Rust
1. error[E0596]: cannot borrow `*borrowed_string` as mutable, as it is behind a `&` reference
 --> src/main.rs:9:5

```
borrowed_string.push_str("PARTY FOUL! Here is your flag: ");
^^^^^^^^^^^^^^^ `borrowed_string` is a `&` reference, so the data it refers to cannot be borrowed as mutable
```

Looks like it doesn't like the `&`, a little research tells me that this is an immutable reference (immutable means unchangable, while mutable means changable). We need to make this a mutable reference with `&mut`.

This took me a couple of tries, there were three lines that needed to be changed. Following the errors allowed me to track down the lines and the correct syntax. You can refer to the "fixed" main to view my solution

<details><summary>Flag</summary>
    <pre>
    picoCTF{4r3_y0u_h4v1n5_fun_y31?}
    </pre>
   </details>