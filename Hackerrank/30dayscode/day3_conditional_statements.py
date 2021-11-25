#!/bin/python3

import math
import os
import random
import re
import sys

'''
Objective
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an integer, , perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not N is weird. (pedaço de código usado para 
substituir algumas outras funcionalidades de programação. Um stub pode simular o comportamento de um código existente 
ou ser um substituto temporário para o código ainda a ser desenvolvido)

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0'''

if __name__ == '__main__':
    N = int(input().strip())

    if N % 2 != 0:
        print("Weird")
    if N % 2 == 0 and 2 <= N <= 5:
        print("Not Weird")
    if N % 2 == 0 and 6 <= N <= 20:
        print("Weird")
    if N % 2 == 0 and N > 20:
        print("Not Weird")




