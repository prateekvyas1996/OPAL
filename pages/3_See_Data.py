from Home import *
data = pd.read_csv('output/data.csv')
st.dataframe(data.head(30),use_container_width=True)