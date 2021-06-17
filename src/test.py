from surprise import SVD
from surprise import accuracy
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise.model_selection import train_test_split
from surprise.model_selection import GridSearchCV

import numpy as np

reader = Reader(line_format='user item rating', sep=',')
data = Dataset.load_from_file('./data/ratings.csv', reader=reader)
#data = Dataset.load_builtin('ml-100k')

#cross_validate(CoClustering(), data, verbose=True, measures=['RMSE', 'MAE', 'FCP'], cv=4)

trainset, testset = train_test_split(data, test_size=0.2)

# We'll use the famous SVD algorithm.
algo = SVD(n_epochs=20, lr_all=0.005, reg_all=0.1, n_factors=10, biased=False)
P = []
i = 0
while i < 50:
    # Train the algorithm on the trainset, and predict ratings for the testset
    algo.fit(trainset)
    predictions = algo.test(testset)
    p = accuracy.fcp(predictions)
    P.append(p)

    i += 1
print(np.mean(P))
print(np.std(P))

'''algo = SVD(n_epochs=10, lr_all=0.005, reg_all=0, n_factors=20, biased=False)
cross_validate(algo, data, measures=['RMSE', 'FCP'], cv=5, verbose=True)'''

'''param_grid = {'n_epochs': [5, 10,20], 'lr_all': [0.002, 0.005,],
'reg_all': [0, 0.05, 0.1, 0.15, 0.2], 'n_factors': [5,10,15,20,25],
'biased': [False]}
gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'fcp'], cv=5)

gs.fit(data)

# best RMSE score
print(gs.best_score['fcp'])
# combination of parameters that gave the best RMSE score
print(gs.best_params['fcp'])

# best RMSE score
print(gs.best_score['rmse'])
# combination of parameters that gave the best RMSE score
print(gs.best_params['rmse'])'''
