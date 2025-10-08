import pdfplumber


def leggi_pdf(percorso_pdf):
    """Legge il testo da un PDF"""
    testo_completo = ""

    try:
        with pdfplumber.open(percorso_pdf) as pdf:
            for pagina in pdf.pages:
                testo_pagina = pagina.extract_text()
                if testo_pagina:
                    testo_completo += testo_pagina + "\n"

        return testo_completo.strip()

    except Exception as e:
        print(f"❌ Errore nella lettura del PDF: {e}")
        return ""