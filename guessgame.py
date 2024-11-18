import streamlit as st 
import random

st.title("NUMBER GUESSING GAME")
st.write("I am guessing number between 1 to 100")
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1,100)
    st.session_state.attempts=0
user_guess=st.number_input("your guess:", min_value=1 , max_value=100 , step=1)
if st.button("submit guess"):
    st.session_state.attempts += 1
    if user_guess<st.session_state.number:
        st.write("too low!","try again.")
    elif user_guess>st.session_state.number:
        st.write("too high!","try again")
    else:
        st.write(f"congratulations!","you guessed the number in {st.session_state.attempts} attempt.")
        if st.button("play again"):
            st.session_state.number=random.randint(1,100)
            st.session_state.attempts=0
if st.session_state.attempts>0:
    st.write(f"attempts:{st.session_state.attempts}")
    