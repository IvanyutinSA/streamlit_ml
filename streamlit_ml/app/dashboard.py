from os.path import realpath, dirname
import sys
if dirname(dirname(dirname(realpath(__file__)))) not in sys.path:
    sys.path.append(dirname(dirname(dirname(realpath(__file__)))))

import streamlit as st
from streamlit_ml.app.rbtree_visualizations import rb_tree
from streamlit_ml.app.dashboard_ml import ml

with st.sidebar:
    st.title('Lab')
    lab_number = st.selectbox('Choose lab number', [1, 2])
lab_number = 0 if lab_number is None else lab_number

labs = {
    1: ml,
    2: rb_tree,
}

labs.get(lab_number, lambda: st.title('UNKNOWN LAB'))()
