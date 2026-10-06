"""
Dieses Programm soll zeigen wie arg parse funktioniert.

Beim aufrufen der Datei muss man noch einen parameter geben
"""

import argparse


def say_hello(args):
    if args.name:

        print(f'Hallo {args.name.capitalize()}!')
    else:
        print('Hallo unbekannter')




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')

    args = parser.parse_args()

    say_hello(args)



if __name__ == "__main__":
    main()