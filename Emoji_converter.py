
welcome_message = print("Welcome to an Dami's Emoji Converter")
message = input("Enter your characters: ")

# if message == ":)" or message == ":(":
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞",
    }
    outcome = " "
    for word in words:
        outcome += emojis.get(word, word) + " "
    return outcome
# else:
#     print("Please enter a character between ':)' and '(:' ")

print(emoji_converter(message))