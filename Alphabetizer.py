''' Sorts the characters in a block of text alphabetically '''

def alphabetize(text):
    ''' performs alphabetization '''
    letters = [l for l in list(text) if l.isalpha()]
    sorted_letters = sort(letters)

    text = list(text)
    index = 0
    while index < len(text):
        if text[index].isalpha():
            text[index] = sorted_letters.pop(0)
        index += 1

    return ''.join(text)


def sort(alpha_list):
    ''' orders a list of letters (mixed case) '''
    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < len(alpha_list) - 1:
            if alpha_list[i].lower() > alpha_list[i + 1].lower():
                tmp = alpha_list[i]
                alpha_list[i] = alpha_list[i + 1]
                alpha_list[i + 1] = tmp
                swapped = True
            i += 1
    return alpha_list
