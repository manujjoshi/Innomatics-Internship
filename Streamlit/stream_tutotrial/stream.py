import streamlit as st
import pandas as pd
import datetime
import numpy as np

st.title('Text Elements')
st.title('st.title => Manuj Joshi')
st.header('st.header => Manuj Joshi')
st.markdown('st.markdown => Manuj Joshi')
st.subheader('st.subheader => Manuj Joshi')
st.caption('st.caption => Manuj Joshi')
st.code('st.code => Manuj Joshi')
st.text('st.text => Manuj Joshi')
st.latex(r'''st.latex => 
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')

st.title('Display Elements => dataframe')
data = pd.read_csv('IRIS.csv')
st.dataframe(data=data)

st.title('Input widgets')
if st.button('Press me'):
    st.write('you are a good boy')
else:
    st.write('follow text, else you are a bad boy')
    
binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('Download file', binary_contents)

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
    
genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
    
# option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
# st.write('You selected:', option)

options = st.multiselect('What are your favorite colors',['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])
st.write('You selected:', options)
    
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

color = st.select_slider('Select a color of the rainbow',
options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
    
number = st.number_input('Insert a number')
st.write('The current number is ', number)

txt = st.text_area('Text to analyze', '''I am a good boy''')
st.write('you can give any transformation function', str.upper(txt))
    
d = st.date_input("When's your birthday",datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

t = st.time_input('Set an alarm for', datetime.time(9, 45))
st.write('Alarm is set for', t)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
    
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.title('Media Elements')
from PIL import Image
image = Image.open('canada.jpg')
st.image(image, caption='Sunrise by the mountains')
st.subheader('Like this there is for audio and video')
    
st.title('Layouts and containers')
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)


col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
with st.expander("See explanation"):
    st.write("""
...         The chart above shows some numbers I picked for you.
...         I rolled actual dice for these, so they're *guaranteed* to
...         be random.
...     """)
    st.image("https://static.streamlit.io/examples/dice.jpg")
    
with st.container():
    st.write("This is inside the container")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))
    st.write("This is outside the container")
    
# import time
# with st.empty():
#     for seconds in range(60):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#         st.write("✔️ 1 minute over!")
        
st.title('Control Flow')

# name = st.text_input('Name')
# if not name:
#     st.warning('Please input a name.')
#     st.stop()
# st.write('Welcome!!',name)
# st.success('Thank you for inputting a name.')

with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
    st.write("Outside the form")

# form = st.form("my_form")
# form.slider("Inside the form")
# st.slider("Outside the form")
# # Now add a submit button to the form:
# form.form_submit_button("Submit")