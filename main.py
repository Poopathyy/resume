import streamlit as st

# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Resume | Your Name", page_icon="💼", layout="wide")

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
st.subheader("📌 Contact Information")
col1, col2 = st.columns(2)
with col1:
    st.write("📧 Email: poopathyswaq@gmail.com")
    st.write("📱 Phone: +60 11-175771586")
with col2:
    st.write("🔗 [LinkedIn](https://linkedin.com/in/poopathy-ravi)")
    st.write("🌐 [GitHub](https://github.com/Poopathyy)")

st.markdown("---")

# -------------------------------
# EDUCATION
# -------------------------------
st.subheader("🎓 Education")
st.write("**Diploma in Information Technology** – POLITEKNIK SEBERANG PERAI, PENANG(2019 – 2022)")
st.write("- CGPA: 3.75/4.00")
st.write("**Bachelor of Information Technology (HONS) ** – POLITEKNIK SEBERANG PERAI, PENANG(2023 – PRESENT)")
st.write("- CGPA: 3.42/4.00")
st.write("- Relevant Coursework: Data Structures, Machine Learning, Databases, Cloud Computing")

st.markdown("---")

# -------------------------------
# WORK EXPERIENCE
# -------------------------------
st.subheader("💼 Work Experience")

st.write("**Human Resource Assistant** – ACA Elite Sdn Bhd, Melaka (April 2022 – July 2022)")
st.write("- Supported administrative functions and staff coordination")
st.write("- Maintained and organized employee records")

st.write("**Waiter** – GENTING HIGHLANDS, PAHANG (Dec 2018 – April 2029)")
st.write("- Provided high-quality customer service in a fast-paced environment")
st.write("- Developed communication and teamwork skills")

st.markdown("---")

# -------------------------------
# SKILLS
# -------------------------------
st.subheader("🛠️ Skills")

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

st.markdown("---")

# -------------------------------
# OTHER INFORMATION
# -------------------------------
st.subheader("🌟 Other Information")

st.write("- Languages: English, Malay, Mandarin, Tamil")
st.write("- Interests: Artificial Intelligence, Gaming , Cloud Computing, Startups")

st.markdown("---")

# Footer
st.caption("© 2025 POOPATHY | Made with Streamlit")
