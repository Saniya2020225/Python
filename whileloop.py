# count = 1
# while count <= 5:
#   print("Count is :", count)
#  count = count + 1
# print("loop ended")

while True:
    command = input(">>>")
    print(command)
   # if (command == "quit" or command == "QUIT"):
    if (command.lower() == "quit"):
        break
