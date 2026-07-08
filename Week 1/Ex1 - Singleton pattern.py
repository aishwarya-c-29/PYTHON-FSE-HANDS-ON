class Singleton:

    # Store the single instance
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton Object...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        print("Singleton Initialized")

    def show_message(self):
        print("Hello from Singleton!")


# Create first object
obj1 = Singleton()
obj1.show_message()

# Create second object
obj2 = Singleton()
obj2.show_message()

# Check if both objects are the same
print("Are both objects same?", obj1 is obj2)

"""
Creating Singleton Object...
Singleton Initialized
Hello from Singleton!
Singleton Initialized
Hello from Singleton!
Are both objects same? True 
"""
