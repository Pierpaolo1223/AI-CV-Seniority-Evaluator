import os
from dotenv import load_dotenv

# Il prompt per analizzare i CV
PROMPT_ANALISI = """
Analizza il CV e assegna un livello di seniority tecnica complessiva.

Per ogni criterio, valuta anche il livello di evidenza (alta, media, bassa).
Riduci il punteggio se l’evidenza è media o bassa.

CRITERI (totale 100 punti):
1. Impatto sistemico (35)
2. Responsabilità architetturali (25)
3. Leadership tecnica (20)
4. Complessità gestita (20)

Esempi di riferimento:
- Junior: esegue task definiti.
- Mid: contribuisce ma non decide.
- Senior: progetta e guida.
- Staff: influenza più team o sistemi.

Mostra una tabella con i punteggi parziali, poi la somma.

CV DA ANALIZZARE:
{testo_cv}

OUTPUT:
- Tabella dei punteggi
- LIVELLO: [junior/mid/senior/staff]
- PUNTEGGIO: [numero]/100
- MOTIVAZIONE: [breve spiegazione con esempi dal CV]
"""
