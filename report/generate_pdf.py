import os
import subprocess
import sys

def generate_pdf():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(script_dir, "report_template.html")
    pdf_file = os.path.join(script_dir, "Banking_System_Project_Report.pdf")

    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]

    browser_bin = None
    for path in edge_paths:
        if os.path.exists(path):
            browser_bin = path
            break

    if not browser_bin:
        print("Error: Could not locate Microsoft Edge or Google Chrome to compile PDF.")
        sys.exit(1)

    html_uri = "file:///" + html_file.replace("\\", "/")
    cmd = [
        browser_bin,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}",
        html_uri
    ]

    print(f"Compiling project report HTML to PDF using: {os.path.basename(browser_bin)}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
        print(f"[SUCCESS] PDF successfully generated at:\n  {pdf_file} ({os.path.getsize(pdf_file):,} bytes)")
    else:
        print(f"[ERROR] PDF generation failed.\nStderr: {result.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    generate_pdf()
