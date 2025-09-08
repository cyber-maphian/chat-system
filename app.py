import streamlit as st
import time
from streamlit_autorefresh import  st_autorefresh
import hashlib

st.set_page_config(
    page_icon="👨‍💻",
    page_title="loonChat",
    initial_sidebar_state="expanded"
)
#disable loader
st.markdown(
    """
    <style>
        #MainMenu {visibility:hidden;}
        footer {visibility:hidden;}
        .block-container{padding-top:0rem;}
        header{visibility:hidden;}
    </style>
    """
,unsafe_allow_html=True)

#set session
if 'val' not in st.session_state:
    st.session_state.val = None

st.header(":red[2Chat]")
#tabs
chat,login = st.tabs(['chat','Login'])

with chat:
    #auto refresh the page
    st_autorefresh(interval=1000,key="refresh_chat")
    if st.session_state.val == True:
                      
        st.write(':red[All Conversation.]')
        #view message
        with st.container(border=10):
            open_allmsg = open('data/allmsg.txt')
            st.write(open_allmsg.read())
            
        #logout and clear buttons
        with st.expander("Actions"):
            col1,col2 = st.columns(2)
            with col2:
                if st.button('Logout',icon="🔃"):
                    st.session_state.val = None
            with col1:
                clear_ = st.button("clear all msg",key="clear_all_msg",icon="🧹")
                if clear_:
                    clear_ = open('data/allmsg.txt','w')
                    clear_.write('')
                    clear_.close()
        
        #send message
        with st.container(border=True):
            id = st.radio("who are you",options=['hassana','sunday'])
            msg = st.chat_input('say hi')
            #read/write user online or offline
            if id == "sunday":
                #THIS USER IS ONLINE
                id1online = open('data/user1online.txt','w')
                id1online.write(f":green[{id} is online.]")
                id1online.close()

                #check if the other user is online
                user2online = open('data/user2online.txt','r')
                st.write(user2online.read())
                #user2online.close()
            elif id == "hassana":
                #THIS USER IS ONLINE
                id2online = open('data/user2online.txt','w')
                id2online.write(f":green[{id} is online.]")
                id2online.close()
                #check if the other user is online
                user2online = open('data/user1online.txt','r')
                st.write(user2online.read())
                #user2online.close()
            else:
                st.error("invalid user",icon="😡")
            #send a message
            if msg:
                if id == 'sunday':
                    #send to user2
                    user1_send_to_user2 = open('data/user2.txt','w')
                    user1_send_to_user2.write(f'{id}: {msg}')
                    user1_send_to_user2.close()

                    #write to al message
                    allmsg = open('data/allmsg.txt','a')
                    allmsg.write(f'  :red[[{id}: {msg}]]  ')
                    allmsg.write('\n')
                    allmsg.close()
                    #write my message
                    with st.chat_message('human',avatar='👦🏼'):
                        st.write(f'you: {msg}')
                    #read my message
                    with st.chat_message('assistant',avatar='👩🏼'):
                        reader = open('data/user1.txt','r')
                        st.write(reader.read())
                    

                elif id == 'hassana':
                    #send to user2
                    user2_send_to_user1 = open('data/user1.txt','w')
                    user2_send_to_user1.write(f'{id}: {msg}')
                    user2_send_to_user1.close()

                    #write to al message
                    allmsg = open('data/allmsg.txt','a')
                    allmsg.write(f'  :green[[{id}: {msg}]]  ')
                    allmsg.write('\n')
                    allmsg.close()

                    #write my message
                    with st.chat_message('human',avatar='👩🏼'):
                        st.write(f'you: {msg}')
                    #read my message
                    with st.chat_message('assistant',avatar='👦🏼'):
                        reader = open('data/user2.txt','r')
                        st.write(reader.read())

            elif id == 'sunday':
                #read my message
                    with st.chat_message('assistant',avatar='👩🏼'):
                        reader = open('data/user1.txt','r')
                        st.write(reader.read())

            elif id == 'hassana':
                #read my message
                    with st.chat_message('assistant',avatar='👦🏼'):
                        reader = open('data/user2.txt','r')
                        st.write(reader.read())
    else:
        #user 1 offline
        user1offline = open("data/user1online.txt",'w')
        user1offline.write(':red[The other user is offline.]')
        user1offline.close()
        #user 2 offline
        user2offline = open("data/user2online.txt",'w')
        user2offline.write(':red[The other user is offline.]')
        user2offline.close()
        st.error("You are not loged in.",icon="😡")

with login:
    st.write("Login")
    with st.form("login"):
        code = st.text_input("Passcode ",type="password").lower()
        hash = hashlib.sha256(code.encode()).hexdigest()
        if st.form_submit_button("Login"):
            if hash == "e233f4339a124c65f9d36b97010644c7e1037c93b3e34d254d179a069eb0dac2":
                st.success("Your Login Was Successful.",icon="😀")
                st.session_state.val = True
            else:
                st.error("your login attempt failed.",icon="😡")
