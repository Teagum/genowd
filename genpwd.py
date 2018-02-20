#!/usr/bin/env python3

import argparse
import random
import secrets
import string
import sys

bad_chars = ['"', "'", '`', '\\']

def main():
    parser = argparse.ArgumentParser(description='Generate passwords.')
    parser.add_argument('length', metavar='N', type=int,
                        help='Lengh of password.')
    
    args = parser.parse_args()

    base = ''
    base += string.ascii_letters
    base += string.digits
    punct = list(string.punctuation)
    for bc in bad_chars: punct.remove(bc)
    print(punct)
    punct = ''.join(punct)
    base += punct
    
    pwd = ''.join(secrets.choice(base) for i in range(args.length))
    print(pwd)
    

if __name__ == '__main__':
    sys.exit(main())

