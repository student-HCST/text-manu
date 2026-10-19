from pathlib import Path

# Input aur output file ke naam
input_file = Path("data.txt")
output_file = Path("output.txt")

try:
    # Step 1: Text file ko read karein
    with input_file.open("r", encoding="utf-8") as file:
        text = file.read()

    # Step 2: Check karein ki file khaali hai ya nahi
    if not text.strip():
        print("File khaali hai.")

    else:
        # Step 3: Text ko process karein
        lines = text.splitlines()
        words = text.split()
        characters = len(text)

        # Step 4: Statistics print karein
        print("----- File Analysis -----")
        print("Total lines:", len(lines))
        print("Total words:", len(words))
        print("Total characters:", characters)

        # Step 5: Har line ko uppercase karein
        processed_text = text.upper()

        # Step 6: Processed data ko nayi file mein save karein
        with output_file.open("w", encoding="utf-8") as file:
            file.write(processed_text)

        print("\nProcessed data output.txt mein save ho gaya.")
        print("\nProcessed text:")
        print(processed_text)

except FileNotFoundError:
    print("Error: data.txt file nahi mili.")

except UnicodeDecodeError:
    print("Error: File ka encoding sahi nahi hai.")

except OSError as error:
    print("File error:", error)
