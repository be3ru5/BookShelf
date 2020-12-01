#!/usr/bin/python3

# used object names: book_name mod2txt c action n edit_book book_txt book_list to_show random_line reading 
# used object names: random_book line

import os
import random

# reading existing data
path = './.books'
book_list = list(os.listdir(path))

# display book list
def display_list():
    path = './.books'
    files = os.listdir(path)
    n=1
    for f in files:
        print(f'{n}. '+f)
        n += 1

# adding new book 
def create_book():
    # print('new book')
    print()
    print('[#] Adding new book to the bookshelf :*')
    print()
    try:
        book_name = str(input('[+] book name: '))
        mod2txt = book_name + '.txt'
        # mod2txt = '.' + book_name + '.txt'
        try:
             c = open('./.books/'+mod2txt,'x') # c for create
        except FileExistsError:
            print('[-] Error: book already exists :/')
        except:
            print('[-] Something went wrong :/')
    except:
        print('\n[-] Something went wrong :/')

# adding notes to book
def add_txt(book_list):
    print()
    print('Type "HELP" to see your shelf OR')
    edit_book = str(input('[+] Enter book name to add line: ')).lower()
    book_txt = edit_book+'.txt'
    if book_txt in book_list:
        a = open('./.books/'+book_txt,'a')
        print('[+] Write your note:')
        line = str(input('> '))
        a.write('> '+line+'\n')
        print(f'[*] Note added to {edit_book}')
    elif book_txt == 'help.txt':
        print(book_list)
    else:
        print('book doesn\'t exist')
        exit()

# random line show
def read_random(book_list):
    random_book = random.choice(book_list)
    print("<> BOOK: "+random_book)
    print('<> LINE:')
    reading=open("./.books/"+random_book, "r")
    to_show = reading.readlines()
    random_line = random.choice(to_show)
    print(random_line)

# choosing what to do ... 
def action_taker(): 
    # action to take
    print('> 1. display books')
    print('> 2. Add new book')
    print('> 3. Add notes to book')
    print('> 4. Display random line')
    print('> 5. Exit program')
    print()
    # choosed action
    action = str(input('[+] choose your action: '))   
    if action=='1':
        display_list()
    elif action=='2':
        create_book()
    elif action=='3':
        add_txt(book_list)
    elif action=='4':
        read_random(book_list)
    elif action=='5':
        print('[*] Exting Program .....')
        exit()
    else:
        print('[-] You choosed wrong option')
        exit()

print()
action_taker()
print()