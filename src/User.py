class User(object):
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def __eq__(self, other):
        return self.name == other.name

    def __len__(self):
        return len(self.reviews)

    def __str__(self):
        s = ""
        s += self.name + '\n'
        i = 0
        while i < len(self.reviews):
            s += '{}: {}\n'.format(i + 1, self.reviews[i])
            i += 1
        return s
