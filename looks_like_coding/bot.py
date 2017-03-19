import fbchat
import utils
import getpass
import random

dwight_quotes = [

]

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
        print("{} said: {}".format(author_id, message))
        if (author_id == self.id):
            pass
        else:
            self.send(author_id, "Hi, this is {}'s bot, not Hoang.\
                                  My name is {}. Chat with me might be\
                                  more interesting...".format(self.master, self.name))
            self.send(author_id, "I cannot do much for now...")


class Dwight(GreetBot):
    """Hoang's robot butler, Dwight.""" 
    pass


def test():
    """Test the greet bot.""" 
    email = input("Enter your email:" )
    password = getpass.getpass("Type in your password: ")
    bot = GreetBot(email, password)
    bot.listen()


if __name__ == "__main__":
    test()
