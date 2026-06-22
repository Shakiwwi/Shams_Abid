# mUser is prompted to enter the name of a file, and the program will determine the media type of the file based on its extension.
type= input("enter the name of you file: ").strip().lower()

# match statement is used to check the file extension and print the media type of the file
match type:
    case type.endswith(".gif"):
        print("file's media type is image/.gif")
    case type.endswith(".jpg"):
        print("file's media type is image/.jpg")
    case type.endswith(".jpeg"):
        print("file's media type is image/.jpeg")
    case type.endswith(".png"):
        print("file's media type is image/.png")
    case type.endswith(".pdf"):
        print("file's media type is .pdf")
    case type.endswith(".txt"):
        print("file's media type is .txt")
    case type.endswith(".zip"):
        print("file's media type is .zip")
    case _:
        print("file's media type is application/octet-stream")

#application/octet-stream is outputed is the file type is not recognized
