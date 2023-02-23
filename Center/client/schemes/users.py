def users_schemas(user) -> dict:
    return {
        "id": str(user["_id"]), 
        "username": user["username"],
        "email": user["email"],
    }
    
def all_users(users) -> list:
    return [users_schemas(user) for user in users]