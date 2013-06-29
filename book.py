class Book(object):
    """The book that is currenty playing"""


    def __init__(self):
        """Initialize"""

        self.book_id = None
        self.volume = 1
        self.elapsed = .0


    def reset(self):
        """Reset progress"""

        self.__init__()

    def set_progress(self, progress):
        """Set progess from db result"""

        if progress:
            self.part = progress[1]
            self.elapsed = progress[2]

    def is_playing(self):
        """returns if we have a current book"""
        return self.book_id is not None
