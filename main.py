#!/bin/env python3

import sys
#import os
import dataclasses

##### CONSTANTS ###############

##### directories #############

ROOT_DIRECTORY='.'

##### directories ^^^^^^^^^^^^^

##### CONSTANTS ^^^^^^^^^^^^^^^

##### IO FUNCTIONS ############

def eprint(*args, sep=' ', end='\n', flush=False):
    print(*args, sep=sep, end=end, flush=flush, file=sys.stderr)

##### IO FUNCTIONS ^^^^^^^^^^^^

##### GLOBAL MUTABLE ##########

##### GLOBAL MUTABLE ^^^^^^^^^^

##### LANGUAGE ################

##### base language ###########

@dataclasses.dataclass
class Language(object):
    pass

@dataclasses.dataclass
class EnglishLanguage(Language):
    no_subcommand: str = 'no subcommand provided'
    unknown_subcommand: str = 'unknown subcommand'

DEFAULT_LANGUAGE: Language = EnglishLanguage

##### base language ^^^^^^^^^^^

##### language examples #######

@dataclasses.dataclass
class RussianLanguage(DEFAULT_LANGUAGE):
    no_subcommand: str = 'нет подкомманды'
    unknown_subcommand: str = 'неизвестная подкомманда'

##### language examples ^^^^^^^

##### current language ########

current_language: Language = EnglishLanguage

##### current language ^^^^^^^^

##### LANGUAGE ^^^^^^^^^^^^^^^^

def file_to_string(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()

def cla():
    print(f'argc is {len(sys.argv)}')
    print(f'argv is {sys.argv}')
    if (True or len(sys.argv) < 2):
        eprint(current_language.no_subcommand)
    eprint(current_language.unknown_subcommand)

def main():
    cla()

if __name__ == '__main__':
    main()
