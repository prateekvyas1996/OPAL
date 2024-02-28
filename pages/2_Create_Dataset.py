from Home import *

# Read existing data from CSV
data = pd.read_csv('output/data.csv')

# Collect user inputs
link = st.text_input("Enter the link of the News article")
question = st.text_input("Paste the Question Here")
topic = st.selectbox(
    "Select the Topic of the Question",
    ('Science and Technology', 'History', 'Geography', 'Polity', 'Economy')
)
notes = st.text_input("Paste the Notes Here")

# Check if the "Add to CSV" button is clicked
if st.button("Add to CSV"):
    # Create new Series with user inputs
    new_row = pd.Series({
        'link': link,
        'question': question,
        'topic': topic,
        'notes': notes
    })

    # Append the new row to the existing DataFrame
    data = data.append(new_row, ignore_index=True)
    st.write("Data added successfully!")

    # Save the updated DataFrame back to CSV
    data.to_csv('output/data.csv', index=False)