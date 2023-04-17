import streamlit as st
from st_on_hover_tabs import on_hover_tabs
import pymongo


st.set_page_config(
    page_title="Hackniche",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

st.title("Home Page")

# streamlit_app.py

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# Pull data from the collection.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

# Print results.
for item in items:
    st.write(f"{item['name']} has a :{item['pet']}:")