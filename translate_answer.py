def translate_answer(s, answer_index):
    value = (answer_index % 31) + 1  # Derives the XOR key
    decoded_string = ""
    for i in range(0, len(s), 2):
        code = int(s[i:i + 2], 16)  # Convert hex to integer
        decoded_string += chr(code ^ value)  # XOR and convert to character
    return decoded_string


# Example usage:
ans_map = ['55', '44', '47', '46', '46', '42', '45', '4e', '48', '4e']  # Encoded answers
for index, encoded_answer in enumerate(ans_map):
    decoded_answer = translate_answer(encoded_answer, index)
    print(f"Question {index + 1}: {decoded_answer}")
