import random

class BMIPredictor:
    """
    A basic Machine Learning model implemented from scratch using 
    Gradient Descent to predict BMI based on Height (m) and Weight (kg).
    """
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        # Initializing weights (w1 for height, w2 for weight) and bias (b)
        self.w_height = random.uniform(-1, 1)
        self.w_weight = random.uniform(-1, 1)
        self.bias = random.uniform(-1, 1)

    def train(self, heights, weights, targets):
        """
        Trains the model using Gradient Descent (Batch Gradient Descent).
        """
        n = len(targets)
        print(f"Starting training for {self.epochs} epochs...")

        for epoch in range(self.epochs):
            dw_h = 0
            dw_w = 0
            db = 0
            total_error = 0

            for i in range(n):
                # Hypothesis: y = w1*h + w2*w + b
                prediction = (self.w_height * heights[i]) + (self.w_weight * weights[i]) + self.bias
                
                # Mean Squared Error derivative
                error = prediction - targets[i]
                total_error += error**2

                # Accumulated gradients
                dw_h += (2/n) * error * heights[i]
                dw_w += (2/n) * error * weights[i]
                db += (2/n) * error

            # Updating parameters
            self.w_height -= self.lr * dw_h
            self.w_weight -= self.lr * dw_w
            self.bias -= self.lr * db

            if (epoch + 1) % 200 == 0:
                mse = total_error / n
                print(f"Epoch {epoch+1}/{self.epochs} - Error (MSE): {mse:.4f}")

    def predict(self, height, weight):
        """
        Predicts BMI for a given height and weight.
        """
        return (self.w_height * height) + (self.w_weight * weight) + self.bias

def main():
    # Sample Dataset: [Height in meters, Weight in kg, Actual BMI]
    # BMI Formula: weight / height^2
    dataset = [
        [1.50, 45, 20.0],
        [1.60, 55, 21.5],
        [1.70, 65, 22.5],
        [1.75, 75, 24.5],
        [1.80, 85, 26.2],
        [1.85, 95, 27.8],
        [1.65, 50, 18.4],
        [1.55, 60, 25.0],
        [1.72, 70, 23.7],
        [1.68, 80, 28.3]
    ]

    # Splitting dataset into training features and targets
    heights = [row[0] for row in dataset]
    weights = [row[1] for row in dataset]
    targets = [row[2] for row in dataset]

    # Initialize and train the model
    # Note: Using a low learning rate because weights can be sensitive to large height values
    model = BMIPredictor(learning_rate=0.001, epochs=2000)
    model.train(heights, weights, targets)

    print("\nTraining Complete!")
    print(f"Learned Weights: Height_Weight={model.w_height:.4f}, Weight_Weight={model.w_weight:.4f}, Bias={model.bias:.4f}")

    # Testing the model with new data
    test_cases = [
        (1.70, 70),  # Expected BMI ~24.2
        (1.60, 50),  # Expected BMI ~19.5
        (1.80, 90)   # Expected BMI ~27.8
    ]

    print("\n--- Predictions ---")
    for h, w in test_cases:
        prediction = model.predict(h, w)
        actual_bmi = w / (h**2)
        print(f"Height: {h}m, Weight: {w}kg")
        print(f"Predicted BMI: {prediction:.2f}")
        print(f"Actual (Formula) BMI: {actual_bmi:.2f}")
        print(f"Difference: {abs(prediction - actual_bmi):.2f}\n")

if __name__ == "__main__":
    main()
