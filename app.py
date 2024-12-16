import streamlit as st

# Initialize session state for navigation and inputs
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"  # Default page

if "name" not in st.session_state:
    st.session_state.name = ""

# Function to navigate between pages
def navigate_to(page_name):
    st.session_state.current_page = page_name


# Use a placeholder to dynamically render the active page
page_placeholder = st.empty()

# Render only the active page
with page_placeholder.container():
    if st.session_state.current_page == "Home":
        # Home Page Logic
        st.title("Welcome - :)")

        # Inputs for room name and username
        name = st.text_input("Name")
        # Username = st.text_input("Username")

        # Enter Room Button
        if st.button("Click"):
            if not name.strip():
                st.error("Name cannot be empty!")
            else:

                st.session_state.name = name.strip()
                navigate_to("Wish room")

    elif st.session_state.current_page == "Wish room":
    # Render the wish page
        st.markdown(
            f"""
        <style>
        body {{
            background-color: #f0f8ff; /* Alice Blue background */
        }}
        .wish-container {{
            text-align: center;
            padding: 50px;
            border-radius: 15px;
            background: linear-gradient(to bottom, #a2d9ff, #82caff);
            color: #002d62; /* Navy blue text for contrast */
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        }}
        .wish-container h1 {{
            font-size: 50px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .wish-container h2 {{
            font-size: 30px;
            font-style: italic;
            margin-top: 5px;
        }}
        .wish-container .decorative-line {{
            width: 80%;
            height: 2px;
            background-color: #002d62; /* Navy blue line */
            margin: 20px auto;
        }}
        </style>
        <div class="wish-container">
            <h1>🎉 Happy Birthday 🎉</h1>
            <div class="decorative-line"></div>
            <h2>{st.session_state.name}</h2>
        </div>
        """,
            unsafe_allow_html=True
        )


