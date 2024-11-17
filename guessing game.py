import streamlit as st 
st.write("WELCOME TO GUESSING GAME")
st.write("Think a number between 1 to 100")
low=0
high=100
step=0
while low<=high:
    mid=(low+high)//2
    response=input("is you guessed"+str(mid)+"(reply 'yes'or 'low' or 'high')")
    if response=="yes":
        st.write("yes i won the game")
        step+=1
        break
    elif response=="low":
        step+=1
        high=mid-1
    elif response=="high":
        step+=1
        low=mid-1
    else:
        st.write("invalid input")
st.write("it takes",step,"step")