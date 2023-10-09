from fpdf import FPDF

title = '20000 Leagues Under the Seas'

class PDF(FPDF):
    def header(self):
        self.image('modules\\fpdf\\logo.png', 10, 0, 33)
        self.set_font('Arial', 'B', 15)
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.cell(w, 15, title, 1, 1, 'C', 1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        self.set_font('Arial', '', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, name):
        with open(name, 'rb') as fh:
            txt = fh.read().decode('latin-1')
        self.set_font('Times', '', 12)
        self.multi_cell(0, 5, txt)
        self.ln()
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

    def print_linenumbers(self,):
        self.alias_nb_pages()
        self.add_page()
        self.set_font('Times', '', 12)
        for i in range(1, 34):
            self.cell(0, 7, 'Printing line number ' + str(i), 0, 1)
    
pdf = PDF()
pdf.set_title(title)
pdf.set_author('Jules Verne')
pdf.print_linenumbers()
pdf.print_chapter(1, 'A RUNAWAY REEF', 'modules\\fpdf\\chapter1.txt')
# pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
pdf.output('modules\\fpdf\\tuto3.pdf', 'F')