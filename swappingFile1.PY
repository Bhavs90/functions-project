def swap():
    fileName1 = input("enter the file name:-  ")
    fileName2 = input("enter the file name:-  ")
    with open (fileName1,'r') as data_a:
        strA = data_a.read()

    with open (fileName2,"r") as data_b:
        strB = data_b.read()

    with open (fileName1,"w") as data_a:  
        data_a.write(strB)  

    with open (fileName2,"w" ) as data_b:
        data_b.write(strA)          

swap()         
