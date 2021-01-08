# importing modules


from random import randrange
import argparse
import sys
import os 
# we export the OS module in python provides functions for interacting with the operating system. 




def generator (parent_directory):




    '''
    
     with the function generator we can generate files also the prefixes, suffixs and pads

     Parameters:
                    
                    parent_directory 
    Returns:
       '''         
    # Parent Directory path 




    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)
    

    i = 0
    f = os.path.join(parent_directory, '0000')

    while os.path.exists(f):
        i += 1
        f = os.path.join(parent_directory, str(i).rjust(4, '0'))    
    os.makedirs(f) 
    #If there is no file we create 0000 file 

    for index in range(0, 100):
       

        name = os.path.join(f, str(index).rjust(2, '0'))
        f1, f2, f3 = name+'p.txt', name+'c.txt', name+'s.txt'
        
        f_1 = open(f1, "a")
        f_2 = open(f2, "a")
        f_3 = open(f3, "a")

        #For  F1 and F3 we use 48 caracters.
        for n in range(0,48):
            f_1.write(bin(randrange(255))[2:].rjust(8, '0'))
            f_3.write(bin(randrange(255))[2:].rjust(8, '0'))
        #For  F2 we use 2000 caracters.
         for n in range(0,2000):   
            f_2.write(bin(randrange(255))[2:].rjust(8, '0'))
        

        f_1.close()
        f_2.close()
        f_3.close()

generator('generate mode')






def get_the_available_pads (directory):
    

    '''
    with this function we get the pad available to encode
            
            Parameters:
                    directory: only the directory which contain pads folders
            
            Returns:
                     the pad available to encode
                     the path of prefix available to encode
                     the path of suffix available to encode
    '''


    ps = os.path.join(directory, '0000')
    a = 0
    b= 0
    while not os.path.exists(ps):
        a += 1
        ps = os.path.join(directory, str(a).rjust(4, '0'))
    p = os.path.join(ps, '00c.txt')
    while not os.path.exists(p): 
        b += 1
        p = os.path.join(ps, str(b).rjust(2, '0')+'c.txt') 
    prefix = os.path.join(ps, str(b).rjust(2, '0')+'p.txt') 
    suffix = os.path.join(ps, str(b).rjust(2, '0')+'s.txt') 
    print('on utulise',p)
    return p, prefix, suffix

