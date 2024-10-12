from load_data import load_csv
from clean_data import preprocess_data
from train_model import train_and_evaluate
from tuning_model import tune_model
from evaluation_model import evaluate_final_model

route = ''
file_path = route

def main():
    # Load data
    data = load_csv(file_path)  # Replace with your CSV file path
    
    # Clean the data
    cleaned_data = preprocess_data(data)
    
    # Separate features and target
    X = cleaned_data.drop(columns=['column to drop'])  
    y = cleaned_data['data to predict']  
    
    # Train and evaluate models
    f1_scores = train_and_evaluate(X, y)
    print("F1 Scores for each model:")
    for model, score in f1_scores.items():
        print(f"{model}: {score}")
    
    # Hyperparameter tuning
    best_params = tune_model(X, y)
    print("Best hyperparameters found:")
    print(best_params)
    
    # Evaluate the final model with hyperparameter tuning
    final_f1_score = evaluate_final_model(X, y)
    print(f"Final F1 Score for the best model: {final_f1_score}")

if __name__ == "__main__":
    main()