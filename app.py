import streamlit as st
import joblib
import random

# Load the trained model
model = joblib.load("feedback_model.pkl")

# Initialize or reset the game
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(0, 9)

st.title("Guess the Number Game")
st.write("Try to guess the number I am thinking of, between 0 and 9!")

# Input field for the user's guess
guess = st.number_input("Enter your guess:", min_value=0, max_value=9, step=1)

# Provide feedback when user submits a guess
if st.button("Submit Guess"):
    # Predict feedback based on the current target number and the user's guess
    feedback = model.predict([[st.session_state.target_number, guess]])[0]
    
    # Decode the feedback
    if feedback == 0:
        st.write("Feedback: Too Low!")
    elif feedback == 1:
        st.write("Feedback: Too High!")
    else:
        st.write("Feedback: Correct! You've guessed the number.")
        # Reset the game by generating a new target number
        st.session_state.target_number = random.randint(0, 9)
        st.write("Let's play again! Try guessing the new number.")