from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score 
from clean_data import preprocess_data
from tuning_model import tune_model

# Step 5: Evaluate the final model using the best hyperparameters
def evaluate_final_model(X, y):
    best_params = tune_model(X, y)  # Get the best hyperparameters
    model = RandomForestClassifier(**best_params)  # Create model with best params
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocess_data(X)),  # Preprocess the data
        ('model', model)  # Include the model
    ])

    # Split the data again for evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Fit and predict
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    # Calculate the F1 score for the final model
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    return f1  # Return the final F1 score