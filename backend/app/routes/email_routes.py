from fastapi import APIRouter

from app.models.email_models import EmailRequest, EmailResponse
from app.services.email_service import generate_email_reply

router = APIRouter()


@router.post("/generate", response_model=EmailResponse)
def generate_reply(request: EmailRequest):

    reply = generate_email_reply(
        email=request.email,
        tone=request.tone,
    )

    return EmailResponse(reply=reply)