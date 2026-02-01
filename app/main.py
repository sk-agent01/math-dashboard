"""Math Dashboard — Streamlit UI for common math operations."""

import streamlit as st
import sys
from pathlib import Path

# Ensure project root is on sys.path so `app` resolves as a package
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.operations import OPERATIONS

st.set_page_config(page_title="Math Dashboard", page_icon="🧮", layout="centered")
st.title("🧮 Math Dashboard")
st.markdown("Select an operation, provide inputs, and get results.")

# --- Sidebar: operation selector ---
op_names = list(OPERATIONS.keys())
selected_op = st.sidebar.selectbox("Operation", op_names)
op = OPERATIONS[selected_op]

st.header(selected_op)
st.caption(op["description"])

# --- Dynamic input rendering ---
inputs: dict = {}
for param in op["params"]:
    key = param["name"]
    if param["type"] == "int":
        inputs[key] = st.number_input(
            param["label"],
            value=param.get("default", 0),
            step=1,
            format="%d",
            key=f"{selected_op}_{key}",
        )
    elif param["type"] == "float":
        inputs[key] = st.number_input(
            param["label"],
            value=float(param.get("default", 0.0)),
            format="%.6f",
            key=f"{selected_op}_{key}",
        )

# --- Compute ---
if st.button("Calculate", type="primary"):
    try:
        result = op["func"](**inputs)
        st.success(f"**Result:** {result}")
    except Exception as e:
        st.error(f"Error: {e}")
