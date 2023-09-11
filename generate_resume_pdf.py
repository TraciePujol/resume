from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Data for the skills section
skills = [
    "JavaScript",
    "HTML",
    "CSS",
    "Python (Familiarity)",
    "Flask Framework",
    "MySQL (Familiarity)",
    "MS SQL",
    "Integrated Development Environments (Visual Studio Code, Atom)",
    "Command Prompt Tools (Anaconda, Microsoft Developer CMD Prompt)",
    "Microsoft Office (Word, Excel)",
    "Web Development",
    "Database Management",
    "Cloud Technologies (AWS, Microsoft Azure)",
    "Communication Skills",
    "Agile Scrum Methodologies",
    "Discord Server Management",
    # Add more skills as needed
]

# Function to generate the PDF
def generate_resume_pdf():
    c = canvas.Canvas("resume.pdf", pagesize=letter)
    c.setFont("Helvetica", 12)

    # Title
    c.drawString(72, 750, "Tracie Pujol's Resume")

    # Skills Section Title
    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, 700, "Skills Summary")

    # Skills List
    c.setFont("Helvetica", 12)
    y = 680  # Starting Y-coordinate for skills
    for skill in skills:
        c.drawString(90, y, "• " + skill)
        y -= 20  # Adjust Y-coordinate for the next skill

    c.save()

if __name__ == "__main__":
    generate_resume_pdf()
