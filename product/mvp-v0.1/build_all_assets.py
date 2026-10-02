"""
Build Script for Fresher Job Application Kit (Free MVP v0.1)
Generates:
1. resume-template.docx (python-docx)
2. resume-template-reference.pdf (HTML -> Edge PDF)
3. resume-removal-checklist.pdf (HTML -> Edge PDF)
4. resume-self-audit.pdf (HTML -> Edge PDF)
5. jd-tailoring-worksheet.pdf (HTML -> Edge PDF)
6. naukri-checklist.pdf (HTML -> Edge PDF)
7. project-bullet-guide.pdf (HTML -> Edge PDF)
8. job-application-tracker.xlsx (openpyxl)
"""

import os
import sys
import subprocess
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def add_p_border_bottom(p, color_hex="111827", sz="12"):
    """Adds a clean solid bottom border to a heading paragraph in docx."""
    pPr = p._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="{sz}" w:space="4" w:color="{color_hex}"/></w:pBdr>')
    pPr.append(pBdr)

def build_docx_resume():
    doc = Document()
    
    # 0.6 inch margins all around
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(0.55)
        s.bottom_margin = Inches(0.55)
        s.left_margin = Inches(0.65)
        s.right_margin = Inches(0.65)
        s.page_width = Inches(8.5)
        s.page_height = Inches(11.0)
        
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37) # slate-800
    
    # --- HEADER ---
    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(2)
    run_name = p_name.add_run("[FIRST NAME] [LAST NAME]")
    run_name.font.size = Pt(19)
    run_name.font.bold = True
    run_name.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A) # slate-900
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(2)
    r_sub = p_sub.add_run("Aspiring Software Development Engineer | B.Tech CSE (Batch 2026)")
    r_sub.font.size = Pt(10.5)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(0x25, 0x63, 0xEB) # blue-600
    
    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_before = Pt(0)
    p_contact.paragraph_format.space_after = Pt(8)
    r_c = p_contact.add_run("[City, State]  •  +91-9876543210  •  name.fresher@email.com  •  linkedin.com/in/yourprofile  •  github.com/yourhandle")
    r_c.font.size = Pt(9.5)
    r_c.font.color.rgb = RGBColor(0x47, 0x55, 0x69) # slate-600

    def add_section_header(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title.upper())
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        add_p_border_bottom(p, "0F172A", "10")
        return p

    # --- 1. EDUCATION ---
    add_section_header("Education")
    
    p_ed1 = doc.add_paragraph()
    p_ed1.paragraph_format.space_before = Pt(2)
    p_ed1.paragraph_format.space_after = Pt(1)
    r1 = p_ed1.add_run("Bachelor of Technology in Computer Science & Engineering")
    r1.font.bold = True
    p_ed1.add_run(" | [College / University Name, City]")
    
    p_ed1_sub = doc.add_paragraph()
    p_ed1_sub.paragraph_format.space_before = Pt(0)
    p_ed1_sub.paragraph_format.space_after = Pt(4)
    p_ed1_sub.add_run("Graduation: Expected June 2026  •  Current CGPA: ")
    r_gpa = p_ed1_sub.add_run("[8.4 / 10.0]")
    r_gpa.font.bold = True
    p_ed1_sub.add_run(" (or [XX]%)")
    
    p_ed2 = doc.add_paragraph()
    p_ed2.paragraph_format.space_before = Pt(0)
    p_ed2.paragraph_format.space_after = Pt(1)
    p_ed2.add_run("Class XII (Senior Secondary) — CBSE / State Board | [School Name, City] | Year: 2022 | Score: [XX]%")
    
    p_ed3 = doc.add_paragraph()
    p_ed3.paragraph_format.space_before = Pt(0)
    p_ed3.paragraph_format.space_after = Pt(4)
    p_ed3.add_run("Class X (Secondary) — CBSE / State Board | [School Name, City] | Year: 2020 | Score: [XX]%")

    # --- 2. TECHNICAL SKILLS ---
    add_section_header("Technical Skills")
    
    skills = [
        ("Programming Languages: ", "Python, Java, C++, JavaScript (ES6+), SQL"),
        ("Frameworks & Web Tech: ", "React.js, Node.js, Express.js, FastAPI / Spring Boot (Basics), HTML5, CSS3, Tailwind CSS"),
        ("Developer Tools & Platforms: ", "Git, GitHub, VS Code, Postman, Linux / Bash, Docker (Basics), Vercel"),
        ("Core CS Fundamentals: ", "Data Structures & Algorithms, Object-Oriented Programming (OOP), DBMS, Operating Systems, Computer Networks")
    ]
    for lbl, val in skills:
        p_sk = doc.add_paragraph()
        p_sk.paragraph_format.space_before = Pt(0)
        p_sk.paragraph_format.space_after = Pt(1.5)
        r_lbl = p_sk.add_run(lbl)
        r_lbl.font.bold = True
        p_sk.add_run(val)

    # --- 3. ACADEMIC & TECHNICAL PROJECTS ---
    add_section_header("Academic & Technical Projects")
    
    # Project 1
    p_p1 = doc.add_paragraph()
    p_p1.paragraph_format.space_before = Pt(2)
    p_p1.paragraph_format.space_after = Pt(1)
    r_p1_t = p_p1.add_run("[Full-Stack E-Commerce Platform]")
    r_p1_t.font.bold = True
    p_p1.add_run(" | Tech Stack: React.js, Node.js, Express, MongoDB, Stripe API")
    
    p_p1_l = doc.add_paragraph()
    p_p1_l.paragraph_format.space_before = Pt(0)
    p_p1_l.paragraph_format.space_after = Pt(1)
    r_links = p_p1_l.add_run("GitHub: github.com/username/project-repo  •  Live Demo: project-demo.vercel.app")
    r_links.font.size = Pt(9)
    r_links.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
    
    p_b1 = doc.add_paragraph(style='List Bullet')
    p_b1.paragraph_format.space_before = Pt(0)
    p_b1.paragraph_format.space_after = Pt(1)
    p_b1.add_run("Architected a responsive full-stack web store with JWT-based authentication and role-based access control for customers and store managers.")
    
    p_b2 = doc.add_paragraph(style='List Bullet')
    p_b2.paragraph_format.space_before = Pt(0)
    p_b2.paragraph_format.space_after = Pt(1)
    p_b2.add_run("Implemented product search with debounced filters and integrated Stripe checkout API in sandbox mode for test payment processing.")
    
    p_b3 = doc.add_paragraph(style='List Bullet')
    p_b3.paragraph_format.space_before = Pt(0)
    p_b3.paragraph_format.space_after = Pt(4)
    p_b3.add_run("Optimized MongoDB queries using indexing on product category fields, decreasing local query response time from 140ms to 45ms.")

    # Project 2
    p_p2 = doc.add_paragraph()
    p_p2.paragraph_format.space_before = Pt(2)
    p_p2.paragraph_format.space_after = Pt(1)
    r_p2_t = p_p2.add_run("[RESTful Task Management API]")
    r_p2_t.font.bold = True
    p_p2.add_run(" | Tech Stack: Python, FastAPI, SQLite, Pydantic, PyTest, Docker")
    
    p_p2_l = doc.add_paragraph()
    p_p2_l.paragraph_format.space_before = Pt(0)
    p_p2_l.paragraph_format.space_after = Pt(1)
    r_links2 = p_p2_l.add_run("GitHub: github.com/username/task-api-service")
    r_links2.font.size = Pt(9)
    r_links2.font.color.rgb = RGBColor(0x25, 0x63, 0xEB)
    
    p_b21 = doc.add_paragraph(style='List Bullet')
    p_b21.paragraph_format.space_before = Pt(0)
    p_b21.paragraph_format.space_after = Pt(1)
    p_b21.add_run("Developed backend REST API endpoints with request schema validation using Pydantic and automated Swagger OpenAPI documentation.")
    
    p_b22 = doc.add_paragraph(style='List Bullet')
    p_b22.paragraph_format.space_before = Pt(0)
    p_b22.paragraph_format.space_after = Pt(1)
    p_b22.add_run("Authored 22 automated unit and integration test cases using PyTest, reaching 85% test coverage across core CRUD endpoints.")
    
    p_b23 = doc.add_paragraph(style='List Bullet')
    p_b23.paragraph_format.space_before = Pt(0)
    p_b23.paragraph_format.space_after = Pt(4)
    p_b23.add_run("Containerized the application using Docker and configured a GitHub Actions CI pipeline to run tests automatically on git push.")

    # --- 4. PRACTICAL EXPERIENCE / INTERNSHIP ---
    add_section_header("Experience & Practical Work")
    
    p_exp = doc.add_paragraph()
    p_exp.paragraph_format.space_before = Pt(2)
    p_exp.paragraph_format.space_after = Pt(1)
    r_exp_t = p_exp.add_run("Software Development Intern (or Open Source Contributor)")
    r_exp_t.font.bold = True
    p_exp.add_run(" | [Company / Community Name, Location / Remote]  •  [June 2025 – August 2025]")
    
    p_exp_b1 = doc.add_paragraph(style='List Bullet')
    p_exp_b1.paragraph_format.space_before = Pt(0)
    p_exp_b1.paragraph_format.space_after = Pt(1)
    p_exp_b1.add_run("Assisted development team in refactoring legacy JavaScript utility modules into TypeScript, improving static typing and code reliability.")
    
    p_exp_b2 = doc.add_paragraph(style='List Bullet')
    p_exp_b2.paragraph_format.space_before = Pt(0)
    p_exp_b2.paragraph_format.space_after = Pt(4)
    p_exp_b2.add_run("Resolved 6 bug tickets in the sprint backlog related to responsive layout rendering, collaborating via Git feature branches and pull request reviews.")

    # --- 5. CERTIFICATIONS & ACHIEVEMENTS ---
    add_section_header("Certifications & Verified Achievements")
    
    achievements = [
        ("Competitive Problem Solving: ", "Solved 350+ DSA problems on LeetCode / GeeksforGeeks (Focus on Arrays, Strings, Trees, and Dynamic Programming)."),
        ("Technical Certification: ", "[Course / Certification Name, e.g., Meta Front-End Developer Professional Certificate or AWS Certified Cloud Practitioner], [Year]."),
        ("Hackathon / Academic Achievement: ", "Finalist / Top 10 Team in [Hackathon Name, e.g., Smart India Hackathon Internal / College Hackathon 2025] out of 100+ participating teams.")
    ]
    for lbl, val in achievements:
        p_ac = doc.add_paragraph(style='List Bullet')
        p_ac.paragraph_format.space_before = Pt(0)
        p_ac.paragraph_format.space_after = Pt(1.5)
        r_a = p_ac.add_run(lbl)
        r_a.font.bold = True
        p_ac.add_run(val)
        
    out_path = os.path.join(BASE_DIR, "resume-template.docx")
    doc.save(out_path)
    print(f"[OK] Generated {out_path} ({os.path.getsize(out_path)} bytes)")

def convert_html_to_pdf(html_content, output_pdf_name):
    temp_html = os.path.join(BASE_DIR, f"temp_{output_pdf_name}.html")
    output_pdf = os.path.join(BASE_DIR, output_pdf_name)
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        temp_html
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)
        
    if os.path.exists(output_pdf):
        print(f"[OK] Generated {output_pdf_name} ({os.path.getsize(output_pdf)} bytes)")
    else:
        print(f"[ERROR] Failed to generate {output_pdf_name}: {res.stderr}")

def build_pdf_resume_reference():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>ATS Single-Column Fresher Resume Reference</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }
  body {
    font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    color: #1f2937;
    line-height: 1.25;
    font-size: 9.8pt;
    margin: 0;
    padding: 0;
  }
  .header {
    text-align: center;
    margin-bottom: 8px;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 6px;
  }
  .name {
    font-size: 19pt;
    font-weight: bold;
    color: #0f172a;
    margin: 0 0 2px 0;
    letter-spacing: 0.5px;
  }
  .target-title {
    font-size: 10.5pt;
    font-weight: bold;
    color: #2563eb;
    margin: 0 0 4px 0;
  }
  .contact-info {
    font-size: 9pt;
    color: #475569;
  }
  .contact-info a {
    color: #2563eb;
    text-decoration: none;
  }
  .section-title {
    font-size: 11pt;
    font-weight: bold;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.75px;
    border-bottom: 1px solid #0f172a;
    padding-bottom: 1px;
    margin: 7px 0 4px 0;
  }
  .item-header {
    display: flex;
    justify-content: space-between;
    font-weight: bold;
    color: #0f172a;
    margin-top: 3px;
  }
  .item-sub {
    color: #475569;
    font-size: 9pt;
    margin-bottom: 2px;
  }
  .item-links {
    font-size: 8.8pt;
    color: #2563eb;
    margin-bottom: 2px;
  }
  ul {
    margin: 2px 0 4px 16px;
    padding: 0;
  }
  li {
    margin-bottom: 2px;
    line-height: 1.28;
  }
  .skills-row {
    margin-bottom: 2.5px;
    line-height: 1.3;
  }
  .skills-lbl {
    font-weight: bold;
    color: #0f172a;
  }
</style>
</head>
<body>

<div class="header">
  <div class="name">ROHIT SHARMA</div>
  <div class="target-title">Aspiring Software Development Engineer | B.Tech CSE (Batch 2026)</div>
  <div class="contact-info">
    Bengaluru, Karnataka  •  +91-9876543210  •  rohit.sharma.dev@email.com  •  
    <a href="#">linkedin.com/in/rohit-sharma-dev</a>  •  
    <a href="#">github.com/rohitsharma-code</a>
  </div>
</div>

<div class="section-title">Education</div>
<div class="item-header">
  <span>Bachelor of Technology in Computer Science & Engineering</span>
  <span>Expected: June 2026</span>
</div>
<div class="item-sub">
  National Institute of Technology Karnataka (NITK)  •  Current CGPA: <strong>8.45 / 10.0</strong>
</div>
<div style="font-size: 9pt; color: #334155; margin-top: 2px;">
  Class XII (Senior Secondary) — CBSE | Delhi Public School | Year: 2022 | Score: <strong>91.4%</strong><br>
  Class X (Secondary) — CBSE | Delhi Public School | Year: 2020 | Score: <strong>94.2%</strong>
</div>

<div class="section-title">Technical Skills</div>
<div class="skills-row"><span class="skills-lbl">Programming Languages:</span> Python, Java, C++, JavaScript (ES6+), SQL</div>
<div class="skills-row"><span class="skills-lbl">Frameworks & Web Tech:</span> React.js, Node.js, Express.js, FastAPI, Spring Boot (Basics), HTML5, CSS3, Tailwind CSS</div>
<div class="skills-row"><span class="skills-lbl">Developer Tools & Platforms:</span> Git, GitHub, VS Code, Postman, Linux (Ubuntu), Docker (Basics), Vercel</div>
<div class="skills-row"><span class="skills-lbl">Core CS Fundamentals:</span> Data Structures & Algorithms, Object-Oriented Programming (OOP), DBMS, Operating Systems, Computer Networks</div>

<div class="section-title">Academic & Technical Projects</div>

<div class="item-header">
  <span>Full-Stack E-Commerce Platform</span>
  <span>React.js, Node.js, Express, MongoDB, Stripe API</span>
</div>
<div class="item-links">
  GitHub: github.com/rohitsharma-code/fullstack-ecommerce  •  Live Demo: shop-ease-demo.vercel.app
</div>
<ul>
  <li>Architected a responsive full-stack store with JWT authentication and role-based access control for customers and admins.</li>
  <li>Engineered a dynamic product catalog featuring debounced search filtering and integrated Stripe checkout API in sandbox mode.</li>
  <li>Optimized MongoDB queries via compound indexing on product category fields, reducing local query latency from 140ms to 45ms.</li>
</ul>

<div class="item-header">
  <span>RESTful Task & Microservice API</span>
  <span>Python, FastAPI, SQLite, Pydantic, PyTest, Docker</span>
</div>
<div class="item-links">
  GitHub: github.com/rohitsharma-code/fastapi-task-service
</div>
<ul>
  <li>Developed modular REST endpoints with schema validation using Pydantic and automated Swagger OpenAPI interactive documentation.</li>
  <li>Authored 22 automated unit and integration tests using PyTest, achieving 88% statement coverage across core business logic.</li>
  <li>Containerized application using multi-stage Docker builds and built a GitHub Actions CI pipeline to run test suites on commit.</li>
</ul>

<div class="section-title">Practical Experience & Internships</div>
<div class="item-header">
  <span>Software Engineering Intern</span>
  <span>June 2025 – August 2025</span>
</div>
<div class="item-sub">NexTech Labs Pvt. Ltd. | Bengaluru, Karnataka (Hybrid)</div>
<ul>
  <li>Assisted a 5-person engineering squad in refactoring legacy JavaScript client modules into TypeScript, reducing runtime type errors.</li>
  <li>Implemented 4 reusable UI components complying with the internal design system and verified cross-browser compatibility.</li>
  <li>Participated in bi-weekly sprint planning, daily standups, and collaborated via Git feature branches and peer code reviews.</li>
</ul>

<div class="section-title">Certifications & Verified Achievements</div>
<ul>
  <li><strong>Competitive Problem Solving:</strong> Solved 380+ DSA questions across LeetCode & GeeksforGeeks; Knight badge / 1850+ contest rating.</li>
  <li><strong>Certification:</strong> Meta Front-End Developer Professional Certificate (Coursera / DeepLearning.AI), 2025.</li>
  <li><strong>Hackathon Achievement:</strong> Finalist (Top 8 of 115 teams) in HackNITK 2025 for developing an offline campus resource navigator.</li>
</ul>

</body>
</html>"""
    convert_html_to_pdf(html, "resume-template-reference.pdf")

def build_pdf_removal_checklist():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>What to Remove From Your Resume</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }
  body {
    font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.3;
    font-size: 9.5pt;
    margin: 0;
  }
  .header {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 6px;
    margin-bottom: 10px;
  }
  h1 {
    font-size: 16pt;
    color: #0f172a;
    margin: 0 0 3px 0;
  }
  .sub {
    font-size: 9pt;
    color: #475569;
  }
  .badge {
    display: inline-block;
    background: #e2e8f0;
    color: #0f172a;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: bold;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    font-size: 9pt;
  }
  th {
    background-color: #0f172a;
    color: #ffffff;
    text-align: left;
    padding: 6px 8px;
    font-weight: 600;
  }
  td {
    padding: 6px 8px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
  }
  tr:nth-child(even) td {
    background-color: #f8fafc;
  }
  .remove-item {
    font-weight: bold;
    color: #dc2626;
  }
  .why-box {
    color: #334155;
  }
  .exception-box {
    color: #0369a1;
    font-style: italic;
  }
  .callout {
    background: #f1f5f9;
    border-left: 4px solid #2563eb;
    padding: 8px 10px;
    margin-top: 10px;
    font-size: 8.8pt;
    color: #1e293b;
  }
  .callout strong {
    color: #0f172a;
  }
</style>
</head>
<body>

<div class="header">
  <div style="float: right;"><span class="badge">FREE MVP v0.1</span> <span class="badge">QUICK-AUDIT</span></div>
  <h1>WHAT TO REMOVE FROM YOUR RESUME</h1>
  <div class="sub">Indian Fresher Off-Campus Edition  •  Eradicate 1990s Biodata Clutter & Protect Resume Real Estate</div>
</div>

<div class="callout">
  <strong>Guiding Principle:</strong> Resumes are contextual. In modern off-campus tech and corporate recruiting, vertical space is precious. Every line must demonstrate technical competence, problem-solving, or engineering scope. Distinguish between <em>general private-sector best practice</em> and <em>specific employer exceptions</em>.
</div>

<table>
  <thead>
    <tr>
      <th style="width: 24%;">Item to Remove</th>
      <th style="width: 44%;">Why It Hurts Your Resume</th>
      <th style="width: 32%;">Legitimate Exceptions (When to Keep)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="remove-item">1. Father’s / Mother’s Name & Occupation</td>
      <td class="why-box">Irrelevant to your technical ability. Wastes 2–3 lines. Standard tech recruiters view family details as archaic biodata relics.</td>
      <td class="exception-box">Government job forms, PSU background checks, or specific campus placement biodata forms where explicitly mandated.</td>
    </tr>
    <tr>
      <td class="remove-item">2. Marital Status, Religion, Caste & Gender</td>
      <td class="why-box">Completely irrelevant to professional hiring and introduces unconscious bias. Standard private employers do not evaluate this.</td>
      <td class="exception-box">Statutory affirmative action / reservation forms in official government portals (UPSC/SSC/State PSCs).</td>
    </tr>
    <tr>
      <td class="remove-item">3. Full Street Address & Door Number</td>
      <td class="why-box">Privacy risk when uploading to multiple job boards. Recruiters only need to know your current city and relocation willingness.</td>
      <td class="exception-box">Physical document verification after receiving an offer letter; background checks. Use <code>City, State</code> on resume.</td>
    </tr>
    <tr>
      <td class="remove-item">4. Candidate Photograph / Headshot</td>
      <td class="why-box">In Indian tech off-campus applications, photos waste space, risk bias, and can confuse text extraction in older optical parsers.</td>
      <td class="exception-box">Aviation, hospitality, media/acting, modeling, or European countries (e.g. Germany/France) where photos are conventional.</td>
    </tr>
    <tr>
      <td class="remove-item">5. Formal "Declaration" & Signature Block</td>
      <td class="why-box"><em>"I hereby declare that all information..."</em> wastes 4 lines of prime space. Submitting an application implies truthfulness.</td>
      <td class="exception-box">Hard-copy physical submissions for traditional government, banking, or defense exams.</td>
    </tr>
    <tr>
      <td class="remove-item">6. Skill Percentage Rating Bars (e.g. "Java: 85%")</td>
      <td class="why-box">Subjective and meaningless. Recruiters ask: <em>"85% of what? Did you invent the compiler?"</em> It invites difficult interview grilling.</td>
      <td class="exception-box">None in technical engineering. Replace with real projects that demonstrate the skill in action.</td>
    </tr>
    <tr>
      <td class="remove-item">7. Vague Hobbies ("Listening to music")</td>
      <td class="why-box">Listing generic leisure activities looks like white-space filler. It provides zero signal of teamwork or technical curiosity.</td>
      <td class="exception-box">Keep only if exceptional and relevant (e.g. Open Source contributor, Tech community organizer, National chess medalist).</td>
    </tr>
    <tr>
      <td class="remove-item">8. Middle School / Elementary School Records</td>
      <td class="why-box">Listing 8th grade marks or primary school awards displays lack of recent achievements. Keep only Class 12 & 10.</td>
      <td class="exception-box">None. Freshers should focus on College, Class 12, and Class 10.</td>
    </tr>
    <tr>
      <td class="remove-item">9. 25+ Disparate Skill Buzzwords</td>
      <td class="why-box">Listing every tool you ever looked at (Docker, Kubernetes, AWS, C, Python, Flutter, AI) damages credibility when quizzed.</td>
      <td class="exception-box">List only skills you can defend in a live technical screen. Group skills cleanly by Language, Framework, and Tool.</td>
    </tr>
    <tr>
      <td class="remove-item">10. "Career Objective" Paragraphs</td>
      <td class="why-box"><em>"To obtain a challenging position in an esteemed company where I can enhance my skills..."</em> is generic filler.</td>
      <td class="exception-box">Replace with a 1-line crisp target title (e.g. <em>"Aspiring SDE | B.Tech CSE 2026"</em>) or jump directly to Education/Skills.</td>
    </tr>
  </tbody>
</table>

<div class="callout" style="margin-top: 8px;">
  <strong>Self-Check Rule:</strong> If an item does not help a technical hiring manager decide to interview you, <strong>delete it</strong>. Reclaim that space for project architecture, GitHub links, and measurable outcomes.
</div>

</body>
</html>"""
    convert_html_to_pdf(html, "resume-removal-checklist.pdf")

def build_pdf_self_audit():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Indian Fresher Resume Self-Audit Checklist</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }
  body {
    font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.25;
    font-size: 8.8pt;
    margin: 0;
  }
  .header {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 5px;
    margin-bottom: 8px;
  }
  h1 {
    font-size: 15pt;
    color: #0f172a;
    margin: 0 0 2px 0;
  }
  .sub {
    font-size: 8.5pt;
    color: #475569;
  }
  .badge {
    display: inline-block;
    background: #e2e8f0;
    color: #0f172a;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: bold;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 6px;
  }
  th {
    background-color: #0f172a;
    color: #ffffff;
    text-align: left;
    padding: 4px 6px;
    font-size: 8.5pt;
  }
  td {
    padding: 3.5px 6px;
    border-bottom: 1px solid #cbd5e1;
    vertical-align: middle;
  }
  tr:nth-child(even) td {
    background-color: #f8fafc;
  }
  .box {
    width: 14px;
    height: 14px;
    border: 1.5px solid #475569;
    border-radius: 2px;
    display: inline-block;
  }
  .cat-badge {
    font-weight: bold;
    color: #1e40af;
    font-size: 8pt;
  }
  .rule-text {
    font-weight: bold;
    color: #0f172a;
  }
  .rule-desc {
    color: #475569;
    font-size: 8.2pt;
  }
  .callout {
    background: #f1f5f9;
    border-left: 3px solid #2563eb;
    padding: 6px 8px;
    margin-top: 8px;
    font-size: 8.2pt;
  }
</style>
</head>
<body>

<div class="header">
  <div style="float: right;"><span class="badge">FREE MVP v0.1</span> <span class="badge">20-POINT AUDIT</span></div>
  <h1>INDIAN FRESHER RESUME SELF-AUDIT</h1>
  <div class="sub">Pass / Fail Quality Verification Protocol  •  Run This Complete Audit Before Submitting Any Off-Campus Application</div>
</div>

<table>
  <thead>
    <tr>
      <th style="width: 5%; text-align: center;">#</th>
      <th style="width: 18%;">Category</th>
      <th style="width: 67%;">Audit Verification Criteria</th>
      <th style="width: 10%; text-align: center;">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center; font-weight: bold;">1</td>
      <td><span class="cat-badge">Contact Info</span></td>
      <td><span class="rule-text">Professional Email ID:</span> Uses standard firstname.lastname format. No unprofessional nicknames or slang handles.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">2</td>
      <td><span class="cat-badge">Contact Info</span></td>
      <td><span class="rule-text">Valid Phone & City:</span> Active mobile number with <code>+91</code> country code; City and State listed without full door/street address.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">3</td>
      <td><span class="cat-badge">Digital Links</span></td>
      <td><span class="rule-text">Working LinkedIn Profile:</span> Clean, custom URL included and verified to open properly without 404 error.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">4</td>
      <td><span class="cat-badge">Digital Links</span></td>
      <td><span class="rule-text">Working GitHub / Portfolio:</span> Links to active account with clean READMEs, pinned repositories, and actual code.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">5</td>
      <td><span class="cat-badge">Section Order</span></td>
      <td><span class="rule-text">Logical Hierarchy:</span> Contact Header → Education → Technical Skills → Projects → Experience → Achievements.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">6</td>
      <td><span class="cat-badge">Education</span></td>
      <td><span class="rule-text">Degree & Batch Explicit:</span> Full degree name, branch/specialization, college name, and expected passing month & year clearly stated.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">7</td>
      <td><span class="cat-badge">Education</span></td>
      <td><span class="rule-text">Transparent CGPA/Percentage:</span> CGPA stated with scale (e.g. <code>8.4 / 10.0</code>) or percentage. Class 12 & 10 listed in 1 line each.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">8</td>
      <td><span class="cat-badge">Technical Skills</span></td>
      <td><span class="rule-text">Categorized Skills:</span> Grouped logically by Languages, Frameworks, Tools, and Core CS Fundamentals (no unorganized tag soup).</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">9</td>
      <td><span class="cat-badge">Technical Skills</span></td>
      <td><span class="rule-text">Defensibility Test:</span> Every single technology listed is one you have written code in and can answer interview questions on.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">10</td>
      <td><span class="cat-badge">Projects</span></td>
      <td><span class="rule-text">At Least 2 Real Projects:</span> Projects clearly identify technologies used, repo links, and what problem was solved.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">11</td>
      <td><span class="cat-badge">Project Bullets</span></td>
      <td><span class="rule-text">Formula Adherence:</span> Bullets follow <code>[Action Verb] + [Technical Context / Architecture] + [Outcome / Metric]</code>.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">12</td>
      <td><span class="cat-badge">Project Bullets</span></td>
      <td><span class="rule-text">No Passive Descriptions:</span> No passive phrases like <em>"Was responsible for"</em> or <em>"Worked on"</em>; replaced with active verbs like <em>Engineered, Developed</em>.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">13</td>
      <td><span class="cat-badge">Layout & Structure</span></td>
      <td><span class="rule-text">Strict Single-Column:</span> Linear flow from top to bottom. Zero 2-column splits, floating text boxes, or graphic sidebars.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">14</td>
      <td><span class="cat-badge">Layout & Structure</span></td>
      <td><span class="rule-text">No Layout Tables:</span> Tables are not used to structure text columns (as multi-column table layouts can cause text-order or parsing issues in some ATS systems).</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">15</td>
      <td><span class="cat-badge">Typography</span></td>
      <td><span class="rule-text">Clean Universal Font:</span> Standard readable font (Calibri, Arial, or Times), 10–11pt body text, consistent line spacing.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">16</td>
      <td><span class="cat-badge">Page Budget</span></td>
      <td><span class="rule-text">Strict 1-Page Rule:</span> The resume fits completely on exactly 1 page with no orphan 2nd page containing 3 stray lines.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">17</td>
      <td><span class="cat-badge">Text Selectability</span></td>
      <td><span class="rule-text">Ctrl+A Text Copy Test:</span> Pressing Ctrl+A on the PDF selects clean ASCII text; pasting into Notepad pastes readable words.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">18</td>
      <td><span class="cat-badge">De-Clutter Check</span></td>
      <td><span class="rule-text">Zero Biodata Relics:</span> No Father's name, photo, marital status, full home address, or formal declaration paragraph.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">19</td>
      <td><span class="cat-badge">Tailoring Check</span></td>
      <td><span class="rule-text">JD Keyword Alignment:</span> The 3–5 core technical keywords required in the target JD are accurately reflected in your genuine skills.</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: bold;">20</td>
      <td><span class="cat-badge">File Naming</span></td>
      <td><span class="rule-text">Professional File Name:</span> Saved as <code>FirstName_LastName_Resume.pdf</code> (NOT <code>resume_updated_final(1).pdf</code>).</td>
      <td style="text-align: center;"><div class="box"></div></td>
    </tr>
  </tbody>
</table>

<div class="callout">
  <strong>Pass Standard:</strong> You should achieve <strong>20 / 20</strong> before submitting off-campus. If any point fails, fix it immediately in your source <code>.docx</code> file and re-export.
</div>

</body>
</html>"""
    convert_html_to_pdf(html, "resume-self-audit.pdf")

def build_pdf_jd_tailoring():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>10-Minute Job Description Tailoring Worksheet</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }
  body {
    font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.28;
    font-size: 9pt;
    margin: 0;
  }
  .header {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 5px;
    margin-bottom: 8px;
  }
  h1 {
    font-size: 15pt;
    color: #0f172a;
    margin: 0 0 2px 0;
  }
  .sub {
    font-size: 8.5pt;
    color: #475569;
  }
  .badge {
    display: inline-block;
    background: #e2e8f0;
    color: #0f172a;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: bold;
  }
  h2 {
    font-size: 11pt;
    color: #0f172a;
    margin: 8px 0 4px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .step-grid {
    display: flex;
    gap: 8px;
    margin-bottom: 8px;
  }
  .step-card {
    flex: 1;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 8px;
  }
  .step-num {
    font-weight: bold;
    color: #2563eb;
    font-size: 8.5pt;
  }
  .step-title {
    font-weight: bold;
    color: #0f172a;
    margin-bottom: 3px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 6px;
    font-size: 8.5pt;
  }
  th {
    background-color: #0f172a;
    color: #ffffff;
    text-align: left;
    padding: 5px 6px;
  }
  td {
    padding: 6px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
  }
  .fill-cell {
    background-color: #ffffff;
    min-height: 28px;
    color: #64748b;
  }
  .warning-box {
    background: #fef2f2;
    border-left: 4px solid #ef4444;
    padding: 6px 8px;
    margin-top: 8px;
    color: #991b1b;
    font-size: 8.5pt;
  }
  .example-box {
    background: #f0fdf4;
    border-left: 4px solid #16a34a;
    padding: 6px 8px;
    margin-top: 6px;
    color: #166534;
    font-size: 8.3pt;
  }
</style>
</head>
<body>

<div class="header">
  <div style="float: right;"><span class="badge">FREE MVP v0.1</span> <span class="badge">TACTICAL WORKSHEET</span></div>
  <h1>10-MINUTE JOB DESCRIPTION (JD) TAILORING WORKSHEET</h1>
  <div class="sub">How to Reverse-Engineer a Fresher Job Posting & Align Genuine Project Experience Without Fabricating Skills</div>
</div>

<div class="step-grid">
  <div class="step-card">
    <div class="step-num">STEP 1 (3 Mins)</div>
    <div class="step-title">Scan & Extract</div>
    Underline 3 Hard Technical Skills, 2 Developer Tools, and 1 Core CS Fundamental from the JD requirements.
  </div>
  <div class="step-card">
    <div class="step-num">STEP 2 (2 Mins)</div>
    <div class="step-title">Truthful Audit</div>
    Cross-reference with your actual projects. Do you have genuine code evidence? If yes, proceed. If no, never fake it.
  </div>
  <div class="step-card">
    <div class="step-num">STEP 3 (3 Mins)</div>
    <div class="step-title">Align Phrasing</div>
    Adopt the exact standard technical phrasing used in the JD (e.g. change <em>"API creation"</em> to <em>"RESTful API Development"</em>).
  </div>
  <div class="step-card">
    <div class="step-num">STEP 4 (2 Mins)</div>
    <div class="step-title">Reorder Bullets</div>
    Place your most relevant project at the top and ensure the first bullet point directly highlights the required stack.
  </div>
</div>

<h2>Practical Demonstration Walkthrough</h2>
<div class="example-box">
  <strong>FICTIONAL DEMONSTRATION EXAMPLE — DO NOT COPY DIRECTLY:</strong><br>
  <strong>Target Job Posting Requires:</strong> <em>"Strong understanding of Python, RESTful API architecture, relational database queries (SQL), and automated testing."</em><br>
  <strong>Candidate's Actual Experience:</strong> Built a college task manager project using Python (FastAPI), SQLite, and tested endpoints with PyTest.<br>
  <strong>Before Tailoring:</strong> "Made a backend task manager website using Python and SQLite database."<br>
  <strong>After Tailoring:</strong> "Engineered RESTful API service with FastAPI and relational SQLite schema; authored 20+ automated unit tests in PyTest covering all CRUD endpoints." (100% truthful, perfectly aligned).
</div>

<h2>Worksheet: Job Alignment Matrix (Fill for Target Role)</h2>
<table>
  <thead>
    <tr>
      <th style="width: 25%;">JD Term / Requirement</th>
      <th style="width: 25%;">My Truthful Experience / Project Evidence</th>
      <th style="width: 28%;">Updated Resume Phrasing</th>
      <th style="width: 22%;">Interview Defense Talking Point</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><em>Example: RESTful APIs & SQL</em></td>
      <td>Built FastAPI backend with SQLite in Capstone project</td>
      <td>Engineered RESTful endpoints in FastAPI with relational schema</td>
      <td>Can explain HTTP methods, status codes, query joins, and indexing</td>
    </tr>
    <tr>
      <td class="fill-cell">1. Primary Hard Skill:</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
    </tr>
    <tr>
      <td class="fill-cell">2. Secondary Tool / Framework:</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
    </tr>
    <tr>
      <td class="fill-cell">3. Database / Infrastructure:</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
    </tr>
    <tr>
      <td class="fill-cell">4. Core CS Concept / Testing:</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
      <td class="fill-cell">&nbsp;</td>
    </tr>
  </tbody>
</table>

<div class="warning-box">
  <strong>NON-NEGOTIABLE ETHICAL BOUNDARY:</strong> Tailoring means highlighting and translating your <em>genuine capabilities</em> into the vocabulary used by the recruiter. Never add technologies you have never installed, never written code for, or cannot defend under scrutiny. Disqualification during an interview screen damages your reputation and wastes your time.
</div>

</body>
</html>"""
    convert_html_to_pdf(html, "jd-tailoring-worksheet.pdf")

def build_pdf_naukri_checklist():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Naukri Profile Optimization Checklist</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }
  body {
    font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.28;
    font-size: 8.8pt;
    margin: 0;
  }
  .header {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 5px;
    margin-bottom: 8px;
  }
  h1 {
    font-size: 15pt;
    color: #0f172a;
    margin: 0 0 2px 0;
  }
  .sub {
    font-size: 8.5pt;
    color: #475569;
  }
  .badge {
    display: inline-block;
    background: #e2e8f0;
    color: #0f172a;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: bold;
  }
  h2 {
    font-size: 10pt;
    color: #0f172a;
    margin: 7px 0 3px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
  }
  .grid {
    display: flex;
    gap: 8px;
    margin-bottom: 6px;
  }
  .col {
    flex: 1;
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 8px;
  }
  .callout {
    background: #f1f5f9;
    border-left: 3px solid #2563eb;
    padding: 5px 8px;
    margin-top: 6px;
    font-size: 8.2pt;
  }
  .scam-box {
    background: #fef2f2;
    border-left: 3px solid #ef4444;
    padding: 5px 8px;
    margin-top: 6px;
    color: #991b1b;
    font-size: 8.2pt;
  }
  ul {
    margin: 2px 0 4px 14px;
    padding: 0;
  }
  li {
    margin-bottom: 2px;
  }
  code {
    background: #e2e8f0;
    padding: 1px 4px;
    border-radius: 2px;
    font-size: 8pt;
  }
</style>
</head>
<body>

<div class="header">
  <div style="float: right;"><span class="badge">FREE MVP v0.1</span> <span class="badge">PLATFORM GUIDE</span></div>
  <h1>NAUKRI.COM PROFILE OPTIMIZATION CHECKLIST</h1>
  <div class="sub">Recruiter Search Mechanics (Resdex)  •  Profile Completeness  •  Scam Defense for Indian Freshers</div>
</div>

<div class="callout">
  <strong>Evidence Discipline Notice:</strong> This checklist separates <em>verifiable platform features</em> (FACT) from <em>reported recruiter search behaviors</em> (RECRUITER WORKFLOW OBSERVATION) and <em>practical recommendations</em> (GUIDANCE - REQUIRES PERIODIC VERIFICATION). We do not claim any single update frequency or score guarantees interview callbacks.
</div>

<div class="grid">
  <div class="col">
    <div style="font-weight: bold; color: #0f172a; margin-bottom: 3px;">1. Profile Score & Completeness (FACT)</div>
    <div style="font-size: 8.2pt; color: #475569; margin-bottom: 4px;">Naukri displays a profile completeness gauge (0–100%). Incomplete sections can leave required recruiter search fields blank.</div>
    <ul>
      <li><strong>Target High Completeness:</strong> Complete all relevant sections (Education, Projects, Skills, Summary).</li>
      <li><strong>Verified Credentials:</strong> Verify primary mobile number and email ID (verified status badge).</li>
      <li><strong>Current Designation:</strong> For freshers, enter <code>Fresher / Graduate Trainee</code> or <code>B.Tech CSE Student (2026 Batch)</code>.</li>
    </ul>
  </div>

  <div class="col">
    <div style="font-weight: bold; color: #0f172a; margin-bottom: 3px;">2. Recruiter Search Recency (WORKFLOW GUIDANCE - REQUIRES PERIODIC VERIFICATION)</div>
    <div style="font-size: 8.2pt; color: #475569; margin-bottom: 4px;">Recruitment industry sources report that recruiters often apply activity filters (e.g. active in last 15–30 days) to find responsive candidates.</div>
    <ul>
      <li><strong>Weekly Profile Check (Suggested Routine):</strong> Log in every 5–7 days to review notifications and keep details current. (Algorithmic impact of text edits is unverified by platform docs).</li>
      <li><strong>Job Seeking Status:</strong> Set availability to <code>Actively Looking for Jobs</code> and Notice Period to <code>Immediate / 0 Days</code>.</li>
    </ul>
  </div>
</div>

<h2>3. Resume Headline Formula (Character Limit: ~250 Characters)</h2>
<p style="margin: 2px 0 4px 0; font-size: 8.3pt;">Your headline is the primary text snippet visible to a recruiter in search results before clicking your profile. Do not leave it blank.</p>
<div style="background: #ffffff; border: 1px dashed #2563eb; padding: 6px; border-radius: 4px; margin-bottom: 6px;">
  <strong>Recommended Formula:</strong> <code>[Degree + Specialization + Batch] | [Core Tech Stack] | [Target Role] | [Key Project / Focus]</code><br>
  <em>Example:</em> <code>B.Tech CSE 2026 Graduate | Java, Spring Boot, SQL, REST APIs | Aspiring SDE-1 / Software Intern | Hands-on Microservices Project Experience</code>
</div>

<h2>4. Key Skills Architecture (Crucial Search Index Field)</h2>
<ul>
  <li><strong>Use Exact Terminology:</strong> Recruiters query exact keywords. Add both specific frameworks and parent categories (e.g. add both <code>React.js</code> and <code>JavaScript</code>).</li>
  <li><strong>Utilize Available Tags:</strong> Add 15–25 high-priority technical skills relevant to your domain. Do not waste slots on vague adjectives (e.g. avoid <em>"Hardworking", "Punctual", "Fast Learner"</em>).</li>
  <li><strong>Separate Domains:</strong> Categorize: <strong>Languages</strong> (Python, Java), <strong>Databases</strong> (PostgreSQL, MySQL), <strong>Tools</strong> (Git, Postman, Linux), <strong>Concepts</strong> (DSA, OOP, System Design).</li>
</ul>

<h2>5. Profile Summary (Professional Snapshot)</h2>
<p style="margin: 2px 0 4px 0; font-size: 8.3pt;">Write a clean 3–4 sentence summary avoiding generic corporate clichés:</p>
<div style="background: #f8fafc; border: 1px solid #cbd5e1; padding: 5px 8px; border-radius: 4px; font-size: 8.2pt; color: #334155;">
  <em>"B.Tech Computer Science student graduating in 2026 with practical project experience in full-stack web engineering (React, Node.js) and relational database design. Proficient in Data Structures and Algorithms in Java/Python with 350+ solved challenges. Actively seeking SDE-1 or software engineering internship opportunities."</em>
</div>

<div class="scam-box">
  <strong>RECRUITMENT SCAM DEFENSE FOR FRESHERS (OFFICIAL POLICY WARNING):</strong><br>
  • Legitimate companies and recruitment portals <strong>NEVER charge money</strong> for interviews, job offers, security deposits, registration fees, or training bonds.<br>
  • If someone calls claiming to be from "Naukri HR" or a company HR asking for payment via UPI/QR code, <strong>it is 100% a fraud scam</strong>.<br>
  • Never share OTPs, bank details, or original certificates with unsolicited callers.
</div>

</body>
</html>"""
    convert_html_to_pdf(html, "naukri-checklist.pdf")

def build_pdf_bullet_guide():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Fresher Project Bullet-Point Formula</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 12mm 14mm;
  }
  body {
    font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.28;
    font-size: 8.8pt;
    margin: 0;
  }
  .header {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 5px;
    margin-bottom: 8px;
  }
  h1 {
    font-size: 15pt;
    color: #0f172a;
    margin: 0 0 2px 0;
  }
  .sub {
    font-size: 8.5pt;
    color: #475569;
  }
  .badge {
    display: inline-block;
    background: #e2e8f0;
    color: #0f172a;
    padding: 1px 6px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: bold;
  }
  .formula-banner {
    background: #0f172a;
    color: #ffffff;
    padding: 8px 12px;
    border-radius: 4px;
    margin-bottom: 8px;
    text-align: center;
    font-size: 10pt;
    font-weight: bold;
    letter-spacing: 0.5px;
  }
  .formula-banner span {
    color: #60a5fa;
  }
  h2 {
    font-size: 10pt;
    color: #0f172a;
    margin: 7px 0 3px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 2px;
  }
  .verb-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 6px;
    margin-bottom: 8px;
    font-size: 8pt;
  }
  .verb-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 4px 6px;
    border-radius: 3px;
  }
  .verb-head {
    font-weight: bold;
    color: #1e40af;
    margin-bottom: 2px;
  }
  .card {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
    padding: 6px 8px;
    margin-bottom: 6px;
  }
  .card-title {
    font-weight: bold;
    color: #0f172a;
    font-size: 8.8pt;
    margin-bottom: 2px;
  }
  .weak {
    color: #b91c1c;
    background: #fef2f2;
    padding: 3px 6px;
    border-radius: 3px;
    margin-bottom: 3px;
    font-size: 8.2pt;
  }
  .strong {
    color: #15803d;
    background: #f0fdf4;
    padding: 3px 6px;
    border-radius: 3px;
    font-size: 8.2pt;
  }
  .metric-tip {
    font-size: 8pt;
    color: #475569;
    margin-top: 2px;
    font-style: italic;
  }
  .fictional-label {
    color: #64748b;
    font-size: 7.5pt;
    font-weight: bold;
    text-transform: uppercase;
  }
</style>
</head>
<body>

<div class="header">
  <div style="float: right;"><span class="badge">FREE MVP v0.1</span> <span class="badge">WRITING FORMULA</span></div>
  <h1>FRESHER PROJECT BULLET-POINT FORMULA</h1>
  <div class="sub">How to Transform Passive Academic Descriptions into Strong Engineering Narratives (With Fictional Examples)</div>
</div>

<div class="formula-banner">
  [Strong Action Verb]  +  <span>[Technical Context / Architecture]</span>  +  [Outcome / Metric / Scope]
</div>

<h2>Action Verb Catalog (Select Based on Contribution)</h2>
<div class="verb-grid">
  <div class="verb-card">
    <div class="verb-head">Engineering / Building</div>
    Engineered, Architected, Developed, Constructed, Implemented, Integrated
  </div>
  <div class="verb-card">
    <div class="verb-head">Optimization / Speed</div>
    Optimized, Accelerated, Refactored, Indexed, Streamlined, Compressed
  </div>
  <div class="verb-card">
    <div class="verb-head">Testing & Reliability</div>
    Automated, Validated, Containerized, Debugged, Monitored, Deployed
  </div>
  <div class="verb-card">
    <div class="verb-head">Data & Analysis</div>
    Modeled, Extracted, Transformed, Analyzed, Visualized, Benchmarked
  </div>
</div>

<h2>6 Before vs. After Transformations</h2>
<div class="fictional-label">[ALL EXAMPLES BELOW ARE FICTIONAL DEMONSTRATIONS — DO NOT COPY DIRECTLY; ADAPT TO YOUR ACTUAL PROJECT DATA]</div>

<div class="card">
  <div class="card-title">1. Full-Stack Web Application (E-Commerce / Social)</div>
  <div class="weak"><strong>Weak (Passive):</strong> "Created a full-stack shopping website using React and Node.js with login and cart."</div>
  <div class="strong"><strong>Strong (Formula):</strong> "Architected full-stack web application using React.js and Express; implemented JWT authentication and role-based access control for 2 user roles, integrating Stripe checkout in sandbox mode."</div>
  <div class="metric-tip">How to quantify without users: Mention authentication security, number of endpoints, or response times.</div>
</div>

<div class="card">
  <div class="card-title">2. Backend REST API / Microservice</div>
  <div class="weak"><strong>Weak (Passive):</strong> "Made APIs in Python for task management and stored data in SQLite database."</div>
  <div class="strong"><strong>Strong (Formula):</strong> "Developed modular RESTful service with FastAPI and SQLite; authored 22 automated unit test cases in PyTest, achieving 88% statement coverage across core CRUD endpoints."</div>
  <div class="metric-tip">How to quantify without users: Test suite coverage %, number of unit tests, or request validation depth.</div>
</div>

<div class="card">
  <div class="card-title">3. Machine Learning / Data Analysis Project</div>
  <div class="weak"><strong>Weak (Passive):</strong> "Did customer churn prediction using Python and machine learning algorithms."</div>
  <div class="strong"><strong>Strong (Formula):</strong> "Engineered customer churn classifier using Python (scikit-learn, Pandas) across a dataset of 7,000+ records; benchmarked Random Forest vs. XGBoost, reaching 84% ROC-AUC."</div>
  <div class="metric-tip">How to quantify: Dataset row count, precision/recall, or feature engineering count.</div>
</div>

<div class="card">
  <div class="card-title">4. Systems / CLI / Automation Script</div>
  <div class="weak"><strong>Weak (Passive):</strong> "Wrote a Python script to parse server log files and find errors."</div>
  <div class="strong"><strong>Strong (Formula):</strong> "Constructed command-line log analysis utility in Python with regex parsing; processed 50,000+ server log entries in under 3.5 seconds, exporting structured JSON error summaries."</div>
  <div class="metric-tip">How to quantify: Records processed, execution throughput, or format conversion speed.</div>
</div>

<div class="card">
  <div class="card-title">5. Database Query Optimization</div>
  <div class="weak"><strong>Weak (Passive):</strong> "Wrote SQL queries to get data for the frontend."</div>
  <div class="strong"><strong>Strong (Formula):</strong> "Optimized relational database queries by implementing B-Tree indexes on foreign keys and compound fields, reducing local query latency from 140ms to 45ms."</div>
  <div class="metric-tip">How to quantify: Query execution time (via EXPLAIN / benchmark), index count.</div>
</div>

<div class="card">
  <div class="card-title">6. Academic Capstone / Hardware / IoT Project</div>
  <div class="weak"><strong>Weak (Passive):</strong> "Worked on college project for smart irrigation using Arduino and sensors."</div>
  <div class="strong"><strong>Strong (Formula):</strong> "Engineered automated irrigation telemetry system on ESP32/Arduino; collected soil moisture readings every 60s via MQTT protocol, triggering relay valves to conserve water."</div>
  <div class="metric-tip">How to quantify: Telemetry sampling interval, protocols used (MQTT/HTTP), hardware sensors integrated.</div>
</div>

</body>
</html>"""
    convert_html_to_pdf(html, "project-bullet-guide.pdf")

def build_xlsx_tracker():
    wb = openpyxl.Workbook()
    
    # Sheet 1: Dashboard
    ws_dash = wb.active
    ws_dash.title = "Application Dashboard"
    ws_dash.views.sheetView[0].showGridLines = True
    
    # Sheet 2: Application Tracker
    ws_track = wb.create_sheet(title="Applications Log")
    ws_track.views.sheetView[0].showGridLines = True
    
    # Styling Palette
    header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    kpi_title_font = Font(name="Calibri", size=10, bold=True, color="475569")
    kpi_num_font = Font(name="Calibri", size=20, bold=True, color="0F172A")
    kpi_border = Border(
        left=Side(style='thin', color="CBD5E1"),
        right=Side(style='thin', color="CBD5E1"),
        top=Side(style='thin', color="CBD5E1"),
        bottom=Side(style='thin', color="CBD5E1")
    )
    kpi_fill = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    
    # --- DASHBOARD SETUP ---
    ws_dash["A1"] = "FRESHER JOB APPLICATION DASHBOARD"
    ws_dash["A1"].font = Font(name="Calibri", size=16, bold=True, color="0F172A")
    ws_dash["A2"] = "Summary metrics automatically calculated from the 'Applications Log' tab."
    ws_dash["A2"].font = Font(name="Calibri", size=10, italic=True, color="475569")
    
    # KPI Cards
    kpis = [
        ("B4", "C4", "B5", "C5", "Total Tracked", '=COUNTA(\'Applications Log\'!A4:A500)'),
        ("D4", "E4", "D5", "E5", "Submitted", '=COUNTIF(\'Applications Log\'!H4:H500, "Applied") + COUNTIF(\'Applications Log\'!H4:H500, "Assessment (OA)") + COUNTIF(\'Applications Log\'!H4:H500, "Interviewing") + COUNTIF(\'Applications Log\'!H4:H500, "Offer Received") + COUNTIF(\'Applications Log\'!H4:H500, "Rejected") + COUNTIF(\'Applications Log\'!H4:H500, "Ghosted / No Reply")'),
        ("F4", "G4", "F5", "G5", "Assessments (OA)", '=COUNTIF(\'Applications Log\'!H4:H500, "Assessment (OA)")'),
        ("B7", "C7", "B8", "C8", "Active Interviews", '=COUNTIF(\'Applications Log\'!H4:H500, "Interviewing")'),
        ("D7", "E7", "D8", "E8", "Offers Received", '=COUNTIF(\'Applications Log\'!H4:H500, "Offer Received")'),
        ("F7", "G7", "F8", "G8", "Rejections Logged", '=COUNTIF(\'Applications Log\'!H4:H500, "Rejected")')
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
        
        # Border box
        for col in [top_l[0], top_r[0]]:
            for row in [top_l[1:], bot_l[1:]]:
                ws_dash[f"{col}{row}"].border = kpi_border

    # Instructions box on dashboard
    ws_dash["B11"] = "HOW TO USE THIS TRACKER:"
    ws_dash["B11"].font = Font(name="Calibri", size=11, bold=True, color="0F172A")
    instructions = [
        "1. Open the 'Applications Log' sheet to record every internship or job application.",
        "2. Use the dropdown menus in 'Source', 'Status', and 'Interview Stage' to keep data consistent.",
        "3. Track the exact resume version you submitted (e.g. Resume_Java_v1.pdf vs Resume_React_v2.pdf).",
        "4. Set a Follow-up Date 7–10 days after applying to send a polite follow-up or connection request.",
        "5. Avoid applying blindly to 50 jobs/day. Aim for 3–5 tailored, high-intent applications per day."
    ]
    for i, inst in enumerate(instructions):
        ws_dash[f"B{12+i}"] = inst
        ws_dash[f"B{12+i}"].font = Font(name="Calibri", size=9.5, color="334155")
        
    ws_dash.column_dimensions["A"].width = 4
    ws_dash.column_dimensions["B"].width = 16
    ws_dash.column_dimensions["C"].width = 16
    ws_dash.column_dimensions["D"].width = 16
    ws_dash.column_dimensions["E"].width = 16
    ws_dash.column_dimensions["F"].width = 16
    ws_dash.column_dimensions["G"].width = 16

    # --- APPLICATIONS LOG SHEET ---
    headers = [
        "Company Name",
        "Role Applied For",
        "Job URL / Link",
        "Date Found",
        "Date Applied",
        "Resume Version",
        "Source",
        "Status",
        "Interview Stage",
        "Follow-up Date",
        "Contact / Recruiter Name",
        "Notes & Next Steps"
    ]
    
    ws_track.row_dimensions[3].height = 24
    for col_idx, h in enumerate(headers, 1):
        cell = ws_track.cell(row=3, column=col_idx, value=h)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = kpi_border

    # Sample rows (Clearly fictitious examples)
    sample_rows = [
        ("Infosys / TCS (Off-Campus)", "Systems Engineer / Trainee", "https://careers.example.com/job/101", "2026-03-01", "2026-03-02", "Resume_Java_v1.pdf", "Company Careers Page", "Applied", "N/A", "2026-03-12", "Recruiter Team", "Applied via official portal; OA link expected within 10 days."),
        ("Swiggy / Zomato (Internship)", "Frontend Engineering Intern", "https://linkedin.com/jobs/view/102", "2026-03-03", "2026-03-03", "Resume_React_v2.pdf", "LinkedIn", "Assessment (OA)", "Online Assessment", "2026-03-08", "Priya (Campus Talent)", "Completed 90-min HackerRank test; 2 DSA problems solved."),
        ("FinTech Startup X", "Junior Backend Developer", "https://naukri.com/job/103", "2026-03-04", "2026-03-04", "Resume_Python_v1.pdf", "Naukri", "Interviewing", "Tech Round 1", "2026-03-10", "Anil (Engineering Lead)", "Technical interview scheduled for Tuesday 4 PM; review FastAPI & SQL joins.")
    ]
    
    for row_idx, r_data in enumerate(sample_rows, 4):
        ws_track.row_dimensions[row_idx].height = 20
        for col_idx, val in enumerate(r_data, 1):
            cell = ws_track.cell(row=row_idx, column=col_idx, value=val)
            cell.font = Font(name="Calibri", size=9.5, color="1E293B")
            cell.border = kpi_border
            if col_idx in [4, 5, 10]:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx in [7, 8, 9]:
                cell.alignment = Alignment(horizontal="center", vertical="center")

    # Data Validations (Dropdowns)
    # Source validation
    dv_source = DataValidation(type="list", formula1='"Naukri,LinkedIn,Company Careers Page,Referral,Campus,Internshala,Other"', allow_blank=True)
    ws_track.add_data_validation(dv_source)
    dv_source.add("G4:G500")
    
    # Status validation
    dv_status = DataValidation(type="list", formula1='"Saved / To Apply,Applied,Assessment (OA),Interviewing,Offer Received,Rejected,Ghosted / No Reply"', allow_blank=True)
    ws_track.add_data_validation(dv_status)
    dv_status.add("H4:H500")
    
    # Interview Stage validation
    dv_stage = DataValidation(type="list", formula1='"N/A,Recruiter Screen,Online Assessment,Tech Round 1,Tech Round 2,Managerial / HR,Offer Discussion"', allow_blank=True)
    ws_track.add_data_validation(dv_stage)
    dv_stage.add("I4:I500")

    # Set Column Widths
    col_widths = {
        "A": 24, # Company
        "B": 24, # Role
        "C": 26, # URL
        "D": 13, # Date Found
        "E": 13, # Date Applied
        "F": 20, # Resume Version
        "G": 20, # Source
        "H": 20, # Status
        "I": 20, # Stage
        "J": 14, # Follow-up
        "K": 22, # Contact
        "L": 35  # Notes
    }
    for col_letter, width in col_widths.items():
        ws_track.column_dimensions[col_letter].width = width

    out_xlsx = os.path.join(BASE_DIR, "job-application-tracker.xlsx")
    wb.save(out_xlsx)
    print(f"[OK] Generated {out_xlsx} ({os.path.getsize(out_xlsx)} bytes)")

if __name__ == "__main__":
    print("Building Fresher Job Application Kit (Free MVP v0.1) assets...")
    build_docx_resume()
    build_pdf_resume_reference()
    build_pdf_removal_checklist()
    build_pdf_self_audit()
    build_pdf_jd_tailoring()
    build_pdf_naukri_checklist()
    build_pdf_bullet_guide()
    build_xlsx_tracker()
    print("Asset generation complete!")
