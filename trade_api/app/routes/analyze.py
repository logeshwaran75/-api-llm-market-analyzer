from fastapi import APIRouter, HTTPException
from app.services.search_service import search_sector
from app.services.groq_service import analyze_market

router = APIRouter()

@router.get("/analyze/{sector}")
async def analyze(sector: str):

    if len(sector) < 3:
        raise HTTPException(
            status_code=400,
            detail="Invalid sector"
        )

    data = search_sector(sector)

    report = analyze_market(sector, data)

    # Save markdown file
    filename = f"{sector}_report.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    return {
        "sector": sector,
        "report": report,
        "file_saved": filename
    }