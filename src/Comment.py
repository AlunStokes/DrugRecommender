class Comment(object):
    def __init__(self, user, purpose, content, rating):
        self.user = user
        self.purpose = purpose
        self.content = content
        self.rating = rating

    def __str__(self):
        s = ""
        s += self.user + '\n'
        s += self.purpose + '\n'
        s += self.content + '\n'
        s += str(self.rating) + '/10'
        return s
