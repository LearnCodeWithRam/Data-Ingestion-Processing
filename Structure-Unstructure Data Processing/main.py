import streamlit as st
from image_to_text import extract_text_from_image

# Function to process the uploaded file based on its type
def process_uploaded_file(file_upload, file_type):
    processing_result = ""
    if file_upload is not None:
        processing_result += f"Processing {file_type} file: {file_upload.name}\n"
        # Add code to process the uploaded file here
        if file_type == "Image":
            processing_result=extract_text_from_image(file_upload)
        # You can use 'file_type' to determine the file type and apply specific processing logic
        processing_result += "Processing complete."
    return processing_result

# Sidebar
st.sidebar.title("Structure/Unstructure Data Processing by files")
file_type = st.sidebar.selectbox("Choose a file type", ["Image", "Audio","Video", "PPT", "CSV", "PDF","DOCs"])
file_upload = st.sidebar.file_uploader(f"Upload {file_type} File", type=["jpg", "png", "jpeg", "gif", "wav", "mp3", "pptx", "csv", "pdf","docs"])
submit_button = st.sidebar.button("Submit", key="file_submit")
file_processing_output = st.sidebar.empty()
#file_processing_output = st.sidebar.text_area("Processing Output", key="file_out", value="")
#file_processing_output = st.sidebar.text_area("Processing Output", value="")

if submit_button:
        #file_processing_output.value = "Processing..."
        file_processing_output.text("Processing...")
        with st.spinner("AI is at Work! "):
            result = process_uploaded_file(file_upload, file_type)
            #file_processing_output.value = result
            #file_processing_output.text_area(result)
            #file_processing_output.text(result)
            file_processing_output.markdown(result)
        

# Main content
st.title("Structure/Unstructure Data Processing by URL")
st.write("Enter the URL in the field below.")

# Input field for URL
url = st.text_input("URL")

# Dropdown menu for URL type
url_type = st.selectbox("Choose URL type", ["Video URL", "Web URL"])
url_processing_output = st.text_area("Processing Output", key="url_output", value="")

# Submit button
if st.button("Submit", key="url_submit"):
    url_processing_output.value = "Processing..."
    # Add code to process the URL based on its type
    if url_type == "Video URL":
        url_processing_output.value = f"Processing Video URL: {url}\n"
        # Add video URL processing logic here
        url_processing_output.value += "Processing complete."
    else:
        url_processing_output.value = f"Processing Web URL: {url}\n"
        # Add web URL processing logic here
        url_processing_output.value += "Processing complete."
