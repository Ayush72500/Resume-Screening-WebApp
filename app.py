"""
app.py

Ultra-minimal Streamlit UI for Resume Screening & Role Classification.
Triggers analysis ONLY when the "Analyze Resume" button is clicked and automatically cleans up temporary files.
"""

import streamlit as st
import roles
import extractor
import analyzer
import utils


# --- PAGE CONFIGURATION & HIDE STREAMLIT DEPLOY HEADER ---
st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="centered"
)

# Hide Streamlit top header bar, deploy button, main menu, and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    </style>
""", unsafe_allow_html=True)


def main():
    st.title("Resume Screening System")
    st.markdown("Upload a PDF resume to identify the target job role.")
    st.divider()

    all_roles = roles.get_roles()

    uploaded_file = st.file_uploader(
        "Upload your PDF resume",
        type=["pdf"]
    )

    analyze_clicked = st.button("Analyze Resume", type="primary")

    if analyze_clicked:
        if uploaded_file is None:
            st.warning("Please upload a PDF resume first.")
            return

        temp_path = None
        extracted_text = ""

        try:
            # Save temporary file
            temp_path = utils.save_uploaded_file(uploaded_file)

            with st.spinner("Extracting text from PDF..."):
                extracted_text = extractor.extract_text_from_pdf(temp_path)
        finally:
            # Delete temporary file immediately after text extraction
            if temp_path:
                utils.remove_file(temp_path)

        if not extracted_text or len(extracted_text.strip()) == 0:
            st.error("We could not extract readable text from this PDF. Please try another resume.")
            return

        primary_role = analyzer.analyze_resume(extracted_text, all_roles)

        st.success("Analysis Complete!")
        st.subheader("Target Job Role")
        st.info(f"🎯 **{primary_role}**")


if __name__ == "__main__":
    main()
