# Keith Brazill (G00387845)
# 16th March 2020

# Write a program that reads in a text file and outputs the number of e's it contains. 
# The program should take the filename from an argument on the command line.
# Ex: $ python es.py moby-dick.txt
#     116960    

txtfile = str(input("Insert Txt File Name: "))   

with open (txtfile, "r") as myfile:
    data = myfile.read()
    freq = data.count("e")
    print(freq)

# References

# https://docs.python.org/3/tutorial/inputoutput.html
# https://pythonexamples.org/python-count-number-of-words-in-text-file/
# https://pythonexamples.org/python-count-number-of-characters-in-text-file/
# https://docs.python.org/3/library/stdtypes.html#str.count
# https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python
# https://learn.datacamp.com/projects/38
# https://realpython.com/read-write-files-python/
