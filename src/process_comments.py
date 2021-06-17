import pickle

from Comment import Comment
from Review import Review
from User import User

def comment_list_to_field_lists(l):
    users = []
    purposes = []
    contents = []
    ratings = []
    for i in l:
        users.append(i.user)
        purposes.append(i.purpose)
        contents.append(i.content)
        ratings.append(i.rating)
    return users, purposes, contents, ratings

if __name__ == '__main__':
    with open('./data/comment_data.pkl', 'rb') as f:
        data = pickle.load(f)

    users = []

    for key in data.keys():
        '''if len(data[key]) < 100:
            continue'''
        print("Processing {}".format(key))
        for comment in data[key]:
            if User(comment.user) in users:
                r = Review(key, comment.purpose, comment.content, comment.rating)
                users[users.index(User(comment.user))].add_review(r)
            else:
                r = Review(key, comment.purpose, comment.content, comment.rating)
                u = User(comment.user)
                u.add_review(r)
                users.append(u)

    with open('./data/user_data.pkl', 'wb') as f:
        pickle.dump(users, f, pickle.HIGHEST_PROTOCOL)
