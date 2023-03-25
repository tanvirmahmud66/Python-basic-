massage = input(">")
print(massage)
words = massage.split(" ")
print(words)

emoji = {
    ":)": "🙂",
    ":(": "😞",
    ":D": "😀",
    ":E": "😡"
}
output = ""
for each_word in massage:
    output += emoji.get(each_word, each_word)

print(output)