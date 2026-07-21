from typing import Literal

from pydantic import BaseModel, Field


class EmailRequest(BaseModel):

    email: str = Field(
        min_length=10,
        max_length=5000
    )

    tone: Literal[
        "Professional",
        "Friendly",
        "Formal",
        "HR",
        "Customer Support",
    ]


class EmailResponse(BaseModel):
    reply: str