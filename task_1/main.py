#Wikipedia Downloader Task
from reportlab.pdfgen import canvas
import wikipedia
import warnings
import os
warnings.catch_warnings()
warnings.simplefilter("ignore")

def newX(x):
    newX = x     # Feature 2
    return newX

def newY(y):
    height = 3508
    newY = y     # Feature 2
    return newY

def createPDF(title, link, summary):
    import os
    
    # Check if running in GitHub Codespaces
    is_codespace = os.environ.get('CODESPACES', False)
    
    if is_codespace:
        # In Codespaces, save to a web-accessible directory
        pdf_path = os.path.join(os.getcwd(), 'web', title + ".pdf")
        # Create web directory if it doesn't exist
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        pdf_path = os.path.join(os.path.dirname(__file__), title + ".pdf")
    else:
        # Save in the same directory as main.py
        pdf_path = os.path.join(os.path.dirname(__file__), title + ".pdf")

    pdf = canvas.Canvas(pdf_path)
    pdf.setPageSize((2480, 3508))
    pdf.setFont("Helvetica", 40)

    # Feature 1, Feature 2, Feature 3

    pdf.save()

    if is_codespace:
        # Create a simple HTML file to provide download link
        html_path = os.path.join(os.path.dirname(pdf_path), 'download.html')
        with open(html_path, 'w') as f:
            f.write(f'''<!DOCTYPE html>
<html>
<head><title>Download {title} PDF</title></head>
<body>
    <h1>Download PDF</h1>
    <p><a href="{title}.pdf" download>{title}.pdf</a></p>
</body>
</html>''')
        print(f"\nIf running in Codespaces, you can find your PDF at: {pdf_path}")
        print(f"Access the download page at: {html_path}")

def outputinConsole(title,link,summary):
    print("\nTitle: " + title)
    print("Link: " + link)
    print("Summary: " + summary[:300] + "...")

if __name__ == '__main__':

    search_term = input("\nEnter search term: ")

    try:
        page = wikipedia.page(search_term)
        print("Topic was found.")
        outputinConsole(page.title, page.url, page.summary)
        createPDF(page.title, page.url, page.summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print("The search term is ambigious. Please select a specific topic.")
        options = '\n'.join(e.options)
        print(options)
    except wikipedia.exceptions.PageError as e:
        print("The search term did not lead to any matches.")

