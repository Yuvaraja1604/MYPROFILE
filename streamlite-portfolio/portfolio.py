import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import requests
import webbrowser

# Function to convert image to base64
def get_base64_image(image_path_or_url):
    if image_path_or_url.startswith('http://') or image_path_or_url.startswith('https://'):
        response = requests.get(image_path_or_url)
        if response.status_code == 200:
            return base64.b64encode(response.content).decode()
        else:
            raise ValueError("Failed to fetch image from URL.")
    else:
        with open(image_path_or_url, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()


# Path to your background image
background_image_path = r"https://raw.githubusercontent.com/Yuvaraja1604/MYPROFILE/main/streamlite-portfolio/probg3.avif"
background_image_base64 = get_base64_image(background_image_path)

# Path to your profile image
# Path to your profile image (use the raw URL)
profile_image_path = r"https://raw.githubusercontent.com/Yuvaraja1604/MYPROFILE/main/streamlite-portfolio/Profile%20pics.jpg"
profile_image_base64 = get_base64_image(profile_image_path)

# Inject custom CSS with Streamlit
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{background_image_base64}");
        background-size: cover;
        background-position: center;
    }}

    .profile-container {{
        display: flex;
        align-items: center;
        margin: 20px;
    }}
    .profile-image {{
        border-radius: 50%;
        width: 150px;
        height: 150px;
        margin-right: 20px;
    }}
    .profile-text {{
        max-width: 600px;
        color: #40E0D0;
    }}
    .header-text {{
        color: #FFFF00; /* Change this color to your preference */
    }}
    .header-text1 {{
        color:#FFA07A; /* Change this color to your preference */
    }}
    .profile-text1 {{
        max-width: 600px;
        color: #FF00FF;
    }}
    .profile-text2 {{
        max-width: 600px;
        color: #40E0D0;
    }}
    .profile-text3 {{
        max-width: 600px;
        color:#00FF00;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# Title of the Portfolio
st.markdown(
    f"""
    <div class="profile-container">
        <img src="data:image/jpeg;base64,{profile_image_base64}" class="profile-image" />
        <div class="profile-text">
            <h1 class="header-text">About Me</h1>
            <p> Hi, I am Yuvarajasimha Reddy, a B.Tech graduate in Computer Science and Engineering (CSE) with a specialization in Data Science from SRM-AP University. I possess a solid foundation in machine learning and web development, with hands-on experience in completing various projects. Proficient in Python,Java, and C++, I am eager to apply my skills to innovative, real-time projects.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# Section: Internship
st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text3">
            <h1 class="header-text1">Internship</h1>
            <h4 class="header-text">Intern At Andhra Pradesh State Skill Development Corporation (APSSDC)</h4>
            <p>Developed a Room Booking System project and Online Voting System project using Django for the back-end, HTML, CSS, and Bootstrap for the front end, and SQLite for database management. Gained hands on experience in full-stack development and efficient data handling.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# section: PROJECTS
st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text3">
            <h1 class="header-text">PROJECTS</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text3">
            <h3 style="color: #FFFFFF;">Project 1: Climate change Monitoring and Analysis</h3>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text1">
            <p>In This Project,Offers essential weather and climate 
information through a front-end developed with HTML, CSS, and Bootstrap, and a back-end built using 
Django, Python, and SQLite3. It includes machine learning algorithms and data visualization techniques 
for accurate predictions and representations. 
• Key features of the CCMA project include basic weather information via API, climate change data 
visualization, prediction tools, and news alerts.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("""
         [GitHub link](https://github.com/Yuvaraja1604/climate-change-Monitoring-and-Analysis)
""")
st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text3">
            <h3 style="color: #FFFFFF;">Project 2: Hotel Room Booking System</h3>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text2">
            <p>In This Project, We developed a comprehensive hotel room booking system that features user registration and 
cancellation capabilities. Users can register for various room types, cancel reservations, and receive 
email updates on their registration status. 
• The system provides administrators with tools to view statistics and manage registration records. 
The project was built using Django for the back-end, HTML, CSS, and Bootstrap for the front-end, 
and SQLite3 for database management.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("""
         [GitHub link](https://github.com/Yuvaraja1604/Intern-At-APSSDC)
""")


# Section: Skills
st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text3">
            <h1 class="header-text1">Skills</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# Using HTML and CSS to add colors
st.markdown(
    """
    <div style="font-size: 18px;">
        <ul>
            <li><strong style="color: #FFA07A;">Programming Languages</strong>: <strong style="color: #FFFFFF;">Python, Java, C++, SQL</strong></li>
            <li><strong style="color: #87CEFA;">Libraries/Tools</strong>: <strong style="color: #FFFFFF;">Pandas, NumPy, Scikit-Learn, TensorFlow</strong></li>
            <li><strong style="color: #98FB98;">Front-End/Tools</strong>: <strong style="color: #FFFFFF;">HTML, CSS, Bootstrap, JavaScript</strong></li>
            <li><strong style="color: #FFD700;">Back-End/Tools</strong>: <strong style="color: #FFFFFF;">Django Framework</strong></li>
            <li><strong style="color: #FF6347;">Others</strong>: <strong style="color: #FFFFFF;">Data Visualization, Statistical Analysis, Machine Learning</strong></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)


# Section: Contact
st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-text3">
            <h1 class="header-text">Contact</h1>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
# Button to open GitHub link
if st.button('Visit My GitHub'):
    webbrowser.open_new_tab('https://github.com/Yuvaraja1604')

# Button to open LinkedIn link
if st.button('Visit My LinkedIn'):
    webbrowser.open_new_tab('https://www.linkedin.com/in/yuvarajasimha-reddy-chitta-49463524b')

