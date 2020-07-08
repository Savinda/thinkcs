def cleanword(s):
    """Clean-out word punctuations and all"""
    from string import punctuation
    new_string = ""
    for letter in s:
        if letter not in punctuation:
            new_string.join(letter)
            new_string += letter
    return new_string

def has_dashdash(s):
    """Check whether the string have -- in it, and return true if yes"""
    ch = "--"
    if ch in s:
        return True
    else:
        return False
    
def extract_words(s):
    """Extract words from a string without punctuation and split if word contain --"""
    from string import punctuation
    new_string = ""
    if has_dashdash:
        s = s.replace("--", " ")
    for letter in s:
        if letter not in punctuation:
            new_string.join(letter)
            new_string += letter.lower()
    return new_string.split()
        
    
def wordcount(word, s):
    """Count number of occurences of word in string s"""
    count = 0
    for i in s:
        if i == word:
            count += 1
    return count

def wordset(l):
    """Return unique words in the given list"""
    result = []
    i = 0
    while i < len(l):
        if l[i] not in result:
            result += [l[i]]
        i += 1
    return sorted(result)
      
def longestword(l):
    """Find a longest item's length in a given list"""
    i = 0
    max_now = 0
    while i < len(l):
        if max_now < len(l[i]):
            max_now = len(l[i])
        i += 1
    return max_now