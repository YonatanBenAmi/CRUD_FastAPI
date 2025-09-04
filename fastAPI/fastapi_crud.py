from fastapi import FastAPI, HTTPException

app = FastAPI()

users = []


# <<< Create >>>
@app.post("/users/")
def create_user(user: dict):
    for single_user in users: # בודק אם קיים כבר משתמש כזה לפני היצירה
        if single_user["id"] == user["id"]:
            raise HTTPException(status_code=400, detail="User already exists")
    users.append(user) # מוסיף את המשתמש
    return user


# <<< Get >>>
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/")
def get_all_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# <<< Update >>>
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# <<< Delete >>>
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")


