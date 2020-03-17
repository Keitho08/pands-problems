# Keith Brazill (G00387845)
# 16th March 2020

# Write a program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line.
# Ex: $ python es.py moby-dick.txt
#     116960    

txtfile = str(input("Insert Txt File Name: "))   # the user is prompted to enter name of txt file as string

with open (txtfile, "r") as myfile:              # opens text file as myfile in read mode
    data = myfile.read()                         # data is equal to the text read in inserted file  
    freq = data.count("e")                       # freq is equal to count of "e" contained in inserted file
    print(freq)                                  # prints freq i.e. number of e's answer = 116960 for Moby Dick

# References

# https://docs.python.org/3/tutorial/inputoutput.html
# https://pythonexamples.org/python-count-number-of-words-in-text-file/
# https://pythonexamples.org/python-count-number-of-characters-in-text-file/
# https://docs.python.org/3/library/stdtypes.html#str.count
# https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python
# https://learn.datacamp.com/projects/38
# https://realpython.com/read-write-files-python/
# Version of Moby Dick text file used: https://www.gutenberg.org/files/2701/old/moby10b.txt 