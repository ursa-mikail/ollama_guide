"""
#!ollama serve
!nohup ollama serve > ollama.log 2>&1 &
!ollama pull llama3
!ollama run llama3
"""

#!pip install pypdf
import subprocess
import time
from pypdf import PdfReader

def query_llama(prompt):
    print("Llama now processing.")
    start_time = time.time()
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("llama problem:", e.stderr)
        return None

def get_text(pdf_name):
    reader = PdfReader(pdf_name)
    page = reader.pages[0]
    return page.extract_text()

# Usage
fname = "example.pdf"       # Replace with actual PDF filename
text = get_text(fname)

query = f"For the text of '{text}'. Find the US postcodes, IP addresses, email addresses, bank details, telephone numbers, credit card details, MAC addresses, cities, and passwords."
res = query_llama(query)

print(res)

