import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center"> Health Insurance Cost Prediction using ML</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    model = joblib.load('model_joblib_gr')

    # Display region information
    # st.markdown("""
    # **Region Mapping:**
    # - Southwest
    # - Southeast
    # - Northwest
    # - Northeast
    # """)

    # Input fields
    p1 = st.slider('Enter Your Age', 18, 100)

    s1 = st.selectbox('Sex', ('Male', 'Female'))
    p2 = 1 if s1 == 'Male' else 0  

    p3 = st.number_input("Enter Your BMI Value")

    p4 = st.slider("Enter Number of Children", 0, 5)

    p5 = st.selectbox("Smoker", ("Yes", "No"))
    p5 = 1 if p5 == 'Yes' else 0  

    region_dict = {"Southwest": 1, "Southeast": 2, "Northwest": 3, "Northeast": 4}
    region_selected = st.selectbox("Select Your Region", list(region_dict.keys()))
    p6 = region_dict[region_selected]

    # Prediction
    if st.button('Predict'):
        pred = model.predict([[p1, p2, p3, p4, p5, p6]])
        st.success('Your Insurance Cost is {:.2f}'.format(pred[0]))
        st.balloons()

if __name__ == "__main__":
    main()
