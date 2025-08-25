# This is a simple program that asks for user input and prints a message\
name = input("What is your name ? ")
name = name.capitalize().title() # Capitalize the first letter of the name 
name = name.strip() # Remove any leading or trailing spaces
# We can also use name = name.lower().capitalize() to achieve the same result

age  = input("How old are you ? ")

job = input("what is your job ? ")
job = job.lower() # Convert the job to lowercase
job = job.strip() # Remove any leading or trailing spaces

ProLang = input("What is your favourite programming language ? ")
ProLang = ProLang.upper() # Convert the programming language to uppercase
ProLang = ProLang.strip() # Remove any leading or trailing spaces

#The end parameter is used to avoid a new line and the f string is used to format the string
print (f"{name} is", job + " and he is", age, end=" ") 
print ("years old, he loves to code in", ProLang)
