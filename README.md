En semantisk musik-sökapp byggd med **Streamlit**, **LangChain**, **ChromaDB** och **HuggingFace embeddings**.  
Projektet gör det möjligt att söka efter Spotify-låtar

## Funktioner

- Naturlig språkbaserad låtsökning
- Vektorbaserad likhetssökning med ChromaDB
- HuggingFace sentence embeddings
- Streamlit-gränssnitt
- Sortering efter:
  - Relevans
  - Danceability
  - Energi
  - Popularitet
  - Tempo
  - Längd

---

# Teknik

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

Beroenden finns i `requirements.txt`.

---

# 📁 Projektstruktur

```bash
.
├── app.py
├── spotify.ipynb
├── requirements.txt
├── .env
├── .gitignore
└── chroma_spotify_db/

```

| Fil | Beskrivning |
|------|-------------|
| `app.py` | Huvudapplikationen |
| `spotify.ipynb` | Notebook för databehandling |
| `requirements.txt` | Python-bibliotek |
| `.env` | API-nycklar och miljövariabler |
| `chroma_spotify_db/` | Chroma vektordatabas |

---
# Installation

## 1. Klona projektet

```bash
git clone <repo-url>
cd spotify-song-finder
```

## 2. Skapa virtuell miljö

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 3. Installera beroenden

```bash
pip install -r requirements.txt
```

---

# ▶️ Starta appen

```bash
streamlit run app.py
```

Öppna sedan:

```bash
http://localhost:8501
```

---

# Hur det fungerar

Projektet använder:

- **HuggingFace embeddings** för att omvandla text till vektorer
- **ChromaDB** för att lagra låtdata
- **LangChain** för semantisk sökning
- **Streamlit** för användargränssnittet

Liknande låtar hämtas med:

```python
vector_store.similarity_search_with_score()
```

---

# Miljövariabler

Skapa en `.env` fil:

```env
GEMINI_API_KEY=your_api_key
```
---

# Viktigt

Databasen måste finnas lokalt:

```bash
./chroma_spotify_db
```

Om databasen saknas kommer appen inte fungera korrekt.

---














├── .gitignore
└── chroma_spotify_db/
```
