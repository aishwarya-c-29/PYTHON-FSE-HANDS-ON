class Database:
    def get_user(self, user_id):
        # Imagine this fetches data from a real database
        print("Fetching from database...")
        return {"id": user_id, "name": "Alice"}

def get_username(user_id):
    db = Database()
    user = db.get_user(user_id)
    return user["name"]
