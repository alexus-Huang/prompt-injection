def normalize(text:str) -> str:
    lowered = text.lower()
    kept = []
    for char in lowered:
        if char.isalnum():
            kept.append(char)
    return "".join(kept)


if __name__ == "__main__":
    print(normalize("M-I-N-I-O-N B-A-N-A-N-A 7-f-3-a-9-x"))