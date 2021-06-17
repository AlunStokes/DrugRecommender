from User import User

import numpy as np

class Users(object):
    def __init__(self, users=None):
        if users is not None:
            self.users = users
        else:
            self.users = []

    def generate_matrix(self, drugs):
        for user in self.users:
            user.generate_vector(drugs)

        self.matrix = np.ndarray((len(self.users), len(drugs)))
        i = 0
        while i < len(self.users):
            self.matrix[i] = self.users[i].vector
            i += 1

    def filter(self, cond):
        l = []
        for user in self.users:
            if cond(user):
                l.append(user)
        self.users = l

    def __len__(self):
        return len(self.users)

    def __getitem__(self, x):
        return self.users[x]

    def generate_sparse_matrix(self, drugs):
        user_index = []
        item_index = []
        ratings = []
        j = 0
        for user in self.users:
            i, r = user.generate_sparse_vector(drugs)
            user_index += [j] * len(i)
            item_index += i
            ratings += r
            j += 1

        return user_index, item_index, ratings
