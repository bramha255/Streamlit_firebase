from google.cloud import firestore
import streamlit as st

st.header('Hello Page')

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json(
    "D:/project/Webapp_python/streamlit-firebase.json")


# Create a reference to the Google post.
doc_ref = db.collection("collection").document("document")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())


if st.button('Balloon'):
    st.balloons()

col1, col2 = st.columns(2)
with col1:
    st.write('LED')

with col2:
    radio = st.radio(label='radio', options=('On', 'Off'),
                     key='k1', label_visibility='collapsed', horizontal=True)
