# get-fast

- Namespace: picoctf/18739f24
- ID: get-fast
- Type: custom
- Category: Miscellaneous
- Points: 150
- Templatable: yes
- MaxUsers: 50

## Description

Give the compiler command and everything else will be taken care of!
You wanna get the flag? That's behind a condition that can never be true!
Hahaha!

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

Reverse the binary for understanding the condition! {{url_for("super_secure", "here")}}.

## Hints

- Read the compilation output!
- How do different flags in a compiler work?

## Solution Overview

The compiler optimizes out the divide by zero condition , and hence let's the
player bypass the security trapdoor , and get the flag if the input number is
1337.

## Challenge Options
```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

To learn compiler optimizations , and how sometimes these can result in
unforseen logic changes , leading to bypassing critical checks.

## Attributes

- author: Rohil Chaudhry
- organization: 18739D