from pydantic import BaseModel
class LoginRequest(BaseModel): email: str; password: str
class RegisterRequest(BaseModel): email: str; full_name: str | None = ""; password: str
class TokenResponse(BaseModel): access_token: str; refresh_token: str; token_type: str = "bearer"
class ResetRequest(BaseModel): email: str
class DoReset(BaseModel): token: str; new_password: str
