def input_lines():
    print("Enter text here: ")
    lines = []

    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    return " ".join(lines)

def plain_text(text):
    text = text.lower()
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.replace("!","")
    text = text.replace("?","")
    return text

def main():
    text = input_lines()
    clean_text = plain_text(text)

    print("\nClean Text: ")
    print(clean_text)

if __name__ == "__main__":
    main()