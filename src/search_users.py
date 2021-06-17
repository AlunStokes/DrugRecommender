import pickle
import csv

from Users import Users

if __name__ == '__main__':
    with open('./data/user_data.pkl', 'rb') as f:
        data = pickle.load(f)

    users = Users(data)

    drugs = ['fluoxetine', 'escitalopram', 'citalopram', 'fluvoxamine', 'paroxetine', 'sertraline', 'vilazodone', 'bupropion', 'tranylcypromine',
    'phenelzine', 'duloxetine', 'desvenlafaxine', 'levomilnacipran', 'venlafaxine', 'nefazodone', 'trazodone', 'amitriptyline', 'clomipramine',
    'desipramine', 'doxepin', 'imipramine', 'nortriptyline', 'mirtazapine']

    #users.filter(lambda x: x.num_dist_drugs() > 1)

    user_index, item_index, ratings = users.generate_sparse_matrix(drugs)

    print(len(user_index))
    exit()

    with open('./data/ratings.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow(["user", "drug", "rating"])
        for u,i,r in zip(user_index, item_index, ratings):
            writer.writerow([u,i,(r-1)//2+1])
