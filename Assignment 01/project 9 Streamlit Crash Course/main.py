import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# check=st.checkbox("you have all the things")
# if check:
#     st.write("Thanks")

# name=st.text_input("PLease enter your name")
# age =st.slider("Select your age",0,100)
# if st.button("Submit"):
#     st.write("Name: ", name)
#     st.write("Age: ", age)
#     st.write("Thanks for submitting")


                                                                        
# search a particular city

# number= st.number_input("enter the number to display in yellow",value=80)

# city = st.selectbox("Choose a city to filter", df["City"].unique())
# filtered_data = df[df["City"] == city]

# st.write(f"Data for city: {city}")
# st.dataframe(filtered_data)

# style_df=df.style.applymap(lambda x: "background-color: yellow" if isinstance(x,int) and x>number else "")
# st.dataframe(style_df)


# data visualization through


# data =pd.DataFrame({
#     "fruits":["Apple","Banana","Orange","Pineapple"],
#     "prices":[23,43,56,87]
# })
# fig=px.bar(data,x="fruits",y="prices",title="fruit prices chart")
# st.plotly_chart(fig)

# data = pd.DataFrame(
#     np.random.randn(100, 3),
#     columns = ["A", "B", "C"]
# )

# plt.figure(figsize=(10, 6))
# sns.scatterplot(x = data["A"], y = data["B"])
# plt.title("Scatter plot of A and B")

# st.pyplot(plt)



# with st.expander("see more detail"):
#     st.write("Line Chart")
#     st.line_chart([1,2,3,4,5])


st.sidebar.title("Navigation")

opt= st.sidebar.selectbox("Choose a page: ",["Home","About", "Contact"])
if opt == "Home":
    st.write("This is home page")
elif opt == "About":
    st.write("This is about page")
elif opt == "contact":
    st.write("This is contact page")