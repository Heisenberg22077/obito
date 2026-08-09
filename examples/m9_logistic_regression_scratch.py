"""
Module 9: Logistic Regression from Scratch

This implementation demonstrates the mechanical understanding phase of the 
Practitioner Track - implementing core ML algorithms with NumPy only.

Learning Objectives:
- Understand gradient descent for logistic regression
- Implement sigmoid, loss, and gradient functions
- Build a scikitlearn-compatible estimator class
- Validate against scikit-learn on toy data
"""

import numpy as np
from typing import Tuple, Optional


class LogisticRegressionScratch:
    """
    Logistic Regression classifier implemented from scratch with NumPy.
    
    Parameters
    ----------
    learning_rate : float
        Step size for gradient descent (default: 0.1)
    n_iterations : int
        Number of gradient descent iterations (default: 1000)
    random_state : int, optional
        Random seed for reproducibility
    
    Attributes
    ----------
    weights : np.ndarray
        Learned feature weights
    bias : float
        Learned bias term
    """
    
    def __init__(self, learning_rate: float = 0.1, n_iterations: int = 1000, 
                 random_state: Optional[int] = None):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.random_state = random_state
        self.weights = None
        self.bias = None
        self.loss_history = []
    
    @staticmethod
    def sigmoid(z: np.ndarray) -> np.ndarray:
        """
        Sigmoid activation function.
        
        Maps any real value to (0, 1) range for probability interpretation.
        """
        # Clip to prevent overflow
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))
    
    def _compute_loss(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Binary cross-entropy loss.
        
        Loss = -1/n * sum(y*log(y_pred) + (1-y)*log(1-y_pred))
        """
        epsilon = 1e-15  # Prevent log(0)
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
        n_samples = len(y_true)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss
    
    def fit(self, X: np.ndarray, y: np.ndarray) -> 'LogisticRegressionScratch':
        """
        Fit logistic regression model using gradient descent.
        
        Parameters
        ----------
        X : np.ndarray
            Training features, shape (n_samples, n_features)
        y : np.ndarray
            Binary labels, shape (n_samples,)
        
        Returns
        -------
        self : LogisticRegressionScratch
            Fitted estimator
        """
        if self.random_state is not None:
            np.random.seed(self.random_state)
        
        n_samples, n_features = X.shape
        
        # Initialize weights
        self.weights = np.zeros(n_features)
        self.bias = 0
        self.loss_history = []
        
        # Gradient descent
        for i in range(self.n_iterations):
            # Forward pass
            linear_pred = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(linear_pred)
            
            # Compute loss
            loss = self._compute_loss(y, y_pred)
            self.loss_history.append(loss)
            
            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            
            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            
            # Print progress every 100 iterations
            if (i + 1) % 100 == 0:
                print(f"Iteration {i+1}/{self.n_iterations}, Loss: {loss:.4f}")
        
        return self
    
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """
        Predict probability estimates for samples.
        
        Parameters
        ----------
        X : np.ndarray
            Test features, shape (n_samples, n_features)
        
        Returns
        -------
        probabilities : np.ndarray
            Probability of positive class, shape (n_samples,)
        """
        linear_pred = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear_pred)
    
    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        """
        Predict binary class labels.
        
        Parameters
        ----------
        X : np.ndarray
            Test features, shape (n_samples, n_features)
        threshold : float
            Classification threshold (default: 0.5)
        
        Returns
        -------
        predictions : np.ndarray
            Binary predictions, shape (n_samples,)
        """
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int)
    
    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Calculate accuracy score.
        
        Parameters
        ----------
        X : np.ndarray
            Test features
        y : np.ndarray
            True labels
        
        Returns
        -------
        accuracy : float
            Classification accuracy
        """
        predictions = self.predict(X)
        return np.mean(predictions == y)


def create_toy_dataset(n_samples: int = 100, n_features: int = 2, 
                       random_state: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create a simple binary classification dataset.
    """
    np.random.seed(random_state)
    
    # Generate two clusters
    X_class0 = np.random.randn(n_samples // 2, n_features) + np.array([-2, -2])
    X_class1 = np.random.randn(n_samples // 2, n_features) + np.array([2, 2])
    
    X = np.vstack([X_class0, X_class1])
    y = np.hstack([np.zeros(n_samples // 2), np.ones(n_samples // 2)])
    
    # Shuffle
    shuffle_idx = np.random.permutation(n_samples)
    X, y = X[shuffle_idx], y[shuffle_idx]
    
    return X, y


def main():
    """
    Demonstrate logistic regression implementation.
    """
    print("=" * 60)
    print("Logistic Regression from Scratch - Module 9 Example")
    print("=" * 60)
    
    # Create dataset
    X, y = create_toy_dataset(n_samples=200, n_features=2)
    print(f"\nDataset: {X.shape[0]} samples, {X.shape[1]} features")
    print(f"Class distribution: {np.bincount(y.astype(int))}")
    
    # Split data
    split_idx = int(0.8 * len(X))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]
    
    # Train our implementation
    print("\n--- Training Custom Implementation ---")
    custom_model = LogisticRegressionScratch(
        learning_rate=0.1, 
        n_iterations=1000, 
        random_state=42
    )
    custom_model.fit(X_train, y_train)
    
    # Evaluate
    train_acc = custom_model.score(X_train, y_train)
    test_acc = custom_model.score(X_test, y_test)
    print(f"\nCustom Implementation:")
    print(f"  Training Accuracy: {train_acc:.3f}")
    print(f"  Test Accuracy: {test_acc:.3f}")
    print(f"  Learned weights: {custom_model.weights}")
    print(f"  Learned bias: {custom_model.bias:.3f}")
    
    # Compare with scikit-learn
    try:
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score
        
        print("\n--- Comparing with scikit-learn ---")
        sklearn_model = LogisticRegression(random_state=42, max_iter=1000)
        sklearn_model.fit(X_train, y_train)
        
        sklearn_train_acc = sklearn_model.score(X_train, y_train)
        sklearn_test_acc = sklearn_model.score(X_test, y_test)
        
        print(f"scikit-learn:")
        print(f"  Training Accuracy: {sklearn_train_acc:.3f}")
        print(f"  Test Accuracy: {sklearn_test_acc:.3f}")
        print(f"  Learned weights: {sklearn_model.coef_[0]}")
        print(f"  Learned bias: {sklearn_model.intercept_[0]:.3f}")
        
        print(f"\n✅ Performance match: {abs(test_acc - sklearn_test_acc) < 0.05}")
        
    except ImportError:
        print("\n⚠️ scikit-learn not available for comparison")
    
    print("\n" + "=" * 60)
    print("Next Steps:")
    print("1. Try different learning rates")
    print("2. Add regularization (L1/L2)")
    print("3. Implement multi-class classification")
    print("4. Add early stopping")
    print("=" * 60)


if __name__ == "__main__":
    main()
