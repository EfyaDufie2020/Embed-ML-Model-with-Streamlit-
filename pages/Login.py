import streamlit as st
import bcrypt

# Sample user database (for demo purposes)
# In a real application, this would be stored securely in a database
users_db = {
    "user1": {"password": bcrypt.hashpw("password1".encode(), bcrypt.gensalt()), "role": "user"},
    "admin": {"password": bcrypt.hashpw("adminpass".encode(), bcrypt.gensalt()), "role": "admin"},
}

# Function to verify the password
def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password)

# Login page
def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in users_db and verify_password(users_db[username]["password"], password):
            st.session_state["username"] = username
            st.session_state["role"] = users_db[username]["role"]
            st.success("Login successful")
            st.experimental_rerun()  # Reload the app to reflect the login state
        else:
            st.error("Invalid username or password")

# Admin page
def admin_page():
    st.title("Admin Page")
    st.write("Welcome, admin!")
    st.write("Only admins can see this page.")

# User page
def user_page():
    st.title("User Page")
    st.write("Welcome, user!")
    st.write("This is a page for general users.")

# Main application
def main():
    # Check if the user is logged in
    if "username" not in st.session_state:
        login_page()
    else:
        st.sidebar.title(f"Welcome, {st.session_state['username']}")
        
        # Sidebar menu
        option = st.sidebar.selectbox("Menu", ["Home", "Logout"])
        
        if option == "Logout":
            del st.session_state["username"]
            del st.session_state["role"]
            st.experimental_rerun()

        # Role-based access control
        if st.session_state["role"] == "admin":
            admin_page()
        elif st.session_state["role"] == "user":
            user_page()
        else:
            st.error("Unknown role")

if __name__ == "__main__":
    main()
