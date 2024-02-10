#!/USR/BIN/PYTHON3
"""
    review inhereits from BaseModel
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
        Class Review
    """

    place = ""
    user_id = ""
    text = ""
