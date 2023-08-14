import os

def MassRenamer():
    path = input("[ENTER THE PATH] : ")
    i = 0
    
    renameType = input(">>> Would you like to keep the original name along with the numbering? (Y/N) \n > ")
        
    if renameType == "Y" or renameType == "y":
        original_name = True
    elif renameType == "N" or renameType == "n":
        original_name = False

    if os.path.isdir(path):
        print("[DX] Directory Found!")
        extension = input(">>> Enter the File extension you would like to be sorted : ")
        filenames = os.listdir(path)
        

        for files in filenames:
            print(files)
            ext = files.split(".")
            extl = ext[len(ext) - 1]
            fname = ext[0:len(ext)-1]

            if original_name == False:
                source = path + "\\" + files
                dest = path + "\\" + str(i) + "." + extl
            elif original_name == True:
                source = path + "\\" + files
                dest = path + "\\" + str(i) +"-" + "".join(fname) + "." + extl

            if extl == extension and fname not in ext:
                os.rename(source,dest)
                i = i + 1
                print(f"[DX] Successfully renamed {files} ")

            else:
                print(f"[DX] Passed {files} as the extension is not .{extension}")



    elif not os.path.isdir(path):
        print("[DX] Directory not found! Please check the path!")

    else:
        print("[DX] An Unexpected error occurred! Please contact the Developer (Yuki/DrasteX/Tushar Whatever you call me) to resolve this issue!")

MassRenamer()

def Exit():
    Exit = input("\n Press Enter to Exit OR Input 'r' to use the program again!")
Exit()

if Exit == 'r':
    MassRenamer()
    Exit()
