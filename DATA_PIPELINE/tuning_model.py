from sklearn.model_selection import RandomizedSearchCV  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.pipeline import Pipeline
from clean_data import preprocess_data

# Step 4: Hyperparameter tuning
def tune_model(X, y):
    model = RandomForestClassifier()  # Choose a model to tune
    pipeline = Pipeline(steps=[
        ('preprocessor', preprocess_data(X)),  # Preprocess the data
        ('model', model)  # Include the model
    ])

    # Define the hyperparameter grid to search
    param_distributions = {
        'model__n_estimators': [50, 100, 200],  # Number of trees in the forest
        'model__max_depth': [None, 10, 20, 30],  # Maximum depth of the tree
    }

    # Perform randomized search
    search = RandomizedSearchCV(pipeline, param_distributions, n_iter=10, cv=5, random_state=42)
    search.fit(X, y)  # Fit the model to the data

    return search.best_params_  # Return the best hyperparameters found