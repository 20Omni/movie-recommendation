
import streamlit as st
import pandas as pd

# Load prediction files
itemcf_df = pd.read_csv("itemcf_predictions.csv")
usercf_df = pd.read_csv("usercf_predictions.csv")

# App title
st.title("🎬 Movie Recommendation Dashboard")

# Sidebar selection
option = st.sidebar.selectbox("Choose Recommendation Type", ("Item-Based CF", "User-Based CF"))

# Input: Number of recommendations to display
num_recs = st.sidebar.slider("Number of Recommendations", 5, 20, 10)

# Show recommendations
st.subheader(f"Top {num_recs} Movie Recommendations")

if option == "Item-Based CF":
    st.markdown("🔹 Based on similar items you liked")
    st.dataframe(itemcf_df.head(num_recs))
else:
    st.markdown("🔹 Based on similar users' preferences")
    st.dataframe(usercf_df.head(num_recs))
