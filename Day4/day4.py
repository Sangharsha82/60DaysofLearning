import json

file = open("user.txt", "r")
content = file.read()
print(content)
file.close()

# write() — overwrites file content (mode "w" creates if not found)
file = open("user.txt", "w")
file.write("name: Sangharsha\n")
file.write("age: 22\n")
file.close()

# Append without overwriting — use mode "a"
file = open("user.txt", "a")
file.write("city: Kathmandu\n")
file.close()

# "with" automatically closes the file even if an error occurs

# Reading
with open("user.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed here ✓

# Writing
with open("user.txt", "w") as file:
    file.write("name: Sangharsha\n")
    file.write("age: 22\n")

    import json

# json.load()  → reads from a FILE OBJECT → returns Python dict/list
with open("config.json", "r") as f:
    data = json.load(f)
print(data["name"])   # Sangharsha



with open("config.json", "w") as f:
    json.dump(data, f, indent=4)