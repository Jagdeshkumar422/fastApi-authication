from passlib.context import CryptContext
from pydantic import BaseModel

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserCreate(BaseModel):
    username: str
    password: str

def hash_password(password: str):
    """Hash the user's password."""
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    """Verify the entered password."""
    return pwd_context.verify(plain_password, hashed_password)
