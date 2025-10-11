import sys
from bidict import bidict

# Implement character replacement from
# Crack the Code: the History of Spy Codes and Ciphers, pg. 17
symbol_dict = bidict(
    {
        "a": "!",
        "b": "@",
        "c": "#",
        "d": "$",
        "e": "%",
        "f": "^",
        "g": "&",
        "h": "*",
        "i": "(",
        "j": ")",
        "k": "_",
        "l": "+",
        "m": "{",
        "n": "}",
        "o": "|",
        "p": "\\",
        "q": ":",
        "r": ";",
        "s": "\'",
        "t": '\"',
        "u": "<",
        "v": ">",
        "w": "`",
        "x": "/",
        "y": "?",
        "z": "~",
    }
)


def symbol_replace(text):
    """
    Replace symbols with letters and vis-versa based on a defined list. Right now the function
    assumes that the text passed will be decodable.

    Args:
        text (string): string of text or symbols to be encoded/decoded

    Returns:
        string: the encoded or decoded message
    """

    result = ""

    for char in text:
        # Only shift alphabetic characters
        if char.isalpha():
            # convert char to symbol
            symbol_temp = symbol_dict[char.lower()]

            result += str(symbol_temp)
        else:
            # Keep non-alphabetic characters unchanged
            result += symbol_dict.inverse[char]

    return result


def main():
    # Check if the right number of arguments have been passed
    # if len(sys.argv) != 2:
    #     print("The text to decode/encode must be passed")
    #     sys.exit(1)

    text = input("enter text to be encoded/decoded: ")

    # text = fr"{sys.argv[1]}"

    # Process the text and display the result
    result = symbol_replace(text)
    print(f"Original: {text}")
    print(f"Result:   {result}")


if __name__ == "__main__":
    main()
