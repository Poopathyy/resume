import streamlit as st

# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Resume | POOPATHY", page_icon="💼", layout="wide")

# Background color (light pastel)
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9f9; /* Sky blue pastel */
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# HEADER
# -------------------------------
col1, col2 = st.columns([1, 3])
with col1:
    st.image("profilePic.jpeg", width=200")

with col2:
    st.title("POOPATHY A/L RAVI")
    st.write("Software Developer | Tech Enthusiast")
    st.write("📍Johor, Malaysia")
    st.write("📧 Email: poopathyswaq@gmail.com")
    st.write("📱 Phone: +60 11-17571586")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/poopathy-ravi)")
    st.write("🌐 [GitHub](https://github.com/Poopathyy)")

st.markdown("---")

# -------------------------------
# EDUCATION
# -------------------------------
st.header("🎓 Education")
st.write("**Diploma in Information Technology** – POLITEKNIK SEBERANG PERAI, PENANG(2019 – 2022)")
st.write("- CGPA: 3.75/4.00")
st.write("**Bachelor of Information Technology (HONS)** – UNIVERSITY MALAYSIA KELANTAN(2023 – PRESENT)")
st.write("- CGPA: 3.42/4.00")
st.write("- Relevant Coursework: Data Structures, Machine Learning, Databases, Cloud Computing")

# -------------------------------
# WORK EXPERIENCE
# -------------------------------
st.header("💼 Work Experience")

st.write("**Human Resource Assistant** – ACA Elite Sdn Bhd, Melaka (April 2022 – July 2022)")
st.write("- Supported administrative functions and staff coordination")
st.write("- Maintained and organized employee records")

st.write("**Waiter** – GENTING HIGHLANDS, PAHANG (Dec 2018 – April 2029)")
st.write("- Provided high-quality customer service in a fast-paced environment")
st.write("- Developed communication and teamwork skills")

# -------------------------------
# SKILLS
# -------------------------------
st.header("🛠️ Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("- Python")
    st.write("- R / MATLAB")
    st.write("- SQL")

with col2:
    st.write("- Machine Learning (Scikit-learn, TensorFlow, PyTorch)")
    st.write("- Data Visualization (Matplotlib, Seaborn, Power BI)")

with col3:
    st.write("- Web Development (Django, Flask, React)")
    st.write("- JAVA")

# -------------------------------
# OTHER INFORMATION
# -------------------------------
st.header("🌟 Other Information")
st.write("- Languages: English, Malay, Mandarin, Tamil")
st.write("- Interests: Artificial Intelligence, Gaming , Cloud Computing, Startups")

