"""
Write a function that receives a
List of strings,the function should return a new List that contains
the words that consist of the exact same letters,the order of the words in the
returned List should be like the order of the original.
For example:List = ["pool", "hey", "why", "polo", "pol","ppol", "lopo", "apolo", "hye"]
So the function should return exactly:ret = ['pool', 'hey', 'polo', 'lopo', 'hye']
example ---

typing

anagram -
1. test for empty
2. list with no numbers


steps :
1.  i can parse individual strings in the list , convert it into a dictionary ,
key will be the key as the character , value as the frequency in string

{'p' : 1
 'o' : 2
 'l' : 1
 }
 sets  - {'p','o','l'}
2.
"""
"""
problem to check for anagram : 
1. the length of characters is same - 
2. if the characters are same in 2 strings -  
3. the frequency of characters should be same -  

"""
Vector = list[str]


def check_for_anagram(string_to_compare_1: str, string_to_compare_2: str) -> bool:
    """

    :param string_to_compare_1:
    :param string_to_compare_2:
    :return: True
    """

    if sorted(string_to_compare_1) == sorted(string_to_compare_2):
        return True
    return False


def filter_list_for_anagrams(example_list_to_be_filtered: Vector) -> Vector:
    """
    For example:List = ["pool", "hey", "why", "polo", "pol","ppol", "lopo", "apolo", "hye"]
    So the function should return exactly:ret = ['pool', 'hey', 'polo', 'lopo', 'hye']
    :param example_list_to_be_filtered:
    :return:
    """

    result_list = []

    # for index1,word in enumerate(example_list_to_be_filtered):
    #     if ''.join(sorted(word)) in set_of_list :
    #         result_list.append(word)
    #
    for index1, word1 in enumerate(example_list_to_be_filtered):
        for index2, word2 in enumerate(example_list_to_be_filtered):
            if index1 == index2:
                continue
            if check_for_anagram(word1, word2):
                result_list.append(word1)
                break

    return result_list


if __name__ == '__main__':
    example_list = ["pool", "hey", "why", "polo", "pol", "ppol", "lopo", "apolo", "hye"]
    output = filter_list_for_anagrams(example_list)
    print(output)

    # problem 1 - how to check word for every string in existing list - slice the list
    # problem 2  - if filtered anagram already exists in the loop , it should still append
