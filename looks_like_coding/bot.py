import fbchat
import utils
import getpass
import random

with open('data/dwight_quotes.txt', 'r') as f:
    dwight_quotes = f.readlines()

class GreetBot(fbchat.Client):
    """Saying hi. Copied from EchoBot."""
    
    def __init__(self, email, password, name="GreetBot", master="Hoang"):
        """Create the bot with @param email and @param password."""
        fbchat.Client.__init__(self, email, password)
        self.name = name
        self.master = master

    def on_message(self, mid, author_id, author_name, message, metadata):
        """Call upon a message is received."""
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)
        print("{} said: {}".format(author_name, message))
        if (str(author_id) == str(self.uid)):
            pass
        else:
            self.send(author_id, "Hi, this is {}'s bot, not Hoang.\
                                  My name is {}. Chat with me might be\
                                  more interesting...".format(self.master, self.name))
            self.send(author_id, "I cannot do much for now...")


class Dwight(GreetBot):
    """Hoang's robot butler, Dwight.""" 
    def __init__(self, email, password, name="Dwight", master="Hoang"):
        super(Dwight, self).__init__(email, password, master)
        self.quotes = dwight_quotes
    
    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid)
        self.markAsRead(author_id)
        print("{} said: {}".format(author_id, message))
        if (str(author_id) == str(self.uid)) and message != "test":
            pass
        else:
            i = random.randint(0,len(self.quotes))
            self.send(author_id, self.quotes[i])


def test():
    """Test the greet bot.""" 
    email = input("Enter your email:" )
    password = getpass.getpass("Type in your password: ")
    bot = GreetBot(email, password)
    bot.listen()

def test_dwight():
    """Test Dwight bot.""" 
    email = input("Enter your email:" )
    password = getpass.getpass("Type in your password: ")
    bot = Dwight(email, password)
    bot.listen()


if __name__ == "__main__":
    test_dwight()
