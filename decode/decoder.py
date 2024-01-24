def decode(message_file):
    # Read the file line by line
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Initialize an empty list to store the words in each line
    words = []

    # Loop through the lines and extract the words
    for line in lines:
        num, word = line.strip().split()
        words.append((int(num), word))

    # Initialize an empty list to store the words in the decoded message
    decoded_words = []

    # Loop through the words and add them to the decoded message
    # based on their position in the pyramid structure
    for i in range(len(words)):
        for j in range (words[i][0]):
            decoded_words.append(words[-i-1][1])
            if len(decoded_words) == sum(word[0] for word in words):
                break
        if len(decoded_words) == sum(word[0] for word in words):
            break

    # Return the decoded message as a string
    return ' '.join(decoded_words)
