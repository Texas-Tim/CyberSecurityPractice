**Challenge:** Ph4nt0m 1ntrud3r

**Level:** Easy

**Challenge Author:** Prince Niyonshuti N.

### Description

A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.
To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!

### Step-by-Step Walkthrough
First things first, download the file, open up Wireshark and let's start investigating the PCAP. I've never used Wireshark before, so I'll be stumbling around a lot. Feel free to jump to x for an explanation once I figure things out

The first thing I notice is that one of the files has Illegal Segments. Let's look closer at that one. It's being flagged as an "out of order" segment. I see 2 "reassembled" segments, Frame 1 and Frame 9. I suspect these two are linked somehow. 

If the data is broken somehow, the TCP can be analyzed, but decrypting it only shows me the "reassambled TCP" which matches the window on the right. So that's a dead end. But, that data looks like base64 encoding. Since I know very little of investigating PCAP files, I have no idea if this is abnormal, or if its the right track, but let's explore

packet9: `cGljb0NURg==` translated is `picoCTF`

This must mean we are on the right track! However, a fair warning. 

#### Warning: 
In reality, the first few packets I tried to translate was gibberish. I spent a lot of time going down rabbit holes before coming back to this. I did not find the above value the first time, probably because of a spelling error. Anyways, always explore the abnormalities first, it may save you a lot of time!

#### Solution:
Translating Packet 1 gives me `_89` and some undecipherable characters. This might be useful, but lets only look at the packets that have come "after" our abnormality for now.

Packet 21: `ezF0X3c0cw==` = `{1t_w4s`
Packet 17: `bnRfdGg0dA==` = `nt_th4t`
Packet 15: `XzM0c3lfdA==` = `_34sy_t`
Packet 20: `YmhfNHJfOA==` = `bh_4r_8`
Packet 13: `TEwZTgzOQ==` = `e10e839`
Packet 08: `fQ==` = `}`

Be careful when translating it over, Base64 can be very picky.

Putting it all together, we get our flag!

<details><summary>Flag</summary>
    <pre>
    picoCTF{1t_w4snt_th4t_34sy_tbh_4r_8e10e839}
    </pre>
   </details>