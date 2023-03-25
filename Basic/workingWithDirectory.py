from pathlib import Path

# absolute path
# for windows c:\program files\microsoft
# for mac /usr/local/bin

# relative path
path = Path("module")
print(path.exists())  # will return true
for file in path.glob("*.*"):  # will print all the file inside module directory
    print(file)

path2 = Path("packages")
print(path2.exists())
for file in path2.glob("*.py"):
    print(file)

new_path = Path("ecommerce")
print(new_path.exists())  # will return false

another_path = Path("emails")
# another_path.mkdir()  # will create a new directory called emails
# another_path.rmdir()  # will remove emails directory


