import streamlit as st
from  db import create_table
from  db import addpost,view_records,get_author,get_title,delete_data
from PIL import Image
import base64
import pandas as pd
import matplotlib.pyplot as plt
template_html="""
<div style="background-color:#005555;padding:10px,margin:10px;">
<h4 style="color:white;text-align:center;">{}</h4>
<h3 style="color:white;text-align:center;">{}</h3>
<h2 style="color:white;text-align:center;">{}</h2>
<h2 style="color:white;text-align:center;">{}</h2>
<img src="data:image/jpg;base64,{}" alt="Image" 
style='horizontal-align:center' width="200px" height="200px">
<\div>
"""
st.title("blog database management system")
ch=st.sidebar.selectbox("Select menu",["Home","Add post","Search","Manage blog"])
create_table()
if ch=="Home":
    st.subheader("Home")
    d1=view_records()
    #st.write(d1)
    for i in d1:
        title=i[0]
        author=i[1]
        article=i[2]
        date=i[3]
        image="%s.jpg" %author
        file=open(image,"rb")
        content=file.read()
        im=base64.b64encode(content).decode("utf-8")
        file.close()
        st.markdown(template_html.format(title,author,article,date,im),unsafe_allow_html=True)

elif ch=="Add post":
    st.subheader("Add post")
    t=st.text_input("Title")
    aut=st.text_input("Author")
    art=st.text_area("Article")
    da=st.date_input("Post date")
    
    try:
        im_1=st.file_uploader("upload an image",
                                type=["png","jpg","jpeg"])
        image=Image.open(im_1)
        image=image.convert("RGB")       
        img="{}.jpg".format(aut)
        image.save(img)
        file=open(img,"rb").read()
        im=base64.b64encode(file)
    except:
        print("couldnt open image")
        
    if st.button("Add Post"):
        addpost(t,aut,art,da,im)
        st.success(f"{im} blog successful")
  
elif ch=="Search":
    st.subheader("Search")
    search=st.text_input("Enter the search term")
    r=st.radio("Enter the choice",("Title","Author"))
    if r=="Title":
        result_t=get_title(search)
        #st.write(result_t)
        for i in result_t:
            title=i[0]
            author=i[1]
            article=i[2]
            date=i[3]
            image="%s.jpg" %author
            file=open(image,"rb")
            content=file.read()
            im=base64.b64encode(content).decode("utf-8")
            file.close()
            st.markdown(template_html.format(title,author,article,date,im),unsafe_allow_html=True)

    if r=="Author":
        result_A=get_author(search)
        #st.write(result_A) 
        for i in result_A:
            title=i[0]
            author=i[1]
            article=i[2]
            date=i[3]
            image="%s.jpg" %author
            file=open(image,"rb")
            content=file.read()
            im=base64.b64encode(content).decode("utf-8")
            file.close()
            st.markdown(template_html.format(title,author,article,date,im),unsafe_allow_html=True)

elif ch=="Manage blog":
    st.subheader("Manage blog")
    dv=view_records()
    df=pd.DataFrame(dv,columns=["title","author","article","date","images"])
    df2=df.drop(["images"],axis=1)
    st.dataframe(df2)
    author_list=[i[1] for i in dv]
    blo=st.selectbox("Author name",author_list)
    #=st.text_input("Enter the author name for delete")
    if st.button("delete"):  
        delete_data(blo)
    u=view_records()
    df=pd.DataFrame(u,columns=["title","author","article","date","images"])
    df1=df.drop(["images"],axis=1)
    st.dataframe(df1)
    st.subheader("GRAPHICLE REPRESENTATION")
    title_count=df["title"].value_counts()
    st.write(title_count)
    a=title_count.plot(kind="bar")
    st.pyplot()
    
        

    