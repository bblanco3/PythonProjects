def create():
    doc = ""
    name = ""
    head = ""
    br = "\n"
    code = []
    attr = []
    text = ""


    
    #Getting file name & extension
    fileName = input("Enter the desired css file name: ")
    fileExt = input("Enter the desides file extension: ")
    doc = fileName + "." + fileExt
    print(br)
    print("Currently editing: " + doc)

    print("-" * 25)
    print("Enter '@' where you wish to have the itirated items appear.")
    print("Example: width1, width2, width3 would be width@")


    
    #Get Class Name
    print(br)
    name = input("Enter the desired class name: ")
    head = "." + name + "{"



    
    #Code
    print(br)
    print("Enter lines for the class, when done, type 'DONE'")
    
    while True:
        line = input("Enter code for a line: ")

        if line == "DONE":
            break
        else:
            code.append(line)



        
    #Range of integers or list of attributes
    print(br)
    iti = input("Itirate through range of integers or list of attributes? ")
    iti = iti.lower()
    
    #Code for a range of integers
    if iti == "integers":
        n1 = eval(input("From: "))
        n2 = eval(input("To: "))

        for num in range(n1, (n2+1)):
            text += head.replace('@', str(num)) + "\n"
            for line in code:
                text += "  " + line.replace('@', str(num)) + "\n"
            text += "}\n"
                

    #Code for a list of attributes
    if iti == "attributes":

        print("Enter values, when done, type DONE")
        while True:
            a = input("Enter an attribute: ")

            if a == "DONE":
                break
            else:
                attr.append(a)

 
        for item in attr:
            text += head.replace('@', item) + "\n"
            for line in code:
                text += "  " + line.replace('@', item) + "\n"
            text += "}\n"
            
    text += "\n\n\n\n\n"
    file = open(doc, "a")
    file.write(text)
    file.close()

create()
            

