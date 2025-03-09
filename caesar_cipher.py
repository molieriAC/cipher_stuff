#!/usr/bin/env python3
import sys

def caesar_cipher(direction, shift, text):
    """
    Performs a Caesar cipher based on the given text.
    
    Args:
        direction (str): Either 'forward' to encrypt or 'back' to decrypt.
        shift (int): How many positions to shift the letters (0-25).
        text (str): The text to encrypt or decrypt.
        
    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    
    # If decoding, we reverse the shift direction
    if direction.lower() in ('back', 'b'):
        shift = -shift
    
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
    # Check if we have the right number of arguments
    if len(sys.argv) != 4:
        print("Usage: python cipher.py <forward|back> <shift_value> <text>")
        print("  <forward|back>: Specify a direction '(f)orward' or '(b)ack'.")
        print("  <shift_value>: A number from 0 to 25 specifying the shift amount")
        print("  <text>: The text to process")
        sys.exit(1)
    
    # Parse command line arguments
    direction = sys.argv[1]
    if direction.lower() not in ['forward', 'f', 'back', 'b']:
        print("Error: First argument must specify a direction '(f)orward' or '(b)ack'")
        sys.exit(1)
    
    try:
        shift = int(sys.argv[2])
        if not (0 <= shift <= 25):
            raise ValueError("Shift value must be between 0 and 25")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    text = sys.argv[3]
    
    # Process the text and display the result
    result = caesar_cipher(direction, shift, text)
    print(f"Original: {text}")
    print(f"Result:   {result}")

if __name__ == "__main__":
    main()
