import streamlit as st
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

st.set_page_config(page_title="Spotify Song Finder", layout="wide")

st.title("Spotify Song Finder")
st.write("Search songs using your Spotify vector database.")


@st.cache_resource
def load_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory="./chroma_spotify_db",
        embedding_function=embeddings,
        collection_name="spotify"
    )


def parse_song_content(content):
    song_data = {}

    for line in content.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            song_data[key.strip()] = value.strip()

    return song_data


def to_float(value, default=0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def format_duration(ms):
    try:
        ms = int(float(ms))
        minutes = ms // 60000
        seconds = (ms % 60000) // 1000
        return f"{minutes}:{seconds:02d}"
    except (ValueError, TypeError):
        return "Unknown"


vector_store = load_vector_store()
st.success("ChromaDB loaded successfully.")

question = st.text_input(
    "Ask a question about songs:",
    "What songs have high danceability"
)

col_a, col_b = st.columns(2)

with col_a:
    k = st.slider("Number of results", 5, 20, 20)

with col_b:
    sort_by = st.selectbox(
        "Sort results by",
        [
            "Relevance",
            "danceability",
            "energy",
            "popularity",
            "tempo",
            "duration_ms"
        ]
    )

sort_order = st.radio(
    "Sort order",
    ["Highest first", "Lowest first"],
    horizontal=True
)

if st.button("Search"):
    results = vector_store.similarity_search_with_score(question, k=k)

    seen = set()
    songs = []

    for res, score in results:
        content = res.page_content.strip()

        if content not in seen:
            seen.add(content)
            song = parse_song_content(content)
            song["relevance_score"] = score
            songs.append(song)

    if sort_by != "Relevance":
        songs = sorted(
            songs,
            key=lambda song: to_float(song.get(sort_by)),
            reverse=(sort_order == "Highest first")
        )

    if not songs:
        st.warning("No songs found.")
    else:
        st.write(f"Showing {len(songs)} results")

        for index, song in enumerate(songs, start=1):
            with st.container(border=True):
                st.subheader(f"{index}. {song.get('track_name', 'Unknown track')}")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write(f"Artist: {song.get('artists', 'Unknown')}")
                    st.write(f"Album: {song.get('album_name', 'Unknown')}")
                    st.write(f"Genre: {song.get('track_genre', 'Unknown')}")

                with col2:
                    st.write(f"Popularity: {song.get('popularity', 'Unknown')}")
                    st.write(f"Energy: {song.get('energy', 'Unknown')}")
                    st.write(f"Danceability: {song.get('danceability', 'Unknown')}")

                with col3:
                    st.write(f"Tempo: {song.get('tempo', 'Unknown')}")
                    st.write(f"Duration: {format_duration(song.get('duration_ms'))}")
                    st.write(f"Relevance score: {song.get('relevance_score'):.4f}")