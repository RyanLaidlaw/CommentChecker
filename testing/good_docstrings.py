def greet(name):
    """Generate a personalized greeting message."""
    return f"Hello, {name}! Welcome!"

def farewell(name):
    """Generate a personalized farewell message."""
    return f"Goodbye, {name}! See you next time!"

if __name__ == "__main__":
    # Example usage
    print(greet("Alice"))
    print(farewell("Alice"))