import pickle

from Users import Users

import numpy as np
import scipy.linalg

def svd(train, k):
    utilMat = np.array(train)
    # the nan or unavailable entries are masked
    mask = np.isnan(utilMat)
    masked_arr = np.ma.masked_array(utilMat, mask)
    item_means = np.mean(masked_arr, axis=0)
    # nan entries will replaced by the average rating for each item
    utilMat = masked_arr.filled(item_means)
    x = np.tile(item_means, (utilMat.shape[0],1))
    # we remove the per item average from all entries.
    # the above mentioned nan entries will be essentially zero now
    utilMat = utilMat - x
    # The magic happens here. U and V are user and item features
    U, s, V=np.linalg.svd(utilMat, full_matrices=False)
    s=np.diag(s)
    # we take only the k most significant features
    s=s[0:k,0:k]
    U=U[:,0:k]
    V=V[0:k,:]
    s_root=scipy.linalg.sqrtm(s)
    Usk=np.dot(U,s_root)
    skV=np.dot(s_root,V)
    UsV = np.dot(Usk, skV)
    UsV = UsV + x
    print("svd done")
    return UsV

if __name__ == '__main__':
    with open('./data/user_data.pkl', 'rb') as f:
        data = pickle.load(f)

    users = Users(data)

    drugs = ['fluoxetine', 'escitalopram', 'citalopram', 'fluvoxamine', 'paroxetine', 'sertraline', 'vilazodone', 'bupropion', 'tranylcypromine',
    'phenelzine', 'duloxetine', 'desvenlafaxine', 'levomilnacipran', 'venlafaxine', 'nefazodone', 'trazodone', 'amitriptyline', 'clomipramine',
    'desipramine', 'doxepin', 'imipramine', 'nortriptyline', 'mirtazapine']

    users.filter(lambda x: x.num_dist_drugs() > 1)
    users.generate_matrix(drugs)

    mat = users.matrix
    train = mat[0:700]
    test = mat[700:]

    calc = svd(train, 15)

    print(mat[0])
    print(calc[0])
