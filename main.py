import streamlit as st

# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Resume | POOPATHY", page_icon="💼", layout="wide")

# Custom CSS for colors & styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    h1 {
        color: #2c3e50;
    }
    h2, h3, h4 {
        color: #16a085;
    }
    .contact-info {
        background-color: #ecf0f1;
        padding: 10px;
        border-radius: 8px;
    }
    .section {
        padding: 15px;
        margin-bottom: 20px;
        border-left: 5px solid #16a085;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------------------
# HEADER
# -------------------------------
st.markdown("💼 POOPATHY A/L RAVI")
st.write("Aspiring Data Scientist | Software Developer | Tech Enthusiast")

# Profile Picture (Optional)
# st.image("profile.jpg", width=150)

# -------------------------------
# CONTACT INFO
# -------------------------------
st.markdown("📌 Contact Information")
with st.container():
    st.markdown(
        """
        <div class="contact-info">
            📧 <b>Email:</b> poopathyswaq@gmail.com
            📱 <b>Phone:</b> +60 11-17571586 
            🔗 <b>LinkedIn:</b> <a href="https://linkedin.com/in/poopathy-ravi" target="_blank">linkedin.com/in/poopathy-ravi</a>  
            🌐 <b>GitHub:</b> <a href="https://github.com/Poopathyy" target="_blank">github.com/Poopathyy</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------
# EDUCATION
# -------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("🎓 Education")
st.write("**Diploma in Information Technology** – POLITEKNIK SEBERANG PERAI, PENANG(2019 – 2022)")
st.write("- CGPA: 3.75/4.00")
st.write("**Bachelor of Information Technology (HONS)** – UNIVERSITY MALAYSIA KELANTAN(2023 – PRESENT)")
st.write("- CGPA: 3.42/4.00")
st.write("- Relevant Coursework: Data Structures, Machine Learning, Databases, Cloud Computing")

# -------------------------------
# WORK EXPERIENCE
# -------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### 💼 Work Experience")

st.write("**Human Resource Assistant** – ACA Elite Sdn Bhd, Melaka (April 2022 – July 2022)")
st.write("- Supported administrative functions and staff coordination")
st.write("- Maintained and organized employee records")

st.write("**Waiter** – GENTING HIGHLANDS, PAHANG (Dec 2018 – April 2029)")
st.write("- Provided high-quality customer service in a fast-paced environment")
st.write("- Developed communication and teamwork skills")
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# SKILLS
# -------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### 🛠️ Skills")

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
st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# OTHER INFORMATION
# -------------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("### 🌟 Other Information")
st.write("- Languages: English, Malay, Mandarin, Tamil")
st.write("- Interests: Artificial Intelligence, Gaming , Cloud Computing, Startups")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.caption("© 2025 POOPATHY | Made with Streamlit")
