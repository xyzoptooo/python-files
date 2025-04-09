"""
File Handling & Exception Handling Lab
- Reads a file, converts content to uppercase, writes to new file
- Handles FileNotFoundError, PermissionError, and other exceptions
"""

def main():
    print("\n FILE MODIFIER WITH ERROR HANDLING ")
    print("-------------------------------------")

    # Task 1: Get filename from user
    while True:
        input_filename = input("Enter input filename any: ").strip()
        output_filename = "output.txt"  # Default output name

        try:
            # Task 2: Read file and process content
            with open(input_filename, 'r') as infile:
                original_content = infile.read()
                modified_content = original_content.upper()  # Convert to uppercase

            # Task 3: Write to new file
            with open(output_filename, 'w') as outfile:
                outfile.write(modified_content)

            print(f"\n Success! Modified content saved to '{output_filename}'")
            print(f" Stats: {len(original_content.splitlines())} lines processed")

            # Optional: Show preview
            if input("\nShow preview? (y/n): ").lower() == 'y':
                print("\n--- FIRST 3 LINES (MODIFIED) ---")
                print('\n'.join(modified_content.split('\n')[:3]))

            break  # Exit loop if successful

        except FileNotFoundError:
            print(f"\n Error: File '{input_filename}' not found. Please try again.")
        except PermissionError:
            print(f"\n Error: No permission to read/write '{input_filename}'.")
        except UnicodeDecodeError:
            print("\n Error: File is not a text file (try .txt files).")
        except Exception as e:
            print(f"\n Unexpected error: {type(e).__name__} - {str(e)}")

if __name__ == "__main__":
    main()
    # mmm