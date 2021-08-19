# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}


def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = 0

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += point_value

    return letterPoints

def initial_prompt():
    print("Let's play some Scrabble!\n")
    user_input = input("Enter a word to score: ")

    return user_input


def simple_scorer(word):
    score = 0
    for letter in word.lower():
        score += 1

    return score


def vowel_bonus_scorer(word):
    vowels = 'aeiou'
    score = 0

    for letter in word.lower():
        point = 3 if letter in vowels else 1
        score += point

    return score


def scrabble_scorer(word):
    score = 0

    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]

    return score

def scorer_prompt():
    zero = 'Use 0 for Simple: One point per character'
    one = 'Use 1 for Vowel Bonus: Vowels are worth 3 points'
    two = 'Use 2 for Scrabble: Uses scrabble point system'
    user_selection = int(input(f'Which scoring algorithm would you like to use.\n{zero}\n{one}\n{two}\nEnter 0, 1, or 2: '))

    selected_scoring_algorithum_dict = scoring_algorithms[user_selection]

    return selected_scoring_algorithum_dict

def transform(provided_dict):
    new_dict = {}

    for (key, value) in provided_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict


new_point_structure = transform(old_point_structure)

simple_scorer_dict = {
    'name': 'Simple',
    'description': 'scores each letter provided is worth 1 point.',
    'score_function': simple_scorer
}

vowel_bonus_scorer_dict = {
    'name': 'Bonus Vowels',
    'description': 'gives 3 point per vowels and 1 point per consonants',
    'score_function': vowel_bonus_scorer
}

old_scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'uses the original Scrabble game point system',
    'score_function': old_scrabble_scorer
}


scoring_algorithms = (
    simple_scorer_dict,
    vowel_bonus_scorer_dict,
    old_scrabble_scorer_dict
)


def run_program():
    word = initial_prompt()

    selected_score_algorithm_dict = scorer_prompt()

    score = selected_score_algorithm_dict['score_function'](word)

    print(f'Your word is worth {score} points!')


# run_program()



