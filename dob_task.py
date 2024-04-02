file_lines = [] #array holding each lines of the file

with open('DOB.txt', 'r+') as file:
    for var_line in file:
        file_lines.append(var_line.strip()) #Using .split() method to remove \n in the array

full_name = []  #array holding first and last name e.g ("Orville Wright")
dob = [] #array holding dob e.g ("20 October 1988")

for line in file_lines:
    parts = line.split() #Split each line into full name and DOB
    full_name.append(' '.join(parts[:-3])) #Full name is first and last name combined
    dob.append(' '.join(parts[-3:])) #DOB is the last three parts joined together

print("Name")
counter = -1
for name in range(0,len(full_name)):    #for loop to print out full_name[]
    counter += 1
    full_name_element = full_name[counter]
    print(full_name_element)

print("\n")

print("Birthdate")
counter = -1
for dob_loop in range(0,len(dob)):  #for loop to print out dob[]
    counter += 1
    dob_element = dob[counter]
    print(dob_element)
