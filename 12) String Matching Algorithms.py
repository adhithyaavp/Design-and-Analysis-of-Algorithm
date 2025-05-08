def naive_string_match(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            print(f"Pattern found at index {i}")

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
naive_string_match(text, pattern)
