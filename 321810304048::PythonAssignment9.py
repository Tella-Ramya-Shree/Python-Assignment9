#1.write a python program to read an entire text file
def read(a):
        txt = open(a)
        print(txt.read())
a=input("Enter the file name:")
read(a)
#Output:-
#Enter the file name:myfile01.txt
#Fruits
#Apple
#Banana
#Mango
#Orange

#2.Write a python program to read first n lines of a file
def readfirst(a, n):
        from itertools import islice
        with open(a) as f:
                for l in islice(f,n):
                        print(l,end ='')
a=input("Enter the file name:")
n= int(input("Number of first lines to read:"))
readfirst(a,n)
#Output:
#Enter the file name: myfile1.txt
#Number of first lines to read:3
#Fruits
#Apple
#Banana

#3.Write a Python program to append text to a file and display the text
file=open('myfile01.txt','r')
print('Before appending the text:')
print(file.read())
file=open('myfile01.txt','a')
file.write('Gitam\n')
file.close()
file=open('myfile01.txt','r')
print('After appending the text:')
print(file.read())
#Output:-
#Before appending the text:
#Fruits
#Apple
#Banana
#Mango
#Orange
#After appending the text:
#Fruits
#Apple
#Banana
#Mango
#Orange
#Gitam

#4.Write a Python program to read last n lines of a file
def LastNLines(f,n):
    with open(f) as file:
        print('Last',n,"lines from file:",f)
        for line in (file.readlines() [-n:]):
            print(line, end='')
name=input("Enter the file name:" )
n= int(input("Number of last lines to read:"))
try:
    LastNLines(name,n)
except:
    print("File error....")
#Output:-
#Enter the file name:myfile01.txt
#Number of last lines to read:3
#Mango
#Orange
#Gitam

#5.Write a Python program to read a file line by line store it into a variable
def read(a):
        with open (a) as file:
                cse=file.readlines()
                print(cse)
a=input("Enter the file name:")
read(a)
#Output:-
#Enter the file name:myfile01.txt
#['Fruits\n', 'Apple\n','Banana\n', 'Mango\n','Orange\n','Gitam\n']

#6.Write a Python program to read a file line by line and store it into a list
def read(a):
        with open(a) as file:     
                list = file.readlines()
                print(list)
a=input("Enter the file name:")
read(a)
#Output:-
#Enter the file name:myfile01.txt
#['Fruits\n', 'Apple\n','Banana\n',Mango\n','Orange\n','Gitam\n']