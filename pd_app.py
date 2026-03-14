import streamlit as st
from pypdf import PdfReader
from pypdf import PdfWriter

st.title("Pdf editor")

def display(x):
    if x is not None:
     st.info("your file named "+ x +" has been created", icon="ℹ️")
     
#mergering files
def merge():
    #uploading file
    st.header("Merger files")
    upload_file =st.file_uploader("select your pdf files in order of merger", type=["pdf"], accept_multiple_files=True)
        
    if upload_file is not None:
        for uploadf in upload_file:
            st.write("filename:",uploadf.name)
    j=0        
    pdfm=PdfWriter()
    for pdf in upload_file:
        pdfm.append(pdf)
        j=j+1
        
    with st.form("name_form"):
        merged_name=st.text_input("Enter name of the merged pdf", max_chars=30)
        pdfm.write(merged_name+".pdf")
        submit=st.form_submit_button("Enter")
        
    if submit and j>1:
        display(merged_name)
    
    if submit and j<1:
        st.warning("Select the files to merge first, files not merged.")
    
    
        
    


#extract text
def extracxt():
        st.header("Extract text")
        upload_file=st.file_uploader("select the file to extract text from", type=["pdf"])
        if upload_file is not None:
           reader=PdfReader(upload_file.name)
           length= len(reader.pages)
           st.write("Number of pages= ",length)
           try:
            f=open(upload_file.name+"context.txt","x" ,encoding='utf-8')
    
            for l in range(length):
             page=reader.pages[l]
             ex_txt=page.extract_text()
             
             
             
             st.code(ex_txt) #prints text in a code box!
             f.write(ex_txt)
        
            st.write(upload_file.name)
            f.close
           except:
             st.write("file named "+upload_file.name+"context.txt has already been extracted")
        
    


def main():
    merge()
    extracxt()
    
main()
