import docx2pdf
import pdf2pptx

doc_file_name: str = '2344201200134+张新洲.docx'
pdf_file_name: str = '2344201200134+张新洲.pdf'

# convert the doc file to a pdf file
docx2pdf.convert(doc_file_name)

# convert the pdf file to a ppt file
pdf2pptx.convert_pdf2pptx(pdf_file_name, output_file=None, resolution=150, start_page=0, page_count=14)
