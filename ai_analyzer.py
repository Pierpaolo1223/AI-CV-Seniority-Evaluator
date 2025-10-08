import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
from config import PROMPT_ANALISI

load_dotenv()

# Configura Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


def detect_cv_with_ai(text):
    """
    Usa l'AI per determinare se il testo è un CV
    """
    prompt = f"""
Analizza questo testo e determina se si tratta di un Curriculum Vitae (CV/Resume) o di altro.

CRITERI DI VALUTAZIONE CV:
- Presenza di esperienze lavorative con date
- Sezioni come: istruzione, competenze, formazione o termini analoghi
- Dati personali e contatti
- Struttura organizzata in sezioni
- Descrizione di ruoli professionali

TESTO DA ANALIZZARE:
{text[:3000]}  # Limita per efficienza

RISPOSTA IN FORMATO JSON:
{{
    "is_cv": true/false,
    "reason": "breve spiegazione",
    "document_type": "CV/Lettera/Altro",
    "missing_elements": ["lista elementi mancanti se non è CV"]
}}
"""
    try:
        model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-09-2025')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,
                max_output_tokens=1000,
            )
        )

        return extract_json_from_response(response.text)

    except Exception as e:
        return {
            "is_cv": False,
            "reason": f"Errore durante l'analisi: {str(e)}",
            "document_type": "Errore",
            #"missing_elements": []
        }
    #return response.text


def analizza_cv_con_gemini(testo_cv):

    '''generate_content_models = []
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            generate_content_models.append(model)
            print(f"✅ {model.name}")
            print(f"   Metodi supportati: {', '.join(model.supported_generation_methods)}")
            if hasattr(model, 'description'):
                print(f"   Descrizione: {model.description}")
            print()

    print(f"\n🎯 Totale modelli per generateContent: {len(generate_content_models)}")'''

    """Analizza CV usando Google Gemini"""

    prompt_analisi = PROMPT_ANALISI.format(testo_cv=testo_cv)

    try:
        # Usa il modello Gemini Pro
        model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-09-2025')
        response = model.generate_content(
            prompt_analisi,
            generation_config=genai.types.GenerationConfig(
                temperature=0.2,
                max_output_tokens=2000,
                top_k=40,
                top_p=1
            )
        )

        return response.text

    except Exception as e:
        return f"❌ Errore con Gemini: {e}"


def extract_json_from_response(text):
    import re

    # ✅ Pattern MIGLIORATO - cerca qualsiasi cosa tra { e }
    json_pattern = r'\{.*\}'
    matches = re.finditer(json_pattern, text, re.DOTALL)

    for match in matches:
        try:
            json_data = json.loads(match.group())
            # ✅ NORMALIZZA i boolean
            if 'is_cv' in json_data and isinstance(json_data['is_cv'], str):
                json_data['is_cv'] = json_data['is_cv'].lower() == 'true'
            return json_data
        except json.JSONDecodeError:
            continue

    # Strategia 2: Parsing diretto
    try:
        json_data = json.loads(text.strip())
        if 'is_cv' in json_data and isinstance(json_data['is_cv'], str):
            json_data['is_cv'] = json_data['is_cv'].lower() == 'true'
        return json_data
    except json.JSONDecodeError:
        pass

    # Strategia 3: Fallback
    return {
        "is_cv": "cv" in text.lower(),
        "confidence": "media",
        "reason": "Analisi tramite fallback",
        "document_type": "Da contesto",
        "missing_elements": [],
        "raw_text": text
    }