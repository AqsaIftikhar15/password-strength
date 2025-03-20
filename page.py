import streamlit as st

st.set_page_config(
    page_icon ="🗝️",
    page_title="Password Strength Meter",
)

st.title("Password Strength Checker🔐")
st.markdown("""
### Use this is app to get a critical analysis of your passwords!🕵️‍♀️
            We totally *don't* judge if it’s 'password123' followed by your birth year!
""")

password = st.text_input("Enter your password: ", type="password")


def password_strength_checker(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password shorter than a goldfish's attention span🐠.")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Numbers? ever heard of them 🔢?")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Capital letters are for fancy people 💅")
    
    if not password.isalnum():
        score += 1
    else:
        feedback.append("Special characters? Too mainstream✨")

    return score , feedback

if password:
    score, feedback = password_strength_checker(password)
    st.subheader("Brutal Honest Assessment:")

    for f in feedback:
        st.error(f)
    st.write(f"Security Score: {score}/4 (Congratulations, you tried 🎉)")