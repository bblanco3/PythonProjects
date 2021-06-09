'''
this file creates 10 folders in the same location this file exists in and has depth 4, in each depth the same ten folders are found, good for hiding personal information
'''

import os



options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
root = os.getcwd()


for letter1 in options:
     for letter2 in options:
          for letter3 in options:
               for letter4 in options:

                    os.makedirs(os.path.join(root, letter1, letter2, letter3, letter4))


