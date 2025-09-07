import streamlit as st
import time

st.set_page_config(
    page_icon="👨‍💻",
    page_title="loonChat",
    initial_sidebar_state="expanded"
)

st.header("Welcome To :red[2Chat]")
#tabs
chat, = st.tabs(['chat',])

with chat:
    
    #send message
    with st.container(border=10):
         id = st.radio("who are you",options=['hassana','sunday'])
         msg = st.chat_input('say hi')

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
        
    st.write(':red[All Conversation.]')
    #view message
    with st.container(border=10):
        open_allmsg = open('data/allmsg.txt')
        st.write(open_allmsg.read())
        
    #new msg and clear buttons
    col1,col2 = st.columns(2)
    with col1:
        st.button('New MSG.',icon="🔃")
    with col2:
        clear_ = st.button("clear all msg",key="clear_all_msg",icon="🧹")
        if clear_:
            clear_ = open('data/allmsg.txt','w')
            clear_.write('')
            clear_.close()

