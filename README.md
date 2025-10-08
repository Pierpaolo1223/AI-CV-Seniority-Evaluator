# 🧪 CV Seniority Analyzer - Prototipo Sperimentale

**Un esperimento per testare se l'AI può aiutare nell'analisi iniziale dei CV.** 
Per ora fa una cosa semplice: legge (quasi) qualsiasi PDF e prova a valutare se è un CV e che seniority ha.

## 🎯 Doppia Funzionalità

### **1. Riconoscimento CV**
- 🔍 **Analizza il documento** per capire se è un CV
- ✅ **Conferma** se riconosce le sezioni tipiche (esperienza, educazione, skills)
- ❌ **Rifiuta** documenti non-CV con spiegazione

### **2. Valutazione Seniority** 
- 📊 **Solo se è un CV** procede con l'analisi di seniority
- 📝 **Motivazione trasparente** delle decisioni

## 🛠 **Prerequisiti di Sistema**

### **Software Richiesto**
- **PyCharm** - IDE consigliato per lo sviluppo
- **Python 3.10.12** - Versione specifica di Python
- **Git** - Per il controllo versione

### **Account e API**
- **Account Google** - Per ottenere l'API Key Gemini
- **API Key Gemini** - [Ottienila gratuitamente qui](https://aistudio.google.com)

### **Connettività**
- **Connessione Internet** - Necessaria per le chiamate API a Gemini

## 🤖 Perché Google Gemini

Ho scelto di utilizzare **Google Gemini** per questo prototipo perché:

- **💰 Completamente gratuito** per l'uso personale e progetti PoC
- **🎯 Accuratezza sufficiente** per lo scopo del progetto
- **🚀 Facile integrazione** con le API Python
- **📚 Documentazione eccellente** e community attiva

*Per un Proof of Concept, Gemini offre il miglior bilanciamento tra costo zero e qualità delle risposte, senza i limiti di budget che avrebbero imposto soluzioni a pagamento come OpenAI.*

## 🚀 Istruzioni per l'Esecuzione

### **1. Configurazione API Key**
- Ottieni una API Key gratuita da [Google AI Studio](https://makersuite.google.com/)
- Crea un file `.env` nella root del progetto
- Aggiungi la seguente riga al file:
GEMINI_API_KEY=la_tua_api_key_qui

text

### **2. Installazione Dipendenze**
- Apri il terminale nella **cartella root del progetto**
- Esegui il comando:
```bash
pip install -r requirements.txt
3. Esecuzione del Programma
Dal terminale, sempre nella cartella root, esegui:

bash
python3 main.py
Segui le istruzioni a schermo per inserire il percorso del PDF da analizzare

💡 Suggerimenti
Assicurati di essere nella directory corretta prima di eseguire i comandi

Il file .env deve essere nella stessa cartella di main.py

Per verificare il funzionamento, prova con un CV in formato PDF semplice

## 🔮 Visione Futura

### **Potenziale Evoluzione**
Questo prototipo potrebbe rappresentare la **base concettuale** per:

- **🔄 Sostituire sistemi ATS tradizionali** basati su keyword matching
- **🎯 Introdurre valutazioni più intelligenti** e basate su competenze reali
- **📊 Creare strumenti di recruiting** più trasparenti e oggettivi

### **Perché è Diverso dagli ATS Attuali**
| Feature | ATS Tradizionale | Questo Approccio |
|---------|------------------|------------------|
| **Valutazione** | Keyword counting | Analisi contestuale |
| **Trasparenza** | Black box | Reasoning esplicito |
| **Focus** | Anni esperienza | Competenze dimostrate |

**Nota:** *Questo è solo un prototipo funzionale, ma dimostra che un approccio alternativo è possibile.*