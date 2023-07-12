import streamlit as st
import speech_recognition as sr
import time
from threading import Thread

def start_clicked():
    st.button('Stop')
    while True:
        print('-----------------------Started recording-----------------------')
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
                audio = r.listen(source)
                said = ""
                try:
                    said = r.recognize_google(audio)
                    print(said)
                except Exception as e:
                    print("Exception: " + str(e))

        print('-----------------------Stopped recording-----------------------\n\n')
    
def init():
    st.set_page_config(
    page_title='Voice ChatBot!',
    page_icon=':robot_face:',
    layout='wide',
    initial_sidebar_state='expanded'
    )
    st.title('Voice ChatBot')
    st.sidebar.subheader("About App")
    st.sidebar.info("This web app is to search similar queries for the given query")
    st.sidebar.info("Enter the required fields and click on the 'Search' button to check the same")
    st.sidebar.info("Don't forget to rate this app")
    html_temp = """
        <div id=1 style ="background-color:orange;padding:10px">
        <h1 style ="color:blue;text-align:center;">Voice ChatBot</h1>
        </div>
        <style>
        body {
        background-image: url("https://static.vecteezy.com/system/resources/thumbnails/001/874/132/small/abstract-geometric-white-background-free-vector.jpg");
        background-size: cover;
        }
        </style>
        """
    html1 = """<h2 style ="color:red;text-align:right;"> - Expert</h2> """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.markdown(html1, unsafe_allow_html = True)

def main():
    init()

    st.session_state["thread"] = True
    myThread = Thread(target=start_clicked)

    btn = st.button('Start')

    if btn:
         myThread.start()

main()