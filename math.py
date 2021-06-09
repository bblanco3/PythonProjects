br = '\n'

def math():
    lst = ['Multiplication', 'Combination', 'Permutation', 'Quadratic Roots', 'Factorials']
    done = False

    
    while not done:

        for item in lst:
            ind = lst.index(item) + 1
            ind = str(ind)
            print(ind + ". " + item)
            
        choice = input('\nWhat would you like to do? ').capitalize()
        choice = int(choice)
        choice -= 1
        
        a = 1
        b = 1
        c = 1
        d = 1
        e = 1

        aa = 0
        bb = 0
        cc = 0
        dd = 0
        ee = 0
        
        ans = 0

            
        #   #   #   #   #   #   #   #   #   #    
        #   #   #   #   #   #   #   #   #   #  
        #   #   #   #   #   #   #   # 
        #   #   #   #   #   #   
        #   #   #   #   #   #
        #   #   #   #
        #   #   #   #
        #   #
        #   #
        

        #Multiplication
        if choice == 0:
            print('n' + lst[choice])
            aa = int(input('Enter a number: '))
            bb = int(input('Enter a number: '))
            ans = aa * bb
            print(ans)


        #   #
        #   #
        #   #   #   #
        #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #


        #   #   #   #   #   #   #   #   #   #    
        #   #   #   #   #   #   #   #   #   #  
        #   #   #   #   #   #   #   # 
        #   #   #   #   #   #   
        #   #   #   #   #   #
        #   #   #   #
        #   #   #   #
        #   #
        #   #

        
        #Combination
        if choice == 1:
            
            print('\n' + lst[choice])
            n = int(input('Enter n: '))
            r = int(input('Enter r: '))
            c = n - r
        
            for num in range(1, n+1):
                a *= num
        
            for num in range(1, c+1):
                d *= num


            ans = a/b*d
            ans = int(ans)
            print(ans)


        #   #
        #   #
        #   #   #   #
        #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #


        #   #   #   #   #   #   #   #   #   #    
        #   #   #   #   #   #   #   #   #   #  
        #   #   #   #   #   #   #   # 
        #   #   #   #   #   #   
        #   #   #   #   #   #
        #   #   #   #
        #   #   #   #
        #   #
        #   #

        
        #Permutation
        if choice == 2:
            
            print('\n' + lst[choice])
            n = int(input('Enter n: '))
            r = int(input('Enter r: '))
            c = n - r
        
            for num in range(1, n+1):
                a *= num
        
            for num in range(1, c+1):
                d *= num


            ans = a/d
            ans = int(ans)
            print(ans)


        #   #
        #   #
        #   #   #   #
        #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #


        #   #   #   #   #   #   #   #   #   #    
        #   #   #   #   #   #   #   #   #   #  
        #   #   #   #   #   #   #   # 
        #   #   #   #   #   #   
        #   #   #   #   #   #
        #   #   #   #
        #   #   #   #
        #   #
        #   #
        

        #Quadratic Roots
        if choice == 3:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))

            k = (b * b) - (4 * a * c)
            k2 = k * -1

            if k >= 0:
                x1 = str((-b + k**.5)/(2 * a))
                x2 = str((-b - k**.5)/(2 * a))
            else:
                x1= str(-b / (2*a)) + " + (" + str(k2**.5) + "i)/" + str(2*a)
                x2= str(-b / (2*a)) + " + (" + str(k2**.5) + "i)/" + str(2*a)

            print("({}, {})".format(x1, x2))


        #   #
        #   #
        #   #   #   #
        #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #


        #   #   #   #   #   #   #   #   #   #    
        #   #   #   #   #   #   #   #   #   #  
        #   #   #   #   #   #   #   # 
        #   #   #   #   #   #   
        #   #   #   #   #   #
        #   #   #   #
        #   #   #   #
        #   #
        #   #
        

        #Factorials
        if choice == 4:
            x = eval(input("Enter a number: "))
            total = x
            for n in range(1, x):
                total *= n

            print("{}! = {}".format(x, total))


        #   #
        #   #
        #   #   #   #
        #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #
        #   #   #   #   #   #   #   #   #   #


        ###########################################################################################################
        #Repeat Statement
        q = input('\nRepeat?[y/n] ')
        if q == 'y':
            print(br*3)
            done = False
        if q == 'n':
            done = True


            
math()
