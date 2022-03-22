
print("HTML Table Generator By WBPRO (aka Wülfinger Balázs)\nMade at midnight fueled by power of like 10 energy drinks")

# Tells the generator how many cells in each row
Content = [3,4,5]

# The filename the generators will use
# if you dont add .html it will be automagically append it to the filename
FileName = "Index.html"

# Dont mess with these they are indent levels for the generator
Lv1 = "  "
Lv2 = "      "
Lv3 = "         "


# Automagically append .htm to the filename if not present
if str.lower(".html") in FileName:
    print("[LOG] .html alredy in filename. Leaving it alone.")
else:
    FileName = FileName + ".html"
    print("[LOG] .html is not in filename(you lazy son of a bitch) appending it!")


def WriteHeaders():
    """
    Write proper metadata to the begining of the file.
    """
    # This is ugly as fuck but its 2am what are u gonna do?
    MetaData = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        """
    # Create a Context Manager
    with open(FileName, "w+") as FileHandle:
        FileHandle.write(MetaData)
        GenerateTable(FileHandle, Content)
        FileHandle.close()
        return

def GenerateTable(FileHandle, Content):
    """
    Generate the table in a pretty jank
    yet suprisingly flexible way
    (its 2:30am at this point)
    """
    FileHandle.write("\n")
    FileHandle.write('<table border="2">')
    
    # Generate Markup
    # Theres probably a cleaner implementation but i dont have time
    for rows in Content:

        print(f"[LOG] Writing Row No.{rows}")

        FileHandle.write(f"\n{Lv2}<tr>")
        if Content[0] == rows:
            for i in range(rows):
                print(f"[LOG] Writing header No.{i}")
                FileHandle.write(f"\n{Lv3}<th>PlaceHolder{i}</th>") 
            
            print("[LOG] Writing Header Row Close Tag")
            FileHandle.write(f"\n{Lv2}</tr>")
        
        else:
            for i in range(rows):
                    print(f"[LOG] Writing data tag No.{i}")
                    FileHandle.write(f"\n{Lv3}<td>PlaceHolder{i}</td>") 

    print("[LOG] Writing Table Close Tag")
    FileHandle.write("\n</table>")

    # Return at the end of this mess
    return


def WriteCloseTags(FileHandle):
    """
    Writes body and html close tags to the end of the file
    """
    FileHandle.write("\n</body>")
    FileHandle.write("\n</html>")
    return

def Main():
    WriteHeaders()
    print("[LOG] All Done!")
    return

if __name__ == "__main__":
    # If we are not running as an import call the main function
    Main()

    # if done exit
    print("[LOG] Exiting!")
    exit(0)