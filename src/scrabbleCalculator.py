def calculate_scrabble_score(word):
    letter_scores = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
        'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
        'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
        'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
        'U': 4, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
        'Z': 10
    }

    def get_letter_score(char):
        return letter_scores[char.upper()]

    total_score = 0
    word_multiplier = 1
    is_seven_letter_word = len(word.replace('*', '').replace('**', '').replace('^', '')) == 7

    i = 0
    while i < len(word):
        char = word[i]
        
        if char.isalpha():
            score = get_letter_score(char)
            total_score += score
            
            if i + 1 < len(word) and word[i + 1] == '*':
                total_score += score
                i += 1
            elif i + 1 < len(word) and word[i + 1] == '*':
                total_score += score * 2
                i += 1

        i += 1

    if word.endswith('d'):
        total_score *= 2
    elif word.endswith('t'):
        total_score *= 3

    if is_seven_letter_word:
        total_score += 50

    return total_score

print(calculate_scrabble_score("HEELLO"))       
print(calculate_scrabble_score("HEEELLO"))      
print(calculate_scrabble_score("CHALLENGE"))    
print(calculate_scrabble_score("EASY"))          
print(calculate_scrabble_score("CODE"))          
print(calculate_scrabble_score("BYE"))           