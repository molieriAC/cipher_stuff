import sys
# add the symbol_dict if needed later
# from symbol_replacements import symbol_dict

# TODO: Implement brute force decoding if the key is not present


def caesar_cipher(shift, text):
    """
    Performs a Caesar cipher based on the given text.

    Args:
        shift (int): How many positions to shift the letters (-25 to 25).
            Making the number negative shifts backward (commonly used to decode).
        text (str): The text to encrypt or decrypt.

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""

    for char in text:
        # Only shift alphabetic characters
        if char.isalpha():
            # Determine ASCII offset (97 for lowercase, 65 for uppercase)
            ascii_offset = 97 if char.islower() else 65

            # Apply the shift using modulo to wrap around the alphabet
            shifted = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result += chr(shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result


def main():
    # Check if the right number of arguments have been passed
    if len(sys.argv) != 3:
        print("Usage: python cipher.py <shift_value> <text>")
        print(
            """<shift_value>: A number from -25 to 25 specifying the shift amount.
            Negative numbers indicate a shift backward"""
        )
        print("  <text>: The text to process")
        sys.exit(1)

    try:
        shift = int(sys.argv[1])
        if not (-25 <= shift <= 25):
            raise ValueError("Shift value must be between -25 and 25")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    text = sys.argv[2]

    # Process the text and display the result
    result = caesar_cipher(shift, text)
    print(f"Original: {text}")
    print(f"Result:   {result}")


if __name__ == "__main__":
    main()
