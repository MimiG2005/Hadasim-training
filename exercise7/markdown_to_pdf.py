import markdown
from weasyprint import HTML

def markdown_to_pdf(md_file):
    with open(md_file,"r",encoding="utf-8") as f:
        md_text=f.read()
        print(md_text)
    html_text=markdown.markdown(md_text)
    print(html_text)
    HTML(string=html_text).write_pdf("output_file.pdf")
    
markdown_to_pdf("example.md")
