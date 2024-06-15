from typing import List

def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])



def count_words(data)->int:
    """
    Returns the number of words encoded in data. You may assume
    data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> count_words(data)
    6
    """
    count = 0
    
    # if there is nothing in the dictionary, return 0
    if data == None:
        return 0
    
    # iterate over the keys in the dictionary
    for key in data:  
        # if the current key represents a word
        if data[key][1]:
            count += 1
        # recursively count words in the subtrie
        count += count_words(data[key][0])
    return count



def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. You may
    assume data is a valid trie.

    >>> data = {}
    >>> insert(data, "tree")
    >>> insert(data, "trie")
    >>> insert(data, "try")
    >>> insert(data, "trying")
    
    >>> contains(data, "try")
    True
    >>> contains(data, "trying")
    True
    >>> contains(data, "the")
    False
    """
    # if the input string is empty, return True
    if s == '':
        return True

    # if the first character if the input string is in the dictionary
    if s[0] in data:
        # recursively check if the next character of the input string is in the dictionary
        return contains(data[s[0]][0], s[1:])
    return False



def height(data)->int:
    """
    Returns the length of longest word encoded in data. You may
    assume that data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> height(data)
    11
    """
    max_height = 0

    # if there is nothing in the dictionary, return 0
    if data == None:
        return 0

    # iterate through each key-value in the dictionary
    for key, value in data.items():
        # recursively calculate the height of the subtries and update the max height
        max_height = max(max_height, 1 + height(value[0]))
    return max_height



def count_from_prefix(data, prefix: str)-> int:
    """
    Returns the number of words in data which starts with the string
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professional")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> count_from_prefix(data, 'pro')
    5
    """
    # if the input string is empty, return the number of words in the dictionary
    if prefix == '':
        return count_words(data)

    # if there is nothing in the dictionary, return 0
    if data == None:
        return 0

    # iterate over the keys in the dictionary
    for key in data:
        # if the first character of the prefix matches the current key, recursively count the words that begin with the prefix
        if key == prefix[0]:
            return count_from_prefix(data[key][0], prefix[1:])
    return 0
    


def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professional")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> get_suggestions(data, "progr")
    ['program', 'programming', 'programmer', 'programmers']
    """
    words = []
    
    # if there is nothing in the dictionary, return an empty list
    if data == None:
        return []
    
    # traverse the trie until the prefix is found or no more nodes are available
    node = data
    for char in prefix:
        if char in node:
            # move to the next node
            node = node[char][0]
        else:
            return []
    
    # collect all words starting with the prefix
    collect_words(node, prefix, words)
    
    return words

def collect_words(node, word, words):
    if node == None:
        return
    
    for char in node:
        # check if it's the end of a word
        if node[char][1]:
            words.append(word + char)
        collect_words(node[char][0], word + char, words)
