import argparse

parser = argparse.ArgumentParser()

try:
    parser.add_argument('--username')

    parser.add_argument('--password', type=int)

    args = parser.parse_args()
    if args.username == 'elia' and args.password == 123:
        print('erfolgreich' )
        
    else:
        print('Passwort oder Benutzername falsch')

    
except:
    print("ungültige eingabe(test.py --username <elia> --password <123>)")

