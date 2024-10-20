# Use Streamlit to upload excel file
import tempfile
from datetime import datetime

import streamlit as st
import pandas as pd


def df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8-sig')


def main():
    st.set_page_config(
        page_title='Excel Tool',
        page_icon='kt.ico'  # http is fine too
    )

    # Hide the streamlit style with CSS
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    st.title("Excel Merger")

    upload_files = st.file_uploader("Upload files", type=["xlsx", "xls"], accept_multiple_files=True)

    # Add a button to trigger the calculation
    if st.button("Merge"):
        # Merge the uploaded files
        df_result = pd.DataFrame()
        for file in upload_files:
            df = pd.read_excel(file)
            df_result = pd.concat([df_result, df], join='outer', axis=0, ignore_index=True)
        st.write(df_result)
        output = df_to_csv(df_result)
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Add a button to download the result
        st.download_button(
            label='Download data',
            data=output,
            file_name=f'Result_ {current_time}.csv',
            # mime='application/vnd.ms-excel'
            mime='text/csv'
        )


if __name__ == "__main__":
    main()
