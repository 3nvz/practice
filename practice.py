
chars = set()
count = 0

while True:
    char = input("Enter a character: ")

    if char in chars or len(char) > 1:
        print(f"Number of unique characters entered: {count}")
        break

    chars.add(char)
    count += 1