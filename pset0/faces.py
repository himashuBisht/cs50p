input = input("").split()
emojis = {
    ":)": "🙂",
    ":(": "🙁"
}

result = ""
for word in input:

    result +=emojis.get(word,word) + " "
#get(word,word) will match word other wise default value of word
print(result.strip())
