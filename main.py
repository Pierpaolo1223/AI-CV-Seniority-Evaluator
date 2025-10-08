import os
from ai_analyzer import analizza_cv_con_gemini, detect_cv_with_ai
from pdf_reader import leggi_pdf


def main():
    print("🎯 ANALIZZATORE DI CV")
    print("=" * 40)

    # Chiedi il percorso del PDF
    percorso_pdf = input("Inserisci il percorso del PDF: ").strip()

    # Verifica che il file esista
    if not os.path.exists(percorso_pdf):
        print("❌ File non trovato!")
        return

    # Leggi il PDF
    print("📖 Leggo il PDF...")
    testo_cv = leggi_pdf(percorso_pdf)

    if not testo_cv:
        print("❌ Impossibile leggere il PDF")
        return

    print(f"✅ Testo estratto ({len(testo_cv)} caratteri)")

    print("Verifico se è CV...")
    verificaCV = detect_cv_with_ai(testo_cv)
    # Mostra il risultato
    print("\n" + "=" * 40)
    print("📊 RISULTATO DELL'ANALISI:")
    print("=" * 40)
    print(verificaCV)
    if verificaCV['is_cv']:
        print("Questo è un CV")
        print("🤖 Analizzo con AI...")
        risultato = analizza_cv_con_gemini(testo_cv)
        # Mostra il risultato
        print("\n" + "=" * 40)
        print("📊 RISULTATO DELL'ANALISI:")
        print("=" * 40)
        print(risultato)

    else:
        print("questo non è un CV")

if __name__ == "__main__":
    main()