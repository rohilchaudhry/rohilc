# one-by-one

- Namespace: picoctf/18739f24
- ID: one-by-one
- Type: custom
- Category: Binary Exploitation
- Points: 100
- Templatable: yes
- MaxUsers: 50

## Description

I set up this great service! It takes in your input , and prints it out! 
(And maybe some garbage........who cares!)

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The service's binary can be downloaded {{url_for("super_service", "here")}}.

## Hints

- Go Dumpster diving!
- Do you see a pattern somewhere?

## Solution Overview

Get the flag one character at a time, using the OOB read, which get's printedout in the garbage section.

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

To learn how dangerous OOB read can be , and enable you to read into places you are not supposed to be reading from.

## Attributes

- author: Rohil Chaudhry
- organization: 18739D
