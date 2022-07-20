ext = input("File name: ").strip().lower()
ext = ext.split(".")

if len(ext) == 1:
    print("application/octet-stream")
elif ext[len(ext) - 1] == "gif":
    print("image/gif")
elif ext[len(ext) - 1] in ["jpg", "jpeg"]:
    print("image/jpeg")
elif ext[len(ext) - 1] in ["png"]:
    print("image/png")
elif ext[len(ext) - 1] in ["pdf"]:
    print("application/pdf")
elif ext[len(ext) - 1] in ["txt"]:
    print("text/plain")
elif ext[len(ext) - 1] in ["zip"]:
    print("application/zip")
elif ext[len(ext) - 1] in ["bin"]:
    print("application/octet-stream")
