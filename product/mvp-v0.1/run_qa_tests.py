"""
QA Verification Test Runner for Fresher Job Application Kit (Free MVP v0.1)
Executes deep automated validation across all 8 generated artifact files.
"""

import os
import sys
from docx import Document
import openpyxl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def test_docx(file_path):
    print(f"\n--- Testing DOCX: {os.path.basename(file_path)} ---")
    doc = Document(file_path)
    
    # 1. Section margins
    s = doc.sections[0]
    print(f"Margins: Top={s.top_margin.inches}in, Bottom={s.bottom_margin.inches}in, Left={s.left_margin.inches}in, Right={s.right_margin.inches}in")
    assert s.top_margin.inches <= 0.6, "Top margin should be <= 0.6in"
    assert s.left_margin.inches <= 0.7, "Left margin should be <= 0.7in"
    
    # 2. Table count (Should be 0 for pure linear single-column ATS compatibility)
    table_count = len(doc.tables)
    print(f"Core Layout Tables Count: {table_count} (Expect 0 for pure linear flow)")
    assert table_count == 0, "ATS Single-Column template must not rely on tables for core layout"
    
    # 3. Paragraph count and content inspection
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    print(f"Total Non-Empty Paragraphs: {len(paras)}")
    
    # Verify core sections exist
    required_sections = ["EDUCATION", "TECHNICAL SKILLS", "ACADEMIC & TECHNICAL PROJECTS", "EXPERIENCE & PRACTICAL WORK", "CERTIFICATIONS & VERIFIED ACHIEVEMENTS"]
    found_sections = []
    for s_name in required_sections:
        found = any(s_name in p for p in paras)
        if found:
            found_sections.append(s_name)
    print(f"Found Sections: {len(found_sections)} / {len(required_sections)}")
    assert len(found_sections) == len(required_sections), f"Missing sections: {set(required_sections) - set(found_sections)}"
    
    # 4. Check for unlabelled fabrications
    all_text = " ".join(paras)
    assert "FATHER" not in all_text.upper() or "FATHER'S NAME" not in all_text.upper(), "Father's name found in resume template!"
    assert "DECLARATION" not in all_text.upper(), "Declaration found in resume template!"
    print("[PASS] DOCX Validation passed successfully!")
    return True

def test_xlsx(file_path):
    print(f"\n--- Testing XLSX: {os.path.basename(file_path)} ---")
    wb = openpyxl.load_workbook(file_path, data_only=False)
    
    sheet_names = wb.sheetnames
    print(f"Sheets Found: {sheet_names}")
    assert "Application Dashboard" in sheet_names, "Missing 'Application Dashboard' sheet"
    assert "Applications Log" in sheet_names, "Missing 'Applications Log' sheet"
    
    ws_log = wb["Applications Log"]
    headers = [ws_log.cell(row=3, column=c).value for c in range(1, 13)]
    print(f"Log Headers ({len(headers)}): {headers}")
    expected_headers = [
        "Company Name", "Role Applied For", "Job URL / Link", "Date Found",
        "Date Applied", "Resume Version", "Source", "Status",
        "Interview Stage", "Follow-up Date", "Contact / Recruiter Name", "Notes & Next Steps"
    ]
    assert headers == expected_headers, f"Header mismatch: {set(expected_headers) - set(headers)}"
    
    # Check data validations
    dvs = ws_log.data_validations.dataValidation
    print(f"Data Validations Configured: {len(dvs)}")
    assert len(dvs) >= 3, "Expected at least 3 data validations (Source, Status, Interview Stage)"
    
    # Check Dashboard formulas
    ws_dash = wb["Application Dashboard"]
    dash_b5 = ws_dash["B5"].value
    dash_d5 = ws_dash["D5"].value
    print(f"Dashboard B5 Formula: {dash_b5}")
    print(f"Dashboard D5 Formula: {dash_d5}")
    assert dash_b5 and "COUNTA" in str(dash_b5), "Formula in B5 missing or invalid"
    assert dash_d5 and "COUNTIF" in str(dash_d5), "Formula in D5 missing or invalid"
    
    print("[PASS] XLSX Validation passed successfully!")
    return True

def test_pdfs(pdf_list):
    print("\n--- Testing PDF Assets ---")
    all_ok = True
    for pdf_name in pdf_list:
        pdf_path = os.path.join(BASE_DIR, pdf_name)
        exists = os.path.exists(pdf_path)
        size = os.path.getsize(pdf_path) if exists else 0
        print(f"PDF: {pdf_name:32} | Exists: {exists!s:5} | Size: {size:7} bytes", end=" ")
        if exists and size > 25000:
            print("[PASS]")
        else:
            print("[FAIL]")
            all_ok = False
    return all_ok

if __name__ == "__main__":
    print("=" * 60)
    print("STARTING AUTOMATED QA TEST SUITE")
    print("=" * 60)
    
    docx_ok = test_docx(os.path.join(BASE_DIR, "resume-template.docx"))
    xlsx_ok = test_xlsx(os.path.join(BASE_DIR, "job-application-tracker.xlsx"))
    
    pdfs = [
        "resume-template-reference.pdf",
        "resume-removal-checklist.pdf",
        "resume-self-audit.pdf",
        "jd-tailoring-worksheet.pdf",
        "naukri-checklist.pdf",
        "project-bullet-guide.pdf"
    ]
    pdfs_ok = test_pdfs(pdfs)
    
    print("\n" + "=" * 60)
    if docx_ok and xlsx_ok and pdfs_ok:
        print("ALL QA TESTS COMPLETED WITH 100% PASS RATE!")
    else:
        print("SOME QA TESTS FAILED. CHECK LOGS ABOVE.")
    print("=" * 60)
