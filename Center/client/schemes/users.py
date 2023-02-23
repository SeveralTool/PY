def users_schemas(user) -> dict:
    return {
        "id": str(user["_id"]), 
        "username": user["username"],
        "email": user["email"],
    }
    