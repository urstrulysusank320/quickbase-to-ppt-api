# from fastapi import FastAPI, Query
# from fastapi.responses import JSONResponse
# import requests
# import os

# app = FastAPI(title="QuickBase to PPT API")

# # Root endpoint
# @app.get("/")
# def root():
#     return {"message": "QuickBase to PPT API is running. Use /health to check status."}

# # Health check endpoint
# @app.get("/health")
# def health_check():
#     return {"status": "OK"}

# # Placeholder endpoint for generating PPT
# @app.get("/generateppt")
# def generate_ppt(
#     templateId: str = Query(..., description="Quickbase Template ID"),
#     recordId: str = Query(..., description="Quickbase Record ID"),
#     filename: str = Query("output", description="Output PPT filename")
# ):
#     """
#     This endpoint will:
#     1. Call Quickbase API to generate PDF/HTML
#     2. Convert it to PPT
#     3. Return PPT as downloadable file
#     """
    
#     # Placeholder logic
#     return JSONResponse(
#         content={
#             "message": "Request received. PPT conversion process will be implemented next.",
#             "templateId": templateId,
#             "recordId": recordId,
#             "filename": filename
#         }
#     )

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from pptx import Presentation
from pptx.util import Inches, Pt
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

# Generate PPT endpoint
@app.get("/generateppt")
def generate_ppt(
    templateId: str = Query(..., description="Quickbase Template ID"),
    recordId: str = Query(..., description="Quickbase Record ID"),
    filename: str = Query("output", description="Output PPT filename")
):
    """
    Generate a simple PPT for demonstration purposes.
    """
    try:
        # Create a new presentation
        prs = Presentation()

        # Add a title slide
        slide_layout = prs.slide_layouts[0]  # 0 = Title slide
        slide = prs.slides.add_slide(slide_layout)
        slide.shapes.title.text = f"QuickBase Record {recordId}"
        slide.placeholders[1].text = f"Template ID: {templateId}"

        # Add a content slide
        slide_layout = prs.slide_layouts[1]  # 1 = Title + Content
        slide = prs.slides.add_slide(slide_layout)
        slide.shapes.title.text = "Record Details"
        content = slide.placeholders[1]
        content.text = f"This PPT was generated for Record ID {recordId} using Template ID {templateId}."

        # Save the PPT
        output_file = f"{filename}.pptx"
        prs.save(output_file)

        # Return the PPT as a downloadable file
        return FileResponse(path=output_file, filename=output_file, media_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')

    except Exception as e:
        return JSONResponse(content={"error": str(e)})
