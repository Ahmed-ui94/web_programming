from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        
        #setting font
        self.set_font('Times', 'B', size=14)
        #move cursor to the right
        self.cell(80)
        #print the title
        self.cell(30, 10, "CS50 Shirtificate", align='C')

def main():
    x = input("You name: ")
    pdf = PDF(orientation="P", unit='mm', format='A4')
    pdf.add_page()
    pdf.image('shirtificate.png', x=40, y=80, w=60, h=70)
    pdf.set_font('Times', 'B', size= 18)
    pdf.cell(8, 150, txt=x + " " + "took CS50", align="C")
    pdf.auto_page_break
    pdf.close()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

        