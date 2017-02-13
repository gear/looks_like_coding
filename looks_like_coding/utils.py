class bcolors:
    """Define colors for code highlighting"""

    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        PURPLE = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''

    def paint(self, string, color):
        """Return the string which will be printed in color."""
        if isinstance(color, str):
            return self.__class__.__dict__[color] + string + self.ENDC
        elif isinstance(color, list):
            return ''.join([self.__class__.__dict__[i] for i in color]) \
                   + string + self.ENDC
        else:
            raise ValueError

    def printc(self, string, color):
        """Print @param string in @param color."""
        print(self.paint(string, color))
