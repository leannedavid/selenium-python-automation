
#Simple open and read file
file = open('inputFile.txt', 'r')
print(file.read())
file.close()
print("====================================================")


#Read and open file and print only those who have P's
file = open ('inputFile.txt', 'r')
for line in file:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

file.close()
print("====================================================")


#Read and open file and write to new file that separates P's and F's
file = open('inputFile.txt', 'r')
pass_file = open('passFile.txt', 'w')
fail_file = open('failFile.txt', 'w')

for line in file:
    line_split = line.split()
    
    if (line_split[2] == 'P'):
        pass_file.write(line)
    else:
        fail_file.write(line)

file.close()
pass_file.close()
fail_file.close()


