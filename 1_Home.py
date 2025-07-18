import streamlit as st
#from streamlit_lottie import st_lottie
import json

# In 1_🏠_Home.py

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css(".streamlit/style.css")

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Srujan Jaini | Digital Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="auto"
)

# Function to load a Lottie file
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# --- HERO SECTION ---
col1, col2 = st.columns([2, 3]) # Adjust column ratio for better balance

with col1:
    st.subheader("Hi, I'm Srujan Jaini 👋")
    st.title("AI & Blockchain Engineer")
    st.write(
        """
        A final-year Computer Science student building intelligent, decentralized solutions. 
        Passionate about the intersection of AI's predictive power and blockchain's verifiable trust.
        """
    )
    # You can add a resume download button here if you like
    # with open("path/to/your/resume.pdf", "rb") as file:
    #     st.download_button("Download My Resume", file, file_name="Srujan_Jaini_Resume.pdf")

# with col2:
#     # --- LOTTIE ANIMATION ---
#     # Create a folder 'lottie' and put your downloaded JSON file there
#     lottie_coding = load_lottiefile("lottie/ai_animation.json") # Replace with your file path
#     st_lottie(
#         lottie_coding,
#         speed=1,
#         reverse=False,
#         loop=True,
#         quality="high",
#         height=400,
#         width=None,
#         key=None,
#     )

# --- SKILLS & ABOUT ---
st.write("---")
st.header("What I Bring to the Table")

# Using tabs for a cleaner layout
tab1, tab2 = st.tabs(["**My Skills** 🤹", "**My Philosophy** 🤔"])

with tab1:
    st.subheader("Technical Toolbox")
    st.markdown(
        """
        - **🤖 AI & Machine Learning:** Python, Pandas, NumPy, Scikit-learn, XGBoost
        - **🔗 Blockchain Technology:** On-Chain Data Analysis, Foundational Solidity, Blockchain APIs
        - **💻 General Development:** Git, GitHub, VS Code, SQL, Streamlit
        - **📜 Certifications:** Google AI Essentials, Google Generative AI Prompting
        """
    )

with tab2:
    st.subheader("My Approach to Technology")
    st.write(
        """
        I believe the most powerful solutions emerge from interdisciplinary thinking. 
        My work is driven by a curiosity to connect different technological fields—like AI and blockchain—to unlock new capabilities. 
        I am a dedicated learner committed to building software that is not only efficient but also secure and trustworthy.
        """
    )



# --- CONTACT ---
st.write("---")
st.header("Get In Touch! 📬")
st.write("I'm currently seeking job opportunities and am open to collaborations. Feel free to reach out!")
st.markdown(
    """
    - **Email:** [jainisrujan@gmail.com](mailto:jainisrujan@gmail.com)
    - **LinkedIn:** [linkedin.com/in/srujan-jaini](https://linkedin.com/in/srujan-jaini-914bb7307)
    - **GitHub:** [github.com/srujan911](https://github.com/srujan911)
    """
)
