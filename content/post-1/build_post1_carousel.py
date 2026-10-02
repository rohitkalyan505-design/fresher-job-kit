"""
Generates LinkedIn PDF Carousel: 5 Things Indian Freshers Should Remove from Their Resumes
High-contrast, 1080x1350 4:5 aspect ratio slides for LinkedIn document upload.
"""

import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POST1_DIR = os.path.join(BASE_DIR, "..", "..", "content", "post-1")
os.makedirs(POST1_DIR, exist_ok=True)
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
  @page {
    size: 1080px 1350px;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
  }
  body {
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #0f172a;
    color: #f8fafc;
  }
  .slide {
    width: 1080px;
    height: 1350px;
    padding: 90px 80px;
    page-break-after: always;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    background: #0f172a;
  }
  .slide-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #334155;
    padding-bottom: 24px;
  }
  .brand-badge {
    font-size: 24px;
    font-weight: 700;
    color: #60a5fa;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .slide-number {
    font-size: 24px;
    font-weight: 600;
    color: #94a3b8;
  }
  .content-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px 0;
  }
  .slide-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 2px solid #334155;
    padding-top: 24px;
    font-size: 22px;
    color: #64748b;
  }
  .swipe-prompt {
    color: #60a5fa;
    font-weight: 600;
  }
  
  /* Slide 1 - Cover */
  .cover-tag {
    display: inline-block;
    background: #1e293b;
    border: 1px solid #3b82f6;
    color: #60a5fa;
    padding: 10px 24px;
    border-radius: 30px;
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 30px;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  .cover-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1.15;
    color: #ffffff;
    margin: 0 0 30px 0;
  }
  .cover-title span {
    color: #f87171;
  }
  .cover-desc {
    font-size: 32px;
    line-height: 1.4;
    color: #cbd5e1;
    margin-bottom: 40px;
  }
  .cover-meta {
    background: #1e293b;
    border-left: 6px solid #3b82f6;
    padding: 24px 30px;
    border-radius: 8px;
    font-size: 26px;
    color: #94a3b8;
  }

  /* Slide Content Components */
  .item-badge {
    display: inline-block;
    background: #7f1d1d;
    color: #fecaca;
    padding: 8px 20px;
    border-radius: 8px;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
    text-transform: uppercase;
  }
  .item-title {
    font-size: 52px;
    font-weight: 800;
    color: #ffffff;
    margin: 0 0 30px 0;
    line-height: 1.2;
  }
  .card-box {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 32px;
    margin-bottom: 24px;
  }
  .card-label {
    font-size: 22px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
  }
  .card-label.why { color: #f87171; }
  .card-label.instead { color: #4ade80; }
  .card-label.exception { color: #38bdf8; }
  .card-text {
    font-size: 28px;
    line-height: 1.4;
    color: #e2e8f0;
    margin: 0;
  }
</style>
</head>
<body>

<!-- SLIDE 1: COVER -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">Off-Campus Resume Guide</span>
    <span class="slide-number">01 / 08</span>
  </div>
  <div class="content-area">
    <div class="cover-tag">Off-Campus Tech 2026</div>
    <h1 class="cover-title">5 Things Indian Freshers Should <span>Delete</span> from Their Resumes</h1>
    <div class="cover-desc">Why your college placement biodata format is getting ignored by off-campus tech recruiters (and what to put instead).</div>
    <div class="cover-meta">Based on recruiter workflows, ATS text parsing tests, and 2026 hiring standards.</div>
  </div>
  <div class="slide-footer">
    <span>Fresher Job Application Kit</span>
    <span class="swipe-prompt">Swipe Next →</span>
  </div>
</div>

<!-- SLIDE 2: FATHER'S NAME -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">Mistake #1</span>
    <span class="slide-number">02 / 08</span>
  </div>
  <div class="content-area">
    <div class="item-badge">Remove This</div>
    <h2 class="item-title">1. Father’s Name & Family Biodata</h2>
    
    <div class="card-box">
      <div class="card-label why">Why It Hurts You:</div>
      <p class="card-text">Recruiters evaluate your technical skills, not family genealogy. In off-campus tech hiring, parent details are viewed as 1990s biodata clutter that wastes 2–3 lines of vertical space.</p>
    </div>

    <div class="card-box">
      <div class="card-label instead">What to Put Instead:</div>
      <p class="card-text">Your clean <strong>GitHub</strong>, <strong>LinkedIn</strong>, and <strong>Portfolio</strong> links. Reclaim that space for real code evidence.</p>
    </div>

    <div class="card-box" style="margin-bottom: 0;">
      <div class="card-label exception">Legitimate Exception:</div>
      <p class="card-text" style="font-size: 24px; color: #94a3b8;">Keep only if specifically mandated in formal Indian Government / PSU / UPSC exam applications.</p>
    </div>
  </div>
  <div class="slide-footer">
    <span>Family details ≠ Engineering ability</span>
    <span class="swipe-prompt">Swipe Next →</span>
  </div>
</div>

<!-- SLIDE 3: DECLARATION -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">Mistake #2</span>
    <span class="slide-number">03 / 08</span>
  </div>
  <div class="content-area">
    <div class="item-badge">Remove This</div>
    <h2 class="item-title">2. The Formal "Declaration" Block</h2>
    
    <div class="card-box">
      <div class="card-label why">Why It Hurts You:</div>
      <p class="card-text"><em>"I hereby declare that all the information above is true to the best of my knowledge..."</em> + Date + Place + Signature block wastes 4–5 lines of prime bottom space.</p>
    </div>

    <div class="card-box">
      <div class="card-label instead">What to Put Instead:</div>
      <p class="card-text">Submitting an application legally implies truthfulness. Replace this wasted space with an extra technical certification or another project bullet.</p>
    </div>

    <div class="card-box" style="margin-bottom: 0;">
      <div class="card-label exception">Legitimate Exception:</div>
      <p class="card-text" style="font-size: 24px; color: #94a3b8;">Physical paper document submissions for traditional banking/defense exams where signed hard copies are required.</p>
    </div>
  </div>
  <div class="slide-footer">
    <span>Zero recruiters read declarations</span>
    <span class="swipe-prompt">Swipe Next →</span>
  </div>
</div>

<!-- SLIDE 4: PHOTOGRAPH -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">Mistake #3</span>
    <span class="slide-number">04 / 08</span>
  </div>
  <div class="content-area">
    <div class="item-badge">Remove This</div>
    <h2 class="item-title">3. Headshot / Candidate Photo</h2>
    
    <div class="card-box">
      <div class="card-label why">Why It Hurts You:</div>
      <p class="card-text">Off-campus software and corporate hiring does not evaluate physical appearance. Photos can confuse optical text parsers and risk introducing unconscious hiring bias.</p>
    </div>

    <div class="card-box">
      <div class="card-label instead">What to Put Instead:</div>
      <p class="card-text">A clean, centered text header with your <strong>Full Name</strong>, <strong>City & State</strong>, <strong>Email</strong>, and <strong>Active Mobile (+91)</strong>.</p>
    </div>

    <div class="card-box" style="margin-bottom: 0;">
      <div class="card-label exception">Legitimate Exception:</div>
      <p class="card-text" style="font-size: 24px; color: #94a3b8;">Hospitality, aviation (cabin crew), media/acting, or European CV standards (e.g. Germany/France) where photos are conventional.</p>
    </div>
  </div>
  <div class="slide-footer">
    <span>Code quality > Headshot</span>
    <span class="swipe-prompt">Swipe Next →</span>
  </div>
</div>

<!-- SLIDE 5: SKILL BARS -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">Mistake #4</span>
    <span class="slide-number">05 / 08</span>
  </div>
  <div class="content-area">
    <div class="item-badge">Remove This</div>
    <h2 class="item-title">4. Subjective Skill Rating Bars</h2>
    
    <div class="card-box">
      <div class="card-label why">Why It Hurts You:</div>
      <p class="card-text">Canva progress bars like <em>"Python: 85%"</em> or <em>"Problem Solving: ★★★★☆"</em> mean nothing to technical interviewers. <em>"85% of what? Did you build the Python compiler?"</em></p>
    </div>

    <div class="card-box">
      <div class="card-label instead">What to Put Instead:</div>
      <p class="card-text">Categorized skills: <strong>Languages</strong>, <strong>Frameworks</strong>, <strong>Tools</strong>, and <strong>Core CS Fundamentals</strong>. Let your projects prove your skill level.</p>
    </div>

    <div class="card-box" style="margin-bottom: 0;">
      <div class="card-label exception">Senior Engineer Rule:</div>
      <p class="card-text" style="font-size: 24px; color: #94a3b8;">Never rate yourself subjectively on a resume. Only list technologies you have written code in and can defend in a live technical screen.</p>
    </div>
  </div>
  <div class="slide-footer">
    <span>Prove skills with projects, not stars</span>
    <span class="swipe-prompt">Swipe Next →</span>
  </div>
</div>

<!-- SLIDE 6: FULL ADDRESS -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">Mistake #5</span>
    <span class="slide-number">06 / 08</span>
  </div>
  <div class="content-area">
    <div class="item-badge">Remove This</div>
    <h2 class="item-title">5. Full Street / House Door Address</h2>
    
    <div class="card-box">
      <div class="card-label why">Why It Hurts You:</div>
      <p class="card-text">Putting your house number, street name, and local landmark creates unnecessary privacy risks when uploading resumes across dozens of job portals.</p>
    </div>

    <div class="card-box">
      <div class="card-label instead">What to Put Instead:</div>
      <p class="card-text">Simply state <code>City, State</code> (e.g. <em>Bengaluru, Karnataka</em> or <em>Hyderabad, Telangana</em>). Recruiters only need to know your general location and relocation willingness.</p>
    </div>

    <div class="card-box" style="margin-bottom: 0;">
      <div class="card-label exception">When Address is Needed:</div>
      <p class="card-text" style="font-size: 24px; color: #94a3b8;">Keep full physical address for background checks and physical onboarding <em>after</em> receiving an official offer letter.</p>
    </div>
  </div>
  <div class="slide-footer">
    <span>Protect your privacy on job boards</span>
    <span class="swipe-prompt">Swipe Next →</span>
  </div>
</div>

<!-- SLIDE 7: REPLACEMENT SUMMARY -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">The Strategy</span>
    <span class="slide-number">07 / 08</span>
  </div>
  <div class="content-area">
    <div class="cover-tag" style="background: #14532d; border-color: #22c55e; color: #86efac;">The 1-Page Payoff</div>
    <h2 class="item-title">What Happens When You Cut the Fluff?</h2>
    
    <div class="card-box">
      <p class="card-text">You immediately reclaim <strong>8 to 12 lines of vertical space</strong>. Fill that space with what actually gets you shortlisted:</p>
      <ul style="font-size: 26px; line-height: 1.5; color: #cbd5e1; margin-top: 16px;">
        <li>2–3 substantive projects with live demo & GitHub links.</li>
        <li>Action verbs: <em>Engineered, Architected, Optimized</em>.</li>
        <li>Scope metrics: <em>Test coverage %, latency reduction, dataset size</em>.</li>
        <li>A clean single-column layout designed to reduce common parsing and text-order risks.</li>
      </ul>
    </div>
  </div>
  <div class="slide-footer">
    <span>Relevance > Biodata</span>
    <span class="swipe-prompt">Final Slide →</span>
  </div>
</div>

<!-- SLIDE 8: THE FREE KIT RESOURCE -->
<div class="slide">
  <div class="slide-header">
    <span class="brand-badge">Free Toolkit</span>
    <span class="slide-number">08 / 08</span>
  </div>
  <div class="content-area" style="text-align: center; align-items: center;">
    <div class="cover-tag" style="background: #1e3a8a; border-color: #3b82f6; color: #93c5fd;">100% Free • ₹0 Upfront</div>
    <h2 class="item-title" style="font-size: 50px;">Need a Clean, ATS-Conscious Resume Template?</h2>
    
    <div class="card-box" style="text-align: left; width: 100%;">
      <p class="card-text" style="font-size: 26px; line-height: 1.5;">
        We compiled the <strong>Fresher Job Application Kit (Free MVP v0.1)</strong>:<br>
        ✓ Single-Column .docx Template (Zero layout tables)<br>
        ✓ Visual 1-Page Reference PDF<br>
        ✓ 20-Point Resume Self-Audit Checklist<br>
        ✓ 10-Minute Job Description Tailoring Worksheet<br>
        ✓ Naukri Profile & Scam Defense Checklist<br>
        ✓ Project Bullet Formula & Excel Application Tracker
      </p>
    </div>

    <div style="background: #1e293b; border: 2px dashed #60a5fa; padding: 20px 30px; border-radius: 12px; font-size: 26px; color: #ffffff; margin-top: 10px;">
      <strong>Zero Paywalls. No Credit Card. Free Download.</strong><br>
      <span style="color: #94a3b8; font-size: 22px;">Check the link in the first comment or profile bio.</span>
    </div>
  </div>
  <div class="slide-footer">
    <span>Save & Share with Classmates</span>
    <span style="color: #60a5fa; font-weight: bold;">Bookmark 🔖</span>
  </div>
</div>

</body>
</html>
"""

temp_html = os.path.join(POST1_DIR, "carousel.html")
out_pdf = os.path.join(POST1_DIR, "linkedin-carousel-5-things-to-remove.pdf")

with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_content)

cmd = [
    EDGE_PATH,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    f"--print-to-pdf={out_pdf}",
    temp_html
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(temp_html):
    os.remove(temp_html)

if os.path.exists(out_pdf):
    print(f"[OK] Generated {out_pdf} ({os.path.getsize(out_pdf)} bytes)")
else:
    print(f"[ERROR] Failed to generate {out_pdf}: {res.stderr}")
