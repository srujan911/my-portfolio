import streamlit as st

st.title("Srujan Jaini")
st.subheader("AI Engineer specializing in Machine Learning and Blockchain Applications")

st.write("Welcome to my digital portfolio! Here you'll find my projects, skills, and journey into the world of technology.")
# --- ABOUT ME ---
st.write("---") # Adds a horizontal line
st.header("About Me")
st.write(
    """
    I'm a final-year Computer Science student passionate about solving problems at the intersection of artificial intelligence and decentralized technology. 
    I believe the combination of AI's predictive power and blockchain's verifiable trust is the future of secure, intelligent systems.
    
    My hands-on experience includes developing predictive models for blockchain analytics and building tools to analyze on-chain data. 
    I am driven by applying cutting-edge technology to solve real-world challenges.
    """
)# --- SKILLS ---
st.write("---")
st.header("Core Competencies")
col1, col2 = st.columns(2) # Create two columns

with col1:
    st.subheader("AI & Machine Learning")
    st.markdown(
        """
        - **Languages & Libraries:** Python, Pandas, NumPy, Scikit-learn
        - **Algorithms:** Predictive Modeling (XGBoost), Classification
        - **Certifications:** Google AI Essentials, Google Prompting Essentials
        """
    )

with col2:
    st.subheader("Blockchain Technology")
    st.markdown(
        """
        - **Concepts:** On-Chain Data Analysis, Smart Contracts
        - **Languages/Tools:** Foundational Solidity, Blockchain APIs
        - **General Tools:** Git, GitHub, VS Code, SQL
        """
    )
# --- PROJECTS ---
st.write("---")
st.header("My Projects")

# --- Project 1 ---
st.subheader("AI-Powered Forecasting for Ethereum Gas Fees")
# st.image("path/to/your/image.png") # Optional: Add a screenshot
st.write(
    """
    Developed a machine learning model using XGBoost to predict volatile gas fees on the Ethereum network. The project involved collecting historical on-chain data, performing rigorous feature engineering, and training the model to provide a practical tool for users to optimize transaction costs.
    """
)
st.link_button("View on GitHub", "https://github.com/srujan911/gas-fee-predictor") # IMPORTANT: Replace with your actual link

# --- Project 2 ---
st.subheader("Cross-Chain Asset Tracker for Stablecoins")
st.write(
    """
    Built a tool to monitor and analyze the movement of USDT tokens across multiple blockchain networks. This project demonstrates an understanding of blockchain data structures and the use of APIs to query and present on-chain information.
    """
)
st.link_button("View on GitHub", "https://github.com/srujan911/cross-chain-token-tracker") # IMPORTANT: Replace link

