from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI(title="QuickBase to PPT API")

# Root endpoint
@app.get("/")
def root():
    return {"message": "QuickBase to PPT API is running. Use /health to check status."}

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
    return JSONResponse(
        content={
            "message": "Request received. PPT conversion process will be implemented next.",
            "templateId": templateId,
            "recordId": recordId,
            "filename": filename
        }
    )
