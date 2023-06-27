# In pb1.py, create a function that replace_spaces that accepts two inputs:
# A string that represents a sentence
# The punctuation character that will replace the spaces in the sentence
def replace_spaces(sentence, punctuation):
    # Split sentence into words
    words = sentence.split()

    # Iterate through words in the list
    for i in range(len(words)):
        # Check if word ends with a space
        if words[i].endswith(' '):
            # Replace space with given punctuation
            words[i] = words[i].replace(' ', punctuation)

    # Join words into new sentence
    new_sentence = punctuation.join(words)

    return new_sentence


sentence = "Test  This is a test   Testing "
# sentence2 = pb1.replace_spaces(sentence, "_")
# print(sentence2) # -> Test__This_is_a_test__Testing_
