from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Dummy user database
users = {
    "admin": {
        "username": "admin",
        "password": pwd_context.hash("admin123")
    }
}

# Create JWT Token
def create_token(data):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=30)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Login
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users.get(form_data.username)

    if not user or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

# Verify Token
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Protected Route
@app.get("/profile")
def profile(user: str = Depends(get_current_user)):
    return {"message": f"Welcome {user}"}

# Logout
@app.post("/logout")
def logout():
    return {
        "message": "Logout successful. Delete the JWT token on the client side."
    }

Output:
Login Request
POST /login

Form data:

username=admin
password=admin123

Response:

{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
Access Protected Route
GET /profile

Header:

Authorization: Bearer eyJhbGciOiJIUzI1NiIs...

Response:

{
  "message": "Welcome admin"
}
Logout
POST /logout

Response:

{
  "message": "Logout successful. Delete the JWT token on the client side."
}
