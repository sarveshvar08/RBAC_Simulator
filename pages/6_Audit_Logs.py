import streamlit as st
import pandas as pd

from utils.data_manager import load_data
from config.settings import AUDIT_LOGS_FILE


st.title("Security Audit Logs")

st.caption(
    "Monitor successful and denied access attempts."
)

logs = load_data(AUDIT_LOGS_FILE)

if not logs:

    st.info("No audit records available.")

else:

    df = pd.DataFrame(logs)

    total = len(df)

    allowed = len(
        df[df["status"] == "ALLOWED"]
    )

    denied = len(
        df[df["status"] == "DENIED"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Requests", total)
    col2.metric("Allowed", allowed)
    col3.metric("Denied", denied)

    st.divider()

    st.subheader("All Access Attempts")

    st.dataframe(
        df.iloc[::-1],
        use_container_width=True
    )

    st.subheader("Access Decision Distribution")

    st.bar_chart(
        df["status"].value_counts()
    )