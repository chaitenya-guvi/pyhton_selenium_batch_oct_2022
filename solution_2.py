# For example:List = ["pool", "hey", "why", "polo", "pol","ppol", "lopo", "apolo", "hye"]
# So the function should return exactly:ret = ['pool', 'hey', 'polo', 'lopo', 'hye']

input_list = ["pool", "hey", "why", "polo", "pol", "ppol", "lopo", "apolo", "hye"]
# ['pool', 'hey', 'polo', 'lopo', 'hye']

Vector = list[str]


def frequency_of_words(list_of_words: Vector) -> dict:
    """

    :param list_of_words: list of strings
    :return: dictionary with frequency of string in list as values
    """
    frequency_count = {}
    for word in list_of_words:
        if word in frequency_count:
            frequency_count[word] += 1
        else:
            frequency_count[word] = 1

    return frequency_count


def filter_anagram_in_list(example_list_to_be_filtered: Vector) -> Vector:
    """
    :param example_list_toyu
    5
    """
    list_of_words = [''.join(sorted(word)) for word in example_list_to_be_filtered]

    frequency_count = frequency_of_words(list_of_words)

    output_list = []
    for index, word in enumerate(list_of_words):
        if frequency_count[word] >= 2 and word in list_of_words:
            output_list.append(input_list[index])

    return output_list


if __name__ == '__main__':
    example_list = ["pool", "hey", "why", "polo", "pol", "ppol", "lopo", "apolo", "hye"]
    output = filter_anagram_in_list(example_list)
    print(output)
