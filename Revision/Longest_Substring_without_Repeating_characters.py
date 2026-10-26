def longest_unique_substring(text):
    last_seen = {}
    left = 0
    max_length = 0

    for right in range(len(text)):
        char = text[right]

        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right

        current_length = right - left + 1

        if current_length > max_length:
            max_length = current_length

    return max_length


text = "abcabcbb"
result = longest_unique_substring(text)

print("Input:", text)
print("Longest substring length:", result)