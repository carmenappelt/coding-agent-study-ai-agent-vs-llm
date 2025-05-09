#Wikipedia Downloader Task
from reportlab.pdfgen import canvas
import wikipedia
import warnings
import os  # Füge os import hinzu

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
    # Erstelle den PDF-Pfad im task_1 Ordner
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, title + ".pdf")
    
    pdf = canvas.Canvas(pdf_path)
    pdf.setPageSize((2480 ,3508))
    pdf.setFont("Helvetica", 40)


    # Feature 1, Feature 2, Feature 3

    pdf.save() #Saves the pdf in the same folder as the main.py file

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

