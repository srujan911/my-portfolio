import streamlit as st


def project_card(image_path, title, description, github_link, caption=""):
    with st.container(border=True): # The border=True and CSS now work together!
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(image_path, caption=caption)
        with col2:
            st.subheader(title)
            st.write(description)
            st.link_button("View on GitHub", github_link)

# --- Load CSS --- (You need this on every page)
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(".streamlit/style.css")
# --- PROJECTS SECTION ---
st.write("---")
st.header("My Projects 🚀")
# --- Project 1 ---
with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    with col1:
        # Add your project image here
        st.image("images/project1_gas_fees.png", caption="Screenshot of the Gas Fee Predictor") # Create an 'images' folder
    with col2:
        st.subheader("AI-Powered Forecasting for Ethereum Gas Fees")
        st.write(
            """
            Developed an XGBoost model to predict volatile gas fees on the Ethereum network. 
            This tool helps users optimize transaction costs by providing accurate forecasts based on historical on-chain data and feature engineering.
            """
        )
        st.link_button("View on GitHub", "https://github.com/srujan911/gas-fee-predictor")

# --- Project 2 ---
with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    with col1:
        # Add your project image here
        st.image("images/project2_tracker.png", caption="Dashboard of the Cross-Chain Tracker") # Create an 'images' folder
    with col2:
        st.subheader("Cross-Chain Asset Tracker for Stablecoins")
        st.write(
            """
            Built a tool to monitor and analyze the movement of USDT tokens across multiple blockchain networks. 
            This project showcases skills in blockchain data analysis and API integration to present complex data in a clear, user-friendly format.
            """
        )
        st.link_button("View on GitHub", "https://github.com/srujan911/cross-chain-token-tracker")

# In your 2_🚀_Projects.py file, inside the project container

st.write("---")
st.subheader("✨ Simulate the Predictor")

# Simple inputs to mimic your model
base_fee = st.slider("Select a base network fee (in gwei):", 10, 150, 35)
priority_level = st.select_slider(
    "Select transaction priority:",
    options=['Low', 'Medium', 'High']
)

# Dummy logic to simulate prediction
priority_map = {'Low': 1, 'Medium': 3, 'High': 5}
predicted_total_fee = base_fee + priority_map[priority_level]

st.metric(label="Predicted Total Fee (gwei)", value=f"{predicted_total_fee}")

st.caption("This is a simplified interactive demo. The actual project uses a trained XGBoost model.")