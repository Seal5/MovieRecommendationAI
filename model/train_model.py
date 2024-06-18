from src.collaborative_filtering import collaborative_filtering
from src.content_based_filtering import content_based_filtering
from src.utils import save_model_to_s3

def main():
    ratings_data_path = 'data/ratings.csv'
    movies_data_path = 'data/movies.csv'
    
    # Train the Filtering Model
    cf_model, cf_rmse, cf_mae = collaborative_filtering(ratings_data_path)
    print(f'Collaborative Filtering - RMSE: {cf_rmse}, MAE: {cf_mae}')
    
    # Train the Content-Based Filtering Model
    cb_model = content_based_filtering(movies_data_path)
    
    # Save models to Aws S3
    save_model_to_s3(cf_model, 'your-s3-bucket', 'collaborative_filtering/model.pkl')
    save_model_to_s3(cb_model, 'your-s3-bucket', 'content_based_filtering/model.pkl')

if __name__ == '__main__':
    main()