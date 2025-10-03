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
        background-color: #87ceeb; /* Sky blue pastel */
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
st.title("💼 POOPATHY A/L RAVI")
st.write("Aspiring Data Scientist | Software Developer | Tech Enthusiast")

# Profile Picture (Optional)
# st.image("profile.jpg", width=150)

# -------------------------------
# CONTACT INFO
# -------------------------------
st.header("📌 Contact Information")
st.write("📧 Email: poopathyswaq@gmail.com")
st.write("📱 Phone: +60 11-17571586")
st.write("🔗 [LinkedIn](https://linkedin.com/in/poopathy-ravi)")
st.write("🌐 [GitHub](https://github.com/Poopathyy)")

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
    st.write("- Cloud: AWS, GCP, Azure")

# -------------------------------
# OTHER INFORMATION
# -------------------------------
st.header("🌟 Other Information")
st.write("- Languages: English, Malay, Mandarin, Tamil")
st.write("- Interests: Artificial Intelligence, Gaming , Cloud Computing, Startups")

# Footer
st.caption("© 2025 POOPATHY | Made with Streamlit")
