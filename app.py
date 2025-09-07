import streamlit as st

st.set_page_config(
    page_icon="👨‍💻",
    page_title="loonChat",
    initial_sidebar_state="expanded"
)

st.header("Welcome To :red[LoonChat]")

#set session for user1
if 'user1' not in st.session_state:
    st.session_state.user1 = ''

#set session for user1
if 'user2' not in st.session_state:
    st.session_state.user2 = ''

#tabs
allmsg,chat = st.tabs(['All Message','chat'])

with allmsg:
    st.write('here you can see all conversation.')
    with st.container(border=10):
        open_allmsg = open('data/allmsg.txt')
        st.write(open_allmsg.read())

    st.button('New MSG.',icon="🔃")

with chat:
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
    
    st.button('New MSG.',icon="🔃",key="refresh2")
