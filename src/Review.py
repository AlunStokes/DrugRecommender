class Review(object):
    def __init__(self, drug, purpose, content, rating):
        self.drug = drug
        self.purpose = purpose
        self.content = content
        self.rating = rating

    def __str__(self):
        s = ""
        s += self.drug + '\n'
        s += self.purpose + '\n'
        s += self.content + '\n'
        s += str(self.rating) + '/10'
        return s
