from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
import os

app = FastAPI(title="QuickBase to PPT API")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "OK"}

# Placeholder endpoint for generating PPT
@app.get("/generateppt")
def generate_ppt(
    templateId: str = Query(..., description="Quickbase Template ID"),
    recordId: str = Query(..., description="Quickbase Record ID"),
    filename: str = Query("output", description="Output PPT filename")
):
    """
    This endpoint will:
    1. Call Quickbase API to generate PDF/HTML
    2. Convert it to PPT
    3. Return PPT as downloadable file
    """
    
    # Placeholder logic
    # For now, it just returns JSON
    return JSONResponse(
        content={
            "message": "Received request. Later we will convert Quickbase template to PPT.",
            "templateId": templateId,
            "recordId": recordId,
            "filename": filename
        }
    )
