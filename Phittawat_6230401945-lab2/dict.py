directory = {"Jane Doe": "+27 555 5367", "John Smith": "+27 555 6254",
             "Bob Stone": "+27 555 5689"}
directory["Jane Doe"] = "+27 555 1024"
directory.update({"Anna Cooper": "+27 555 3237"})
print(directory.get("Bob Stone"))
if directory.get("Bob Stone") is not None:
    print(directory.get("Bob Stone"))
else:
    print("Bob Stone is not in the directory!")
print(directory.keys())
print(directory.values())