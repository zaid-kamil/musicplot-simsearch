import streamlit
from streamlit_agraph import agraph, Node, Edge, Config
import streamlit as st
import pickle
import pandas as pd


st.set_page_config(layout="wide")


with open('similarity.pkl', 'rb') as f:
    sim_df = pickle.load(f)
    
with open('track_names.pkl', 'rb') as f:
    track_names = pickle.load(f)

df = pd.read_csv('all_tracks.csv')




# function to get the most similar tracks
def get_similar_tracks(track_name, sim_df, num=10):
     df = pd.read_csv('all_tracks.csv')
     track_names = df['trackName'].values.tolist()
     results = []
     track_idx = track_names.index(track_name)
     sim_tracks = sim_df.iloc[track_idx].sort_values(ascending=False)
     # remove duplicate tracks
     sim_tracks = sim_tracks.drop_duplicates()
     sim_tracks = sim_tracks.head(num)
     for idx, score in sim_tracks.items():
          results.append({
               'trackName': df.iloc[idx]['trackName'],
               'artistName': df.iloc[idx]['artistName'],
               'similarity': score
          })
     return results

def get_similar_artists(artist_name, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    artist_names = df['artistName'].values.tolist()
    results = []
    artist_idx = artist_names.index(artist_name)
    sim_artists = sim_df.iloc[artist_idx].sort_values(ascending=False)
    # sim_artists = sim_artists.drop(artist_idx)
    sim_artists = sim_artists.drop_duplicates()
    sim_artists = sim_artists.head(num)
    for idx, score in sim_artists.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_genres(genre, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    genre_names = df['genre'].values.tolist()
    results = []
    genre_idx = genre_names.index(genre)
    sim_genres = sim_df.iloc[genre_idx].sort_values(ascending=False)
    # sim_genres = sim_genres.drop(genre_idx)
    sim_genres = sim_genres.drop_duplicates()
    sim_genres = sim_genres.head(num)
    for idx, score in sim_genres.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_albums(album, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    album_names = df['albumName'].values.tolist()
    results = []
    album_idx = album_names.index(album)
    sim_albums = sim_df.iloc[album_idx].sort_values(ascending=False)
    # sim_albums = sim_albums.drop(album_idx)
    sim_albums = sim_albums.drop_duplicates()
    sim_albums = sim_albums.head(num)
    for idx, score in sim_albums.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_playlists(playlist, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    playlist_names = df['playlistName'].values.tolist()
    results = []
    playlist_idx = playlist_names.index(playlist)
    sim_playlists = sim_df.iloc[playlist_idx].sort_values(ascending=False)
    # sim_playlists = sim_playlists.drop(playlist_idx)
    sim_playlists = sim_playlists.drop_duplicates()
    sim_playlists = sim_playlists.head(num)
    for idx, score in sim_playlists.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_years(year, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    year_names = df['year'].values.tolist()
    results = []
    year_idx = year_names.index(year)
    sim_years = sim_df.iloc[year_idx].sort_values(ascending=False)
    # sim_years = sim_years.drop(year_idx)
    sim_years = sim_years.drop_duplicates()
    sim_years = sim_years.head(num)
    for idx, score in sim_years.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_durations(duration, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    duration_names = df['duration_ms'].values.tolist()
    results = []
    duration_idx = duration_names.index(duration)
    sim_durations = sim_df.iloc[duration_idx].sort_values(ascending=False)
    # sim_durations = sim_durations.drop(duration_idx)
    sim_durations = sim_durations.drop_duplicates()
    sim_durations = sim_durations.head(num)
    for idx, score in sim_durations.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_popularities(popularity, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    popularity_names = df['popularity'].values.tolist()
    results = []
    popularity_idx = popularity_names.index(popularity)
    sim_popularities = sim_df.iloc[popularity_idx].sort_values(ascending=False)
    # sim_popularities = sim_popularities.drop(popularity_idx)
    sim_popularities = sim_popularities.drop_duplicates()
    sim_popularities = sim_popularities.head(num)
    for idx, score in sim_popularities.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_acousticness(acousticness, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    acousticness_names = df['acousticness'].values.tolist()
    results = []
    acousticness_idx = acousticness_names.index(acousticness)
    sim_acousticness = sim_df.iloc[acousticness_idx].sort_values(ascending=False)
    # sim_acousticness = sim_acousticness.drop(acousticness_idx)
    sim_acousticness = sim_acousticness.drop_duplicates()
    sim_acousticness = sim_acousticness.head(num)
    for idx, score in sim_acousticness.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_danceability(danceability, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    danceability_names = df['danceability'].values.tolist()
    results = []
    danceability_idx = danceability_names.index(danceability)
    sim_danceability = sim_df.iloc[danceability_idx].sort_values(ascending=False)
    # sim_danceability = sim_danceability.drop(danceability_idx)
    sim_danceability = sim_danceability.drop_duplicates()
    sim_danceability = sim_danceability.head(num)
    for idx, score in sim_danceability.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_energy(energy, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    energy_names = df['energy'].values.tolist()
    results = []
    energy_idx = energy_names.index(energy)
    sim_energy = sim_df.iloc[energy_idx].sort_values(ascending=False)
    # sim_energy = sim_energy.drop(energy_idx)
    sim_energy = sim_energy.drop_duplicates()
    sim_energy = sim_energy.head(num)
    for idx, score in sim_energy.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_instrumentalness(instrumentalness, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    instrumentalness_names = df['instrumentalness'].values.tolist()
    results = []
    instrumentalness_idx = instrumentalness_names.index(instrumentalness)
    sim_instrumentalness = sim_df.iloc[instrumentalness_idx].sort_values(ascending=False)
    sim_instrumentalness = sim_instrumentalness.drop(instrumentalness_idx)
    # sim_instrumentalness = sim_instrumentalness.head(num)
    sim_instrumentalness = sim_instrumentalness.drop_duplicates()
    for idx, score in sim_instrumentalness.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_liveness(liveness, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    liveness_names = df['liveness'].values.tolist()
    results = []
    liveness_idx = liveness_names.index(liveness)
    sim_liveness = sim_df.iloc[liveness_idx].sort_values(ascending=False)
    # sim_liveness = sim_liveness.drop(liveness_idx)
    sim_liveness = sim_liveness.drop_duplicates()
    sim_liveness = sim_liveness.head(num)
    for idx, score in sim_liveness.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_loudness(loudness, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    loudness_names = df['loudness'].values.tolist()
    results = []
    loudness_idx = loudness_names.index(loudness)
    sim_loudness = sim_df.iloc[loudness_idx].sort_values(ascending=False)
    # sim_loudness = sim_loudness.drop(loudness_idx)
    sim_loudness = sim_loudness.drop_duplicates()
    sim_loudness = sim_loudness.head(num)
    for idx, score in sim_loudness.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_speechiness(speechiness, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    speechiness_names = df['speechiness'].values.tolist()
    results = []
    speechiness_idx = speechiness_names.index(speechiness)
    sim_speechiness = sim_df.iloc[speechiness_idx].sort_values(ascending=False)
    sim_speechiness = sim_speechiness.drop(speechiness_idx)
    # sim_speechiness = sim_speechiness.head(num)
    sim_speechiness = sim_speechiness.drop_duplicates()
    for idx, score in sim_speechiness.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_tempo(tempo, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    tempo_names = df['tempo'].values.tolist()
    results = []
    tempo_idx = tempo_names.index(tempo)
    sim_tempo = sim_df.iloc[tempo_idx].sort_values(ascending=False)
    # sim_tempo = sim_tempo.drop(tempo_idx)
    sim_tempo = sim_tempo.drop_duplicates()
    sim_tempo = sim_tempo.head(num)
    for idx, score in sim_tempo.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results

def get_similar_valence(valence, sim_df, num=10):
    df = pd.read_csv('all_tracks.csv')
    valence_names = df['valence'].values.tolist()
    results = []
    valence_idx = valence_names.index(valence)
    sim_valence = sim_df.iloc[valence_idx].sort_values(ascending=False)
    sim_valence = sim_valence.drop(valence_idx)
    # sim_valence = sim_valence.head(num)
    sim_valence = sim_valence.drop_duplicates()
    for idx, score in sim_valence.items():
        results.append({
            'trackName': df.iloc[idx]['trackName'],
            'artistName': df.iloc[idx]['artistName'],
            'similarity': score
        })
    return results


st.title("Music Plot")
st.sidebar.title("Settings")

st.sidebar.subheader("Select a similarity logic")

cols = df.columns.tolist()
cols.remove('key')
# st.write(cols)
op = st.sidebar.radio("Select a vector similariry logic", ['trackName', 'artistName', 'genre', 'danceability', 'energy', 'duration_ms'])
size = st.sidebar.slider("Number of similar tracks", 5, 25, 5)
radius = st.sidebar.slider("Node size", 5, 50, 25)


selection = st.sidebar.selectbox("Select a track", df[op].unique().tolist())

if op == 'trackName':
     with st.spinner("Finding similar tracks..."):
          similar_tracks = get_similar_tracks(selection, sim_df, num=size)
elif op == 'artistName':
     with st.spinner("Finding similar artists..."):
          similar_tracks = get_similar_artists(selection, sim_df, num=size)
elif op == 'genre':
     with st.spinner("Finding similar genres..."):
          similar_tracks = get_similar_genres(selection, sim_df, num=size)
elif op == "danceability":
     with st.spinner("Finding similar danceability..."):
          similar_tracks = get_similar_danceability(selection, sim_df, num=size)
elif op == "energy":
     with st.spinner("Finding similar energy..."):
          similar_tracks = get_similar_energy(selection, sim_df, num=size)
elif op == "duration_ms":
     with st.spinner("Finding similar durations..."):
          similar_tracks = get_similar_durations(selection, sim_df, num=size)
else:
     similar_tracks = []

if similar_tracks:
     st.sidebar.success("Found similar tracks!")
     nodes = []
     edges = []
     for item in similar_tracks:
          if item['similarity'] > 0.9:
               color = "#00FF00"
          elif item['similarity']> 0.85:
               color = "#FFFF00"
          elif item['similarity']> 0.8:
               color = "#FF0000"
          elif item['similarity'] > 0.7:
               color = "#FFA500"
          else:
               color = "#0000FF"
          nodes.append(Node(id=item['trackName'],
               label=item['trackName'],
               color=color,
               size=radius,
               shape="circularImage",
               image="https://img.icons8.com/ios/452/music--v1.png")
          )
          edges.append(Edge(
               source=item['trackName'],
               label=f"{item['similarity']:.2f}",
               target=similar_tracks[0]['trackName'],
               color='white'
          ))
     
     config = Config(width=1800,
               height=1000,
               directed=False,
               physics=True,
               hierarchical=True,
               node_spacing=300,
               tree_spacing=300,
               parentCentralization = True,
               edgeMinimization= True,
               shakeTowards = 'roots',
               levelSeparation=150,
               minVelocity=1,
     )
     return_value = agraph(nodes=nodes,
                         edges=edges,
                         config=config)
     
     sdf = pd.DataFrame(similar_tracks)
     sdf.similarity = sdf.similarity * 100
     st.dataframe(sdf, column_config={
          'similarity': st.column_config.ProgressColumn(
               "score",
               help="Similarity score between 0 and 1",
               format="%.2f%%",
               min_value=10,
               max_value=100,
               width='large'
          )
     }, 
     use_container_width=True,
     height=300)
     
else:
     st.error("No similar tracks found!")



