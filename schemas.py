from pydantic import BaseModel, EmailStr, Field, HttpUrl

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

class LoginRequest(RegisterRequest):
    pass

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class APICreate(BaseModel):
    name: str
    slug: str = Field(pattern=r"^[a-z0-9-]+$")
    version: str = "v1"
    target_url: HttpUrl
    description: str = ""

class APIResponse(APICreate):
    id: int
    is_active: bool
    owner_id: int
    model_config = {"from_attributes": True}

class KeyCreate(BaseModel):
    name: str = "default"

class KeyResponse(BaseModel):
    id: int
    name: str
    prefix: str
    api_key: str

class UsageResponse(BaseModel):
    total_requests: int
    successful_requests: int
    failed_requests: int
