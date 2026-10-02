from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter()
gemini_generator = GeminiDocumentGenerator()

# User input-ஐ validate செய்யும் model
class DocumentRequest(BaseModel):
    document_type: str
    details: str

# POST endpoint - document generate செய்ய
@router.post("/generate")
def generate_document(request: DocumentRequest):
    result = gemini_generator.generate(request.document_type, request.details)
    return {"generated_content": result}
