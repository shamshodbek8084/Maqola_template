from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Maqola
from .forms import MaqolaForm  # ← Formani chaqiramiz
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

# Bosh sahifa
def home(request):
    return render(request, 'home.html')


# Maqolalar ro‘yxati
def list_maqola(request):
    maqolalar = Maqola.objects.all().order_by('number')
    return render(request, 'maqola_list.html', {'maqolalar': maqolalar})


# Maqola qo‘shish — FORM orqali
def create_maqola(request):
    if request.method == 'POST':
        form = MaqolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maqola_list')
    else:
        form = MaqolaForm()
    return render(request, 'maqola_form.html', {'form': form})


# Word faylga eksport
def export_maqola_docx(request):
    maqolalar = Maqola.objects.all().order_by('-id')
    doc = Document()
    last = maqolalar.first()

    heading_text = (
        "Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Kiberxavfsizlik fakulteti\n"
        f"{last.fakultet_raqami} - “{last.fakultet} (Axborot-kommunikatsiya texnologiyalari va servis)” "
        f"{last.guruh_raqami}-guruh talabasi {last.talaba_fish}ning\n"
        "ILMIY ISHLARI RO‘YXATI"
    )
    heading = doc.add_paragraph(heading_text)
    heading.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    for run in heading.runs:
        run.bold = True
        run.font.size = Pt(12)

    table = doc.add_table(rows=1, cols=6)
    table.style = 'Table Grid'
    headers = [
        "№",
        "Ilmiy ishning nomi",
        "Format",
        "Jurnal ma’lumotlari",
        "Bosma bet/muallif",
        "Mualliflar"
    ]
    hdr_cells = table.rows[0].cells
    for i, header in enumerate(headers):
        p = hdr_cells[i].paragraphs[0]
        run = p.add_run(header)
        run.bold = True
        run.font.size = Pt(10)

    for m in maqolalar:
        row_cells = table.add_row().cells
        row_cells[0].text = str(m.number)
        row_cells[1].text = m.title
        row_cells[2].text = m.format
        row_cells[3].text = m.journal_information
        row_cells[4].text = m.piece
        row_cells[5].text = m.authors

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=ilmiy_ishlar.docx'
    doc.save(response)
    return response
