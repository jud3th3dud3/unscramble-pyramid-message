# defines the unscramble function
def unscramble(message_text):
    with open(message_text, 'r') as file:
        lines = file.readlines()
    
    # seperates numbs and words
    entries = [line.strip().split() for line in lines]
    entries = [(int(num), word) for num, word in entries]
    
    # sorts by number
    entries.sort()
    
    # sets variables and array for loop
    pyramid_lines = []
    unscrambled_words = []
    current_number = 1
    next_line_start = 1
    line_length = 1
    
    # creates the pyramid
    while next_line_start <= len(entries):
        end_of_line = next_line_start + line_length - 1
        line_words = [entries[i-1][1] for i in range(next_line_start, end_of_line + 1)]
        pyramid_lines.append(line_words)
        if end_of_line <= len(entries):
            unscrambled_words.append(entries[end_of_line - 1][1])
        next_line_start = end_of_line + 1
        line_length += 1
    
    # Print the pyramid structure
    print("Pyramid Structure:")
    for line in pyramid_lines:
        print(' '.join(line))

    # joins end of line words
    unscrambled_message = ' '.join(unscrambled_words)
    return unscrambled_message

# finds txt file and prints the unscrambled message
if __name__ == "__main__":
    message = unscramble('message.txt')
    print("\nDecoded Message:")
    print(message)