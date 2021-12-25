# read only by default (mode= "r")
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# write to the file
# if the file doesn't exist, it will create the file
with open("my_file.txt", mode="w") as file:
    file.write("Hello World.")

# append to the file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
