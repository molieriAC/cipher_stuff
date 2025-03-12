import itertools


def encode_transposition(plaintext, num_columns):
    # Remove spaces from the plaintext
    plaintext = plaintext.replace(" ", "")
    ciphertext = [""] * num_columns

    # Distribute characters across columns
    for idx, char in enumerate(plaintext):
        column = idx % num_columns
        ciphertext[column] += char

    # Combine columns to form the ciphertext
    return "".join(ciphertext)


def decrypt_transposition(ciphertext, num_columns):
    # Remove spaces from ciphertext if they exist
    ciphertext = ciphertext.replace(" ", "")
    ciphertext_length = len(ciphertext)
    num_rows = ciphertext_length // num_columns

    # Ensure we account for short columns
    short_columns = num_columns - (ciphertext_length % num_columns)

    # Generate all possible column orders (permutations)
    column_orders = list(itertools.permutations(range(num_columns)))

    for order in column_orders:
        # Create an empty grid
        grid = [""] * num_columns
        idx = 0

        # Fill the columns in the given order
        for col_num in range(num_columns):
            if col_num >= short_columns:
                grid[order[col_num]] = ciphertext[idx : idx + num_rows + 1]
                idx += num_rows + 1
            else:
                grid[order[col_num]] = ciphertext[idx : idx + num_rows]
                idx += num_rows

        # Read across rows to reconstruct the plaintext
        plaintext = ""
        for row in range(num_rows + 1):
            for col in range(num_columns):
                if row < len(grid[col]):
                    plaintext += grid[col][row]

        # Check if the reconstructed plaintext is meaningful
        # For simplicity, we just print all possibilities here
        print(f"Trying order {order}: {plaintext}")


def main():
    # Example usage
    input_text = input(
        "please enter coded text: "
    )  # "Ihgaurmny" # Replace with your encoded message
    num_columns = int(
        input("how many columns?: ")
    )  # 3 # Replace with the number of columns you suspect
    encode_decode = input("(e)ncode or (d)ecode the message: ")

    if encode_decode in ("encode", "e"):
        print(encode_transposition(input_text, num_columns))
    else:
        print(decrypt_transposition(input_text, num_columns))


if __name__ == "__main__":
    main()
