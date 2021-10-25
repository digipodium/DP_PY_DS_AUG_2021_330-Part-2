import streamlit as st

st.title("The Streamlit example")
st.header("Simple Heading")
st.subheader("Easy subheading")

st.text("something as normal text")
st.success("Cheers to the success")
st.error("thats a failure")
st.info("this is a information msg")
x = ["ray","casting","is",'used','in','3D']
st.text(x)
st.write('better',x)

ans1 = st.checkbox("Do you like Pokemon?")
if ans1:
    st.success("Pokemons are amazing")
else:
    st.warning("You like Shin Chan then?")

choices = ['Avengers','Bahubali',
            'Inception','Other']
fav_movie = st.radio("Which movie you like",choices)
st.write(f"you like {fav_movie}")

fav_movie = st.selectbox("Which Movie",choices)
st.write(f"you like {fav_movie}")

fav_movies = st.multiselect("Which movies",choices)
st.write(f"you like {fav_movies}")

st.image("times_square.jpg")

st.title("A simple Form")

with st.form('form1'):
    name =  st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    age = st.number_input("What is you age",18,75,24)
    doj = st.date_input("When did you join")
    summary = st.text_area("Tell us about yourself")
    photo = st.file_uploader("upload photo")
    btn = st.form_submit_button("Save")


st.subheader("Your Form Detail")
if btn and name and email and summary:
    st.write("name",name)
    st.write("email",email)
    st.write("age",age)
    st.write("date of joining",doj)
    st.write("summary",summary)
    st.write("photo",photo)

