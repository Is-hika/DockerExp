import streamlit as st

def main():
    st.title("🚲 Bike Sharing Demand Monitoring")
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Select a report to view")

    st.markdown("### Welcome to Evidently AI Dashboard!")
    st.markdown("Use the sidebar to navigate between projects and reports.")

if __name__ == "__main__":
    main()
