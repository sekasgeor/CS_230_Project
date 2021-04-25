import streamlit as st

from PIL import Image
img = Image.open("pizza.jpg")

st.image(img, width=300)
st.title("Welcome to Build A Pizza")

st.header("Build Your Pizza")
hungry = ['not very','somewhat', 'kind of', 'very', 'super']
st.write("How Hungry are You? ")
x = st.slider('Hungry Index',0.0,4.0,1.0)
st.write('You are ', hungry[int(x)], 'hungry!')
st.write(x)

st.subheader("Delivery")
# Add a selectbox :
delivery = st.selectbox(
    'Delivery Option: ',
    ('Eat-In', 'Curb-Side', 'Delivery')
)

st.write("This order is for ", delivery)

st.subheader("Pizza Options")
sizes = ['small','medium','large','extra large']
size = st.radio("Select a size: ", sizes)

mushrooms = st.checkbox("Mushrooms", False)
cheese = st.checkbox("Extra Cheese", True)
if mushrooms and cheese:
    st.write("Your ", size,  " pizza will have mushrooms and extra cheese.")
elif mushrooms:
    st.write("Your ", size,  " pizza will have mushrooms.")
elif cheese:
    st.write("Your ", size,  " pizza will have extra cheese.")
else:
    st.write("Your ", size, " pizza is plain.")

st.subheader("Meats")
meats = ['Sausage','Meatball','Hamburger','Chicken']
meat_toppings = st.multiselect("Select toppings:", meats)
st.write("We will add: ", meat_toppings)

st.subheader("Soda")
soda = st.number_input("How many bottles of soda: ",0,99,1)

your_name = st.text_input("Name: ", "Mark")
st.write("Thanks,", your_name, " for your order!")

st.write("CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=212424")
