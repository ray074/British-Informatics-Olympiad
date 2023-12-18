def countWords(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            content = content.split()
            return len(content)
    
    except FileNotFoundError:
        return None
    
    
def main():
    file = input("Name of file for word count? ")
    count = countWords(file)
    
    if count is not None:
        print(f"\nThe file {file} contains {count} words.")
    else:
        print(f"\n{file} is not a valid file.")
        
    
if __name__ == "__main__":
    main()
