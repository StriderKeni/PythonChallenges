#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    list_names = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        if bool(re.match(r"(^|\s)([a-zA-Z]+@gmail.com){1,50}", emailID)) and bool(re.match(r"^([a-z+]){1,20}", firstName)):
            list_names.append(firstName)

    list_names.sort()
    print('\n'.join(list_names))