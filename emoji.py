def emoji_converter():
    message = input(">")
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞",
    }
    outcome = " "
    for word in words:
        outcome = outcome + emojis.get(word, word) + " "
    return outcome

print(emoji_converter())