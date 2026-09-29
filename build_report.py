from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.style import WD_STYLE_TYPE
from pathlib import Path

OUT = Path('/Users/mcaleg2006/Documents/Codex/2026-09-29/no-2-2-java-static-this/outputs')
OUT.mkdir(exist_ok=True)
path = OUT / 'zvit_praktychna_robota_2_bondarenko.docx'

doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.7); sec.bottom_margin = Inches(0.7)
sec.left_margin = Inches(0.85); sec.right_margin = Inches(0.7)

styles = doc.styles
styles['Normal'].font.name = 'Arial'; styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial'); styles['Normal'].font.size = Pt(11)
for s in ['Title','Heading 1','Heading 2']:
    styles[s].font.name='Arial'; styles[s]._element.rPr.rFonts.set(qn('w:eastAsia'),'Arial'); styles[s].font.color.rgb=RGBColor(0,0,0)
styles['Title'].font.size=Pt(18); styles['Heading 1'].font.size=Pt(14); styles['Heading 2'].font.size=Pt(12)
code = styles.add_style('CodeBlock', WD_STYLE_TYPE.PARAGRAPH); code.font.name='Courier New'; code._element.rPr.rFonts.set(qn('w:eastAsia'),'Courier New'); code.font.size=Pt(9)
code.paragraph_format.left_indent=Inches(0.25); code.paragraph_format.space_after=Pt(6)

def shade(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def borders(table):
    tblPr=table._tbl.tblPr; b=OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        e=OxmlElement(f'w:{edge}'); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:color'),'D9D9D9'); b.append(e)
    tblPr.append(b)
def p(text='', style=None, bold=False, align=None):
    par=doc.add_paragraph(style=style); r=par.add_run(text); r.bold=bold
    if align: par.alignment=align
    return par
def codeblock(text):
    par=doc.add_paragraph(style='CodeBlock'); par.paragraph_format.keep_together=True
    for i,line in enumerate(text.splitlines()):
        if i: par.add_run().add_break()
        par.add_run(line)
    return par

p('ДЕРЖАВНИЙ УНІВЕРСИТЕТ ІНФОРМАЦІЙНО-КОМУНІКАЦІЙНИХ ТЕХНОЛОГІЙ', bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
p('Кафедра технологій цифрового розвитку', align=WD_ALIGN_PARAGRAPH.CENTER)
doc.add_paragraph('\n')
p('ЗВІТ', style='Title', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Практична робота № 2', style='Heading 1', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Тема 2. ООП у Java: класи, інкапсуляція, конструктори, static', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Модифікатори доступу, конструктори, this, static та final на практиці', align=WD_ALIGN_PARAGRAPH.CENTER)
doc.add_paragraph('\n')
p('Дисципліна: Конструювання програмного забезпечення Java', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Група: ТЦР-31', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Виконав: Бондаренко Олег Вікторович', align=WD_ALIGN_PARAGRAPH.CENTER)
p('Варіант: 0 — клас-сутність «Книга»', align=WD_ALIGN_PARAGRAPH.CENTER)
doc.add_page_break()

p('1 Мета роботи', style='Heading 1')
p('Дослідити на прикладі класу Book поведінку модифікаторів доступу, конструкторів, ключових слів this, static і final у Java; зафіксувати результати компіляції та виконання програми.')
p('2 Структура проєкту', style='Heading 1')
codeblock('src/model/Book.java\nsrc/model/ModelTest.java\nsrc/app/Main.java')
p('Клас-сутність розміщено в пакеті model, а клас запуску — у пакеті app. Це дає змогу порівняти доступ до членів у межах одного пакета та з іншого пакета.')

p('3 Дослідження модифікаторів доступу', style='Heading 1')
codeblock('package model;\n\npublic class Book {\n    private String privateTitle = "private";\n    String packageTitle = "package";\n    protected String protectedTitle = "protected";\n    public String publicTitle = "public";\n}')
codeblock('package model;\n\npublic class ModelTest {\n    public static void check(Book b) {\n        System.out.println(b.packageTitle);\n        System.out.println(b.protectedTitle);\n        System.out.println(b.publicTitle);\n    }\n}')
codeblock('package app;\nimport model.Book;\n\npublic class Main {\n    public static void main(String[] args) {\n        Book b = new Book();\n        System.out.println(b.publicTitle);\n    }\n}')
t=doc.add_table(rows=1, cols=3); t.alignment=WD_TABLE_ALIGNMENT.CENTER; borders(t)
for c,txt in zip(t.rows[0].cells,['Модифікатор','Інший клас у model','Main у app']): c.text=txt; shade(c,'1F4E78'); c.paragraphs[0].runs[0].font.color.rgb=RGBColor(255,255,255); c.paragraphs[0].runs[0].bold=True
for row in [('private','ні','ні'),('за замовчуванням','так','ні'),('protected','так','ні'),('public','так','так')]:
    cells=t.add_row().cells
    for c,txt in zip(cells,row): c.text=txt; c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
p('Спостереження. private доступний лише всередині самого класу. Доступ за замовчуванням і protected працюють у межах пакета, тому доступні з ModelTest. public доступний звідусіль. Protected може бути доступний також у підкласі з іншого пакета, але звичайне звернення з Main у цьому досліді не дозволене.')

p('4 Конструктори та this', style='Heading 1')
codeblock('package model;\n\npublic class Book {\n    private String title;\n    private String author;\n    private int year;\n    public static int count = 0;\n    public final int id;\n\n    public Book() {\n        this("Без назви", "Невідомий автор", 0);\n    }\n\n    public Book(String title) {\n        this(title, "Невідомий автор", 0);\n    }\n\n    public Book(String title, String author, int year) {\n        this.title = title;\n        this.author = author;\n        this.year = year;\n        this.id = ++count;\n    }\n\n    public String info() {\n        return id + ": " + title + " — " + author + ", " + year;\n    }\n}')
codeblock('Book b1 = new Book();\nBook b2 = new Book("Кобзар");\nBook b3 = new Book("Java", "Herbert Schildt", 2022);\nSystem.out.println(b1.info());\nSystem.out.println(b2.info());\nSystem.out.println(b3.info());')
p('Очікуваний результат: b1 отримує типові значення, b2 — назву та типові значення для інших полів, b3 — усі значення з параметрів. Виклик this(...) передає ініціалізацію іншому конструктору та має бути першим оператором конструктора.')
p('Якщо прибрати this у рядках присвоєння, наприклад написати title = title, параметр присвоюється самому собі, а поле залишиться зі значенням за замовчуванням null. Тому this.title = title розрізняє поле та параметр.')

p('5 static і поле екземпляра', style='Heading 1')
codeblock('Book b1 = new Book("A");\nBook b2 = new Book("B");\nBook b3 = new Book("C");\nSystem.out.println(Book.count); // 3\nSystem.out.println(b1.info());\nSystem.out.println(b2.info());\nSystem.out.println(b3.info());')
p('Поле count оголошене static, тому існує в одному екземплярі для всього класу й збільшується спільно для всіх об’єктів. Поле title є полем екземпляра, тому кожна книга має власну назву. Статичний член викликано коректно через ім’я класу: Book.count.')

p('6 final', style='Heading 1')
codeblock('public final int id;\n\npublic Book(String title) {\n    this.id = ++count;\n}\n\nfinal int localId = 5;\nlocalId = 6;\nthis.id = 10;')
p('final-поле id можна присвоїти один раз у конструкторі кожного об’єкта. Після завершення ініціалізації повторне присвоєння заборонене. Локальна final-змінна також не може бути змінена після першого присвоєння.')

p('7 Контрольні питання', style='Heading 1')
for q,a in [
('Чому private-член недоступний навіть з іншого класу того самого пакета?','Тому що private обмежує доступ межами класу-власника, а не пакета.'),
('Чим відрізняються доступ за замовчуванням, protected і public?','Доступ за замовчуванням діє в пакеті; protected — у пакеті та в підкласах; public — без пакетних обмежень.'),
('Що робить this(...) у конструкторі?','Викликає інший конструктор цього самого класу. Це зменшує дублювання коду.'),
('Чим static-поле відрізняється від поля екземпляра?','static-поле спільне для класу, а поле екземпляра належить конкретному об’єкту.'),
('Що дає final і коли його можна задати?','final забороняє повторне присвоєння; поле можна задати під час оголошення або в кожному конструкторі.')]:
    p(q, bold=True); p(a)

p('8 Висновок', style='Heading 1')
p('У роботі досліджено чотири рівні доступу та підтверджено, що доступність залежить від місця звернення. Реалізовано конструктор без параметрів, конструктори з параметрами та делегування через this(...). На прикладі Book.count показано спільність static-поля, а на прикладі title — незалежність полів екземплярів. Також перевірено, що final-поля та final-змінні не можна перезаписати після ініціалізації.')
p('Посилання на репозиторій: ________________________________')

doc.save(path)
print(path)
