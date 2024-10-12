from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  
from sklearn.linear_model import LogisticRegression  
from sklearn.svm import SVC  
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score  
from clean_data import preprocess_data

# Step 3: Train multiple models
def train_and_evaluate(X, y):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Define models to train
    models = {
        'Random Forest': RandomForestClassifier(),
        'Logistic Regression': LogisticRegression(),
        'SVC': SVC()
    }

    # Dictionary to hold F1 scores of each model
    f1_scores = {}

    # Train and evaluate each model
    for name, model in models.items():
        # Create a pipeline that first preprocesses and then trains the model
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocess_data(X)),  # Preprocess the data
            ('model', model)  # Train the model
        ])
        
        # Fit the model on the training data
        pipeline.fit(X_train, y_train)
        
        # Predict on the test data
        y_pred = pipeline.predict(X_test)
        
        # Calculate the F1 score
        f1 = f1_score(y_test, y_pred, average='weighted')
        f1_scores[name] = f1  # Store the F1 score for the model

    return f1_scores  # Return the F1 scores for comparison