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

st.write("**Software Engineering Intern** – ABC Tech Sdn Bhd (Jun 2024 – Sep 2024)")
st.write("- Developed web applications using Django & React")
st.write("- Implemented REST APIs and optimized backend queries by 20%")
st.write("- Collaborated with a team of 5 engineers in an Agile environment")

st.write("**Research Assistant** – University XYZ (Jan 2023 – Dec 2023)")
st.write("- Conducted research on Deep Learning models for NLP")
st.write("- Published a paper in IEEE Conference 2023")
st.write("- Assisted in teaching Python and Data Analysis labs")

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
# PROJECTS / ACHIEVEMENTS
# -------------------------------
st.subheader("🚀 Projects & Achievements")

st.write("**Stock Market Prediction App** – Built an LSTM model to predict FBMKLCI trends with 85% accuracy.")
st.write("**IoT Livestock Tracker** – Designed IoT-based smart livestock monitoring system for mountainous areas.")
st.write("**Hackathon Winner** – 1st Place in National AI Innovation Hackathon 2024.")
st.write("**Open Source Contributor** – Contributed to NLP libraries on GitHub.")

st.markdown("---")

# -------------------------------
# OTHER INFORMATION
# -------------------------------
st.subheader("🌟 Other Information")

st.write("- Languages: English, Malay, Mandarin")
st.write("- Interests: Artificial Intelligence, Blockchain, Cloud Computing, Startups")
st.write("- Volunteer Work: Tech Mentor at Local Coding Bootcamp")

st.markdown("---")

# Footer
st.caption("© 2025 Your Name | Made with Streamlit")
