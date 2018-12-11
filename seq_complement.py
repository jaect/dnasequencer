# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:02:10 2018

@author: Josh Jones 
"""
# The following details a DNA sequence and its various complements

seq = input("Enter a DNA sequence consisting of A's, T's, G's, or C's: ")
seq = seq.upper()
for letter in seq:
    if letter != 'A' and letter != 'T' and letter != 'G' and letter != 'C':
        seq = seq.replace(letter, '-')    
        
# Print the length and original sequence  
print("Length of Sequence:", len(seq))
print("Original DNA Sequence: 5`-", seq, "-3`")

# Take and print the complement
complement = []
seq_complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G', '-':'-'}

for letter in seq:
    complement.append(seq_complement[letter])
print("Complement Sequence:   3`-", ''.join(complement), "-5`")

# Take and print the reverse
l = list(seq)
l.reverse()
seq = ''.join(l)
print("Reverse Sequence:      3`-", seq, "-5`")

# Reverse the complement and print
l = list(complement)
l.reverse()
print("Reverse Complement:    5`-", ''.join(l), "-3`")
