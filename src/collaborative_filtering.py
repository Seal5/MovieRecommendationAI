import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

def collaborative_filtering(data_path):
    
    # loading the dataset for use
    df = pd.read_csv(data_path)
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(df[['userId', 'movieId', 'rating']], reader)
    
    # split the dataset 
    trainset, testset = train_test_split(data, test_size=0.2)
    
    # build the algorithm to solve
    algo = SVD()
    algo.fit(trainset)
    
    # test the algorithm for function
    predictions = algo.test(testset)
    
    # calculate RMSE and MAE
    rmse = accuracy.rmse(predictions)
    mae = accuracy.mae(predictions)
    
    return algo, rmse, mae