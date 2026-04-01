from Aşağıdaki kodu **kopyala ve yapıştır**:

```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# ============ USER SCHEMAS ============

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str = Field(..., min_length=1, max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# ============ APIARY SCHEMAS ============

class ApiaryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=255)
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ApiaryCreate(ApiaryBase):
    pass

class ApiaryUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ApiaryResponse(ApiaryBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ============ HIVE SCHEMAS ============

class HiveBase(BaseModel):
    hive_number pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# ==================== USER SCHEMAS ====================

class UserBase(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# ==================== APIARY SCHEMAS ====================

class ApiaryBase(BaseModel):
    name: str
    location: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ApiaryCreate(ApiaryBase):
    pass

class ApiaryUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class ApiaryResponse(ApiaryBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ==================== HIVE SCHEMAS ====================

class HiveBase(BaseModel):
    hive_number: str
    hive_type: str
    queen_color: Optional[str] = None

class HiveCreate(HiveBase):
    apiary_id: int

class HiveUpdate(BaseModel):
    hive_number: Optional[str] = None
    hive_type: str = Field(..., min_length=1, max_length=50)
    hive_type: str = Field(..., min_length=1, max_length=50)
    queen_color: Optional[str] = None

class HiveCreate(HiveBase):
    apiary_id: int

class HiveUpdate(BaseModel):
    hive_number: Optional[str] = None
    hive_type: Optional[str] = None
    status: Optional[str] = None
    queen_color: Optional[str] = None

class HiveResponse(HiveBase):
    id: int
    apiary_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ============ INSPECTION SCHEMAS ============

class InspectionBase(BaseModel):
    queen_seen: bool = False
    brood_status: str = Field(..., min_length=1, max_length=50)
    food_level: str = Field(..., min_length=1, max_length=50)
    disease_signs: Optional[str] = None
    treatment_applied: Optional[str] = None
    notes: Optional[str] = None

class InspectionCreate(InspectionBase):
    hive_id: int

class InspectionResponse(InspectionBase):
    id: int
    hive_id: int
    inspection_date: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True

# ============ HONEY PRODUCTION SCHEMAS ============

class HoneyProductionBase(BaseModel):
    honey_kg: float = Field(..., gt=0)
    beeswax_kg: float = Fiel: Optional[str] = None
    status: Optional[str] = None
    queen_color: Optional[str] = None

class HiveResponse(HiveBase):
    id: int
    apiary_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# ==================== INSPECTION SCHEMAS ====================

class InspectionBase(BaseModel):
    queen_seen: bool
    brood_status: str
    food_level: str
    disease_signs: Optional[str] = None
    treatment_applied: Optional[str] = None
    notes: Optional[str] = None

class InspectionCreate(InspectionBase):
    hive_id: int

class InspectionUpdate(BaseModel):
    queen_seen: Optional[bool] = None
    brood_status: Optional[str] = None
    food_level: Optional[str] = None
    disease_signs: Optional[str] = None
    treatment_applied: Optional[str] = None
    notes: Optional[str] = None

class InspectionResponse(InspectionBase):
    id: int
    hive_id: int
    inspection_date: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True

# ==================== HONEY PRODUCTION SCHEMAS ====================

class HoneyProductionBase(BaseModel):
    honey_kg: float
    beeswax_kg: Optional[float] = 0
    pollen_kg: Optional[float] = 0
    notes: Optional[str] = None

class HoneyProductionCreate(HoneyProductionBase):
    hive_id: int

class HoneyProductionUpdate(BaseModeld(default=0, ge=0)
    pollen_kg: float = Field(default=0, ge=0)
    notes: Optional[str] = None

class HoneyProductionCreate(HoneyProductionBase):
    hive_id: int

class HoneyProductionResponse(HoneyProductionBase):
    id: int
    hive_id: int
    production_date: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True
