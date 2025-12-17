import secrets
import string
import pyperclip

def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters
    
    if use_numbers:
        characters += string.digits
    
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("--- Custom Password Generator ---")
    
    try:
        length = int(input("Enter password length: "))
        
        if length < 0:
            raise ValueError("Length cannot be a negative number!")
            
        include_nums = input("Include numbers? (y/n): ").lower()
        if include_nums not in ['y', 'n']:
            raise ValueError("Wrong choice! Please enter only 'y' or 'n'!")
            
        include_symbols = input("Include symbols? (y/n): ").lower()
        if include_symbols not in ['y', 'n']:
            raise ValueError("Wrong choice! Please enter only 'y' or 'n'!")
        
        result = generate_password(length, include_nums == 'y', include_symbols == 'y')
        print(f"\nYour Password \x1B[32m{result}\x1B[0m")
        
        pyperclip.copy(result)
        print("\x1B[34m(Password copied to clipboard!) \x1B[0m")
        
        print("------------------------------------")
    
    except ValueError as e:
        print(f"\x1B[31mError: {e}\x1B[0m")
        

if __name__ == "__main__":
    main()