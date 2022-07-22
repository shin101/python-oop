"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder: 
    def __init__(self, path):
        file = open(path,'r')
        self.words = self.parse(file)
        
        print(f'{len(self.words)} words read')
    
    def parse(self,file):
        return [word.strip() for word in file]

    def random(self):
        return(random.choice(self.words))

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("subclasswords.txt")
    4 words read

    >>> swf.random() in ["kale", "apple", "parsnips", "mango"]
    True

    >>> swf.random() in ["kale", "apple", "parsnips", "mango"]
    True

    >>> swf.random() in ["kale", "apple", "parsnips", "mango"]
    True

    >>> swf.random() in ["kale", "apple", "parsnips", "mango"]
    True

    """
    def parse(self,file):

        return [word.strip() for word in file if word.strip() and not word.startswith('#')]






# >>> wf = WordFinder("words.txt")
# # 3 words read

# >>> wf.random()
# 'cat'

# >>> wf.random()
# 'cat'

# >>> wf.random()
# 'porcupine'

# >>> wf.random()
# 'dog'