import pickle

from User import User

if __name__ == '__main__':
    with open('./data/user_data.pkl', 'rb') as f:
        users = pickle.load(f)

    print(users[4121])
