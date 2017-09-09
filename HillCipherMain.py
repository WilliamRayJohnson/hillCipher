'''
@author William Ray Johnson
9/7/17
'''

import argparse

import Hill

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrpyt a message using Hill Cipher')
    parser.add_argument('-k', required=True, nargs='+', type=int, 
                        help="The key to be used in the cipher. Input in sequence separated by spaces.")
    args = parser.parse_args()
    key = args.k
        
    cipher = Hill.Hill(key)
    
    option = input("Would you like to encrypt or decrypt a message?: ")
    message = input("What is the message you would like to " + option + "?: ")
    
    if option == 'encrypt' or option == 'Encrypt' or option[0] == 'e':
        newMessage = cipher.encrypt(message)
    if option == 'decrypt' or option == 'Decrypt' or option[0] == 'd':
        newMessage = cipher.decrypt(message)
    
    print("Here is your " + option + "ed message:")
    print(newMessage)
    
if __name__ == '__main__':
    main()