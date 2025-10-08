import os
from dotenv import load_dotenv

# Il prompt per analizzare i CV
'''PROMPT_ANALISI = """
Analizza il CV e assegna un livello di seniority:

CRITERI:
1. IMPATTO SISTEMICO (35%): ha creato/migliorato processi?
2. RESPONSABILITÀ ARCHITETTONICHE (25%): ha progettato sistemi?
3. LEADERSHIP TECNICA (20%): ha guidato/coordinato team?
4. COMPLESSITÀ GESTITA (20%): ha lavorato su sistemi complessi?

CALCOLA:
- Junior: 0-40 punti
- Mid: 41-65 punti  
- Senior: 66-85 punti
- Staff: 86-100 punti

CV DA ANALIZZARE:
{testo_cv}

RISPOSTA IN QUESTO FORMATO:
LIVELLO: [junior/mid/senior/staff]
PUNTEGGIO: [numero]/100
MOTIVAZIONE: [breve spiegazione]
"""'''

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
