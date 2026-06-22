import wikipedia
import re
import json
from pydantic import BaseModel
from typing import Optional

class Institution(BaseModel):
    name: str
    founder: Optional[str] = None
    founded_year: Optional[str] = None
    branches: Optional[str] = None
    employees: Optional[str] = None
    summary: str

def get_details(name):
    try:
        page = wikipedia.page(name)
        text = page.content
        summary = wikipedia.summary(name, sentences=4)

        founder = re.search(r'founder.*?([A-Z][a-zA-Z ]+)', text, re.I)
        year = re.search(r'(Founded|Established).*?(\d{4})', text, re.I)
        employees = re.search(r'(employees|staff|faculty).?(\d[\d,])', text, re.I)
        branches = re.search(r'(branches|campuses).*?(\d+)', text, re.I)

        result = Institution(
            name=name,
            founder=founder.group(1).strip() if founder else None,
            founded_year=year.group(2) if year else None,
            branches=branches.group(2) if branches else None,
            employees=employees.group(2) if employees else None,
            summary=summary
        )

        print(json.dumps(result.model_dump(), indent=4))

    except Exception as e:
        result = Institution(
            name=name,
            summary=f"Error: {e}"
        )
        print(json.dumps(result.model_dump(), indent=4))

institution = input("Enter Institution Name: ")

get_details(institution)
