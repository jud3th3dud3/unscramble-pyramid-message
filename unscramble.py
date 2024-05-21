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
    unscrambled_words = []
    current_number = 1
    next_line_start = 1
    line_length = 1
    
    # creates the pyramid
    while next_line_start <= len(entries):
        end_of_line = next_line_start + line_length - 1
        if end_of_line <= len(entries):
            unscrambled_words.append(entries[end_of_line - 1][1])
        next_line_start = end_of_line + 1
        line_length += 1
    
    # joins end of line words
    unscrambled_message = ' '.join(unscrambled_words)
    return unscrambled_message

# finds txt file and prints the unscrambled message
if __name__ == "__main__":
    message = unscramble('message.txt')
    print(message)