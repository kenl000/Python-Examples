
try:
   # f = open('testfile.txt')
    kl =po
except FileNotFoundError:
    print('The file does not exist.')
except Exception as e:
    print('There is a problem', e )
finally:
    print('The file is closed.')    