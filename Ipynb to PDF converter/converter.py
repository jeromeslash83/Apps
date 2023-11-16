from nbconvert.exporters import PDFExporter
from nbformat import read, NO_CONVERT

class NotebookConverter:
    def __init__(self):
        pass

    def get_pdf_file_path(self, notebook_path):
        return notebook_path.rsplit('.ipynb', 1)[0] + '.pdf'

    def convert_to_pdf(self, notebook_path):
        try:
            pdf_exporter = PDFExporter()

            with open(notebook_path, 'r', encoding='utf-8') as file:
                nb = read(file, as_version=NO_CONVERT)

            (body, _) = pdf_exporter.from_notebook_node(nb)

            pdf_file_path = self.get_pdf_file_path(notebook_path)

            with open(pdf_file_path, 'wb') as pdf_file:
                pdf_file.write(body)

            return pdf_file_path, None
        except Exception as e:
            print(f'Error converting {notebook_path} to PDF: {e}')
            return None, str(e)
