#!/usr/bin/env python
import pprint

message = 'abs wefws abad aew abe eses weqf'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
pprint.pprint(count)
