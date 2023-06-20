from Rename import *

r = Rename()

#Get files
while True:
    path = input("Enter folder path: ")
    try:
        r.SelectFiles(path)
    except TooManyExtensions as TME:
        print("TOO MANY EXTENSIONS FOUND", TME.ext)
        continue
    except (FileNotFoundError,OSError):
        print("NO FILES FOUND")
        continue
    break

#Display Files
print("Files:")
for file in r.full_file_names:
    print("\t" + file)
print()

#Choose option
while (True):
    option = input("Enter option number:\n\t(0) Cancel\n\t(1) Replace text\n\t(2) Add text\n\t(3) Format text\n\t(4) Change extension\nEnter number: ")
    if (option == "1"):

        find = input("Enter text to find: ")
        replace = input("Enter text to replace it with: ")
        r.ReplaceText(find, replace)

    elif (option == "2"):

        text = input("Enter the text you wish to add: ")
        placeBool = True
        while (True):
            placement = input("Do you fish to add text at start (1) or at end (2)?\n:\t")
            if (placement == "1"):
                placeBool = True
            elif (placement == "2"):
                placeBool = False
            else:
                print("Incorrect option")
                continue
            break
        r.AddText(text, placeBool)

    elif (option == "3"):

        text = input("Enter the text you wish to format to: ")
        starting_number = int(input("Starting number: "))
        r.FormatText(text, starting_number)

    elif (option == "4"):

        new_ext = input("Enter the new extension: ")
        r.ChangeExt(new_ext)

    elif (option == "0"):

        print("Exiting program")
        quit()
        break

    else:

        print("\nINCORRECT OPTION")
        continue

    break


#Preview changes
preview = input("Do you wish to preview the changes? (Y/N)\n:")
while True:
    if (preview.lower() == "y"):
        r.Preview()
    elif (preview.lower() == "n"):
        break
    else:
        preview = input("Incorrect option! (Y/N):\n:")
        continue
    break

#Commit changes
commit = input("\nDo you wish to commit these changes? (Y/N)\n:")
while True:
    if (commit.lower() == "y"):
        try:
            r.Commit()
            print("Done :)")
        except DuplicationError:
            print("Two or more files share the same new name")

    elif (commit.lower() == "n"):
        break
    else:
        commit = input("Incorrect option! (Y/N):\n:")
        continue
    break


#Revert changes
revert = input("\nDo you wish to revert these changes? (Y/N)\n:")
while True:
    if (revert.lower() == "y"):
        r.Revert()
        print("Done :)")

    elif (revert.lower() == "n"):
        break
    else:
        revert = input("Incorrect option! (Y/N):\n:")
        continue
    break

