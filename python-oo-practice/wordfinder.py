"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """ Find random word from a file
    
    >>> wf = WordFinder("words.txt")
    3 words read
    
    >>>wf.random() in ["ab", "aa"]
    True
    
    """
    
    def __init__(self,file):
        """Reads file and prints # of words in file"""
        
        self.file = file
        
        with open(self.file, "r") as fp:
            num_words = len(fp.readlines())
            print(f"{num_words} words read")
            
    def random_word(self):
        """Chooses a random word to print from file"""
        
        import random
        
        word_list = []
        
        with open(self.file,"r") as fp:
            for word in fp:
                word_list.append(word)
                
        print(random.choice(word_list))

class SpecialWordFinder(WordFinder):
    """Removes blanks lines and comments
    
    >>> swf = SpecialWordFinder("word2.txt")
    10 words read
    
    swf.random() in ["carrot", "lime"]
    """
    
    def parse(self):
        
        with open(self.file, "r") as fp:
            return [word.strip() for word in fp
                    if word.strip() and not word.startswith('#')]
    