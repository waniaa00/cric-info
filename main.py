import streamlit as st
import feedparser

# Set page config
st.set_page_config(page_title="Cric Info", page_icon="🏏", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 4.5rem; /* Increased size */
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
        margin-bottom: 30px; /* Increased margin for better spacing */
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.4); /* Added text shadow */
    }
    .score-card {
        background-color: #262730; /* Changed to a dark gray */
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3); /* Slightly darker shadow */
    }
    .score-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #f0f2f6; /* Changed to light gray for dark background */
    }
    .score-summary {
        font-size: 1rem;
        color: #cccccc; /* Changed to a lighter gray for dark background */
    }
    .footer {
        font-size: 0.9rem;
        text-align: center;
        color: #888888;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# App header
st.markdown('<p class="main-header">🏏 Cric Info Live 🏏</p>', unsafe_allow_html=True)

# RSS feed URL
RSS_FEED_URL = "https://static.cricinfo.com/rss/livescores.xml"

# Function to fetch and display scores
def display_scores():
    feed = feedparser.parse(RSS_FEED_URL)
    if feed.entries:
        for entry in feed.entries:
            with st.container():
                st.markdown('<div class="score-card">', unsafe_allow_html=True)
                st.markdown(f'<p class="score-title">{entry.title}</p>', unsafe_allow_html=True)
                if 'summary' in entry:
                    st.markdown(f'<p class="score-summary">{entry.summary}</p>', unsafe_allow_html=True)
                st.link_button("Read more", entry.link)
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("No live scores available at the moment.")

# Display scores
display_scores()

# Refresh button
if st.button("Refresh Scores"):
    st.rerun()

st.markdown('<p class="footer">Developed by Wania Akram</p>', unsafe_allow_html=True)
