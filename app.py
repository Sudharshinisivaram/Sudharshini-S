import streamlit as st
import pickle

st.title("Sales Oracle")

Item_Weight= st.number_input("Insert the Item_Weight")
Item_Fat_Content= st.number_input("Insert the Item_Fat_Content")
Item_Visibility= st.number_input("Insert the Item_Visibility")

Item_MRP=st.number_input("Insert the Item_MRP")
Outlet_Location_Type=st.number_input("Insert the Outlet_Location_Type")
Outlet_Type=st.number_input("Insert the Outlet_Type")




submit = st.button("Predict")
if submit:
    with open(r"model.pickle","rb") as f:
        mp=pickle.load(f)
        
    output=mp.predict([[Item_Weight,Item_Fat_Content,Item_Visibility,Outlet_Type,Item_MRP,Outlet_Location_Type]])
    a = (output[0])
    if(a==0):
        c="Grocery store in hike"
    elif(a==1):
        c="Supermarket Type1 in hike"
    elif(a==2):
        c="Supermarket Type2 in hike"
    elif(a==3):
        c="Supermarket Type3 in hike"

    st.success( " output ==> " +c)
    
