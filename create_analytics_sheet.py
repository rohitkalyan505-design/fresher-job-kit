"""
Script to create exp003_content_and_conversion_tracker.xlsx
Generates 3 sheets: Dashboard, Content Performance Log, and Inquiries & Feature Clusters.
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
analytics_dir = os.path.join(BASE_DIR, "analytics")
os.makedirs(analytics_dir, exist_ok=True)
xlsx_path = os.path.join(analytics_dir, "exp003_content_and_conversion_tracker.xlsx")

wb = openpyxl.Workbook()

# Sheet 1: EXP-003 Summary Dashboard
ws_dash = wb.active
ws_dash.title = "EXP-003 Dashboard"
ws_dash.views.sheetView[0].showGridLines = True

# Sheet 2: Content Metrics Log
ws_log = wb.create_sheet(title="Content Performance Log")
ws_log.views.sheetView[0].showGridLines = True

# Sheet 3: Inquiries & Feature Clusters
ws_req = wb.create_sheet(title="Inquiries & Feature Clusters")
ws_req.views.sheetView[0].showGridLines = True

# Palette
header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
kpi_title_font = Font(name="Calibri", size=10, bold=True, color="475569")
kpi_num_font = Font(name="Calibri", size=18, bold=True, color="0F172A")
kpi_border = Border(
    left=Side(style='thin', color="CBD5E1"),
    right=Side(style='thin', color="CBD5E1"),
    top=Side(style='thin', color="CBD5E1"),
    bottom=Side(style='thin', color="CBD5E1")
)
kpi_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

# --- DASHBOARD SETUP ---
ws_dash["A1"] = "EXP-003 EXPERIMENT METRICS & VALIDATION DASHBOARD"
ws_dash["A1"].font = Font(name="Calibri", size=16, bold=True, color="0F172A")
ws_dash["A2"] = "Automated aggregation across LinkedIn, YouTube Shorts, Instagram, and Reddit distribution channels."
ws_dash["A2"].font = Font(name="Calibri", size=10, italic=True, color="475569")

kpis = [
    ("B4", "C4", "B5", "C5", "Total Impressions", "=SUM('Content Performance Log'!E4:E100)"),
    ("D4", "E4", "D5", "E5", "Total Saves / Bookmarks", "=SUM('Content Performance Log'!F4:F100)"),
    ("F4", "G4", "F5", "G5", "Total Kit Downloads", "=SUM('Content Performance Log'!K4:K100)"),
    ("B7", "C7", "B8", "C8", "Profile Visits", "=SUM('Content Performance Log'!I4:I100)"),
    ("D7", "E7", "D8", "E8", "Direct Feedback Items", "=COUNTA('Inquiries & Feature Clusters'!A4:A500)"),
    ("F7", "G7", "F8", "G8", "Paid Signals Logged", '=COUNTIF(\'Inquiries & Feature Clusters\'!G4:G500, "Yes")')
]

for top_l, top_r, bot_l, bot_r, label, formula in kpis:
    ws_dash.merge_cells(f"{top_l}:{top_r}")
    ws_dash.merge_cells(f"{bot_l}:{bot_r}")
    ws_dash[top_l] = label
    ws_dash[top_l].font = kpi_title_font
    ws_dash[top_l].alignment = Alignment(horizontal="center", vertical="center")
    ws_dash[top_l].fill = kpi_fill
    ws_dash[bot_l] = formula
    ws_dash[bot_l].font = kpi_num_font
    ws_dash[bot_l].alignment = Alignment(horizontal="center", vertical="center")
    ws_dash[bot_l].fill = kpi_fill
    for c in [top_l[0], top_r[0]]:
        for r in [top_l[1:], bot_l[1:]]:
            ws_dash[f"{c}{r}"].border = kpi_border

# Column widths
ws_dash.column_dimensions["A"].width = 4
for col in ["B", "C", "D", "E", "F", "G"]:
    ws_dash.column_dimensions[col].width = 16

# --- SHEET 2: CONTENT PERFORMANCE LOG ---
content_headers = [
    "Post ID", "Platform", "Publish Date", "Content Hook / Headline",
    "Impressions / Views", "Saves / Bookmarks", "Shares / Reposts", "Comments",
    "Profile Visits", "Link Clicks", "Kit Downloads", "Save Rate %", "Click-to-Download %"
]
ws_log.row_dimensions[3].height = 24
for col_idx, h in enumerate(content_headers, 1):
    cell = ws_log.cell(row=3, column=col_idx, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = kpi_border

# Pre-populate Post 1 planned rows
planned_posts = [
    ("POST-001-LI", "LinkedIn (rohitkalyan505)", "2026-10-02", "5 Things Indian Freshers Should Remove from Their Resumes (Carousel)", 0, 0, 0, 0, 0, 0, 1, "=IF(E4>0, F4/E4, 0)", "=IF(J4>0, K4/J4, 0)"),
    ("POST-001-IG", "Instagram Reel", "TBD", "Stop Using 1990s Biodatas (50s Video)", 0, 0, 0, 0, 0, 0, 0, "=IF(E5>0, F5/E5, 0)", "=IF(J5>0, K5/J5, 0)"),
    ("POST-001-YT", "YouTube Shorts", "TBD", "Why Your Canva Resume Fails ATS Parsing (55s Demo)", 0, 0, 0, 0, 0, 0, 0, "=IF(E6>0, F6/E6, 0)", "=IF(J6>0, K6/J6, 0)"),
    ("POST-001-RD", "Reddit (r/devIndia)", "TBD", "Guide: The 5 Biodata Relics Wasting Fresher Resume Space", 0, 0, 0, 0, 0, 0, 0, "=IF(E7>0, F7/E7, 0)", "=IF(J7>0, K7/J7, 0)")
]

for row_idx, p_data in enumerate(planned_posts, 4):
    ws_log.row_dimensions[row_idx].height = 20
    for col_idx, val in enumerate(p_data, 1):
        cell = ws_log.cell(row=row_idx, column=col_idx, value=val)
        cell.font = Font(name="Calibri", size=9.5, color="1E293B")
        cell.border = kpi_border
        if col_idx in [1, 2, 3]:
            cell.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx in [5, 6, 7, 8, 9, 10, 11]:
            cell.alignment = Alignment(horizontal="right", vertical="center")
        elif col_idx in [12, 13]:
            cell.alignment = Alignment(horizontal="right", vertical="center")
            cell.number_format = '0.0%'

col_widths_log = {'A': 15, 'B': 18, 'C': 14, 'D': 40, 'E': 18, 'F': 18, 'G': 16, 'H': 14, 'I': 16, 'J': 14, 'K': 16, 'L': 14, 'M': 18}
for c_l, w in col_widths_log.items():
    ws_log.column_dimensions[c_l].width = w

# --- SHEET 3: INQUIRIES & FEATURE CLUSTERS ---
inquiry_headers = [
    "Inquiry ID", "Date Logged", "Platform Source", "User Background",
    "Category", "Verbatim Feedback / Request", "Paid Product Signal? (Yes/No)", "Action / Follow-up"
]
ws_req.row_dimensions[3].height = 24
for col_idx, h in enumerate(inquiry_headers, 1):
    cell = ws_req.cell(row=3, column=col_idx, value=h)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = kpi_border

col_widths_req = {'A': 14, 'B': 14, 'C': 18, 'D': 20, 'E': 22, 'F': 45, 'G': 25, 'H': 30}
for c_l, w in col_widths_req.items():
    ws_req.column_dimensions[c_l].width = w

wb.save(xlsx_path)
print(f"[OK] Generated {xlsx_path} ({os.path.getsize(xlsx_path)} bytes)")
