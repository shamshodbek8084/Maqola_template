from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Maqola
from .forms import MaqolaForm 
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


def home(request):
    return render(request, 'home.html')


def create_maqola(request):
    if request.method == 'POST':
        form = MaqolaForm(request.POST)
        if form.is_valid():
            maqola = form.save(commit=False)
            maqola.user = request.user  # shu foydalanuvchiga biriktiramiz
            maqola.save()
            return redirect('maqola:list')
    else:
        form = MaqolaForm()
    return render(request, 'maqola/create.html', {'form': form})



def list_maqola(request):
    maqolalar = Maqola.objects.filter(user=request.user).order_by('number')
    return render(request, 'maqola/list.html', {'maqolalar': maqolalar})


def update_maqola(request, pk):
    maqola = get_object_or_404(Maqola, pk=pk, user=request.user)
    form = MaqolaForm(request.POST or None, instance=maqola)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('maqola:list')
    return render(request, 'maqola/update.html', {'form': form})


def delete_maqola(request, pk):
    maqola = get_object_or_404(Maqola, pk=pk, user=request.user)
    if request.method == 'POST':
        maqola.delete()
        return redirect('maqola:list')
    return render(request, 'maqola/delete.html', {'maqola': maqola})


# === EXPORT to DOCX ===
def export_maqola_docx(request):
    maqolalar = Maqola.objects.all().order_by('-id')
    doc = Document()
    last = maqolalar.first()

    heading_text = (
        "Muhammad al-Xorazmiy nomidagi Toshkent axborot texnologiyalari universiteti Kiberxavfsizlik fakulteti\n"
        f"{last.fakultet_raqami} - \u201c{last.fakultet} (Axborot-kommunikatsiya texnologiyalari va servis)\u201d "
        f"{last.guruh_raqami}-guruh talabasi {last.talaba_fish}ning\n"
        "ILMIY ISHLARI RO\u2018YXATI"
    )
    heading = doc.add_paragraph(heading_text)
    heading.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    for run in heading.runs:
        run.bold = True
        run.font.size = Pt(12)

    table = doc.add_table(rows=1, cols=6)
    table.style = 'Table Grid'
    headers = ["\u2116", "Ilmiy ishning nomi", "Format", "Jurnal ma’lumotlari", "Bosma bet/muallif", "Mualliflar"]
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
