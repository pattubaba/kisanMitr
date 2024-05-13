import streamlit as st
# from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_option_menu import option_menu
from PIL import Image
from bot_utils.csv_agent import dashboard
import MySQLdb
import base64

st.set_page_config(page_title="Gen-AI License Tracking System",page_icon=":bar_chart:",layout="wide")

if not hasattr(st.session_state,"initialized"):
    st.session_state.initialized = False

def session_init():
    if not hasattr(st.session_state,"data_render"):
        st.session_state.data_render = False
    if not hasattr(st.session_state,"ask_agent"):
        st.session_state.ask_agent = False

session_init()

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_file = r".assets\bg4.jpeg"
with open(image_file, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
st.markdown(f"""
        <style>
            body {{
                background-image: URL("https://i.ibb.co/CBcw0zc/india.jpg");
                background-size: cover;
                }}   
            .block-container {{
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 2.5rem;
                    padding-right: 2.5rem;
                }}
            .stApp {{
                background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
                background-size: cover
                 }} 
            
            .css-uc1cuc {{
                position: fixed;
                top: 0px;
                left: 0px;
                right: 0px;
                height: 2.875rem;
                background: #fdfef0;
                outline: none;
                z-index: 999990;
                display: block;
                }}

        
            .stPlotlyChart {{
            box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
            }}
            
            .div.css-10qvep2.e1f1d6gn1 {{
             height=10px !important;
            }}
        </style>
        """, unsafe_allow_html=True)


st.markdown("""
        <style>
            .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 2.5rem;
                    padding-right: 2.5rem;
                } 
            
            .div.css-10qvep2.e1f1d6gn1 {
             height=10px !important;
            }
        </style>
        """, unsafe_allow_html=True)

# for logo and header
with st.container():
    col1,col2=st.columns([0.10,0.90],gap="large")
    with col1:
        logo_image = Image.open(r".assets\Agrilogo.jpeg")
        resized_logo = logo_image.resize((100, 100))
        # Get the dimensions of the logo image
        logo_width, logo_height = resized_logo.size
        logo= st.image(resized_logo, use_column_width=False, output_format="auto", width=logo_width) 
    with col2:

        # add_vertical_space(1)
        st.title("AI base License Tracking System for Officials")
        st.markdown(" :blue[  **Gen-AI System** for **License Tracking** of **Different** **Applicaiton of **, Seeds, Fertilizer and Pesticides] ")
        # st.divider()

with st.container():
    selected_nav= option_menu(
            menu_title=None,
            options=["AI-Smart Search Engine"],
            icons = ["file-earmark-text"],
            menu_icon="cast",   
            default_index=0,
            orientation="horizontal",
            styles={"container": {"padding": "0.5!important" ,"width":"100% !important"}}
            # styles={
            #             "container": {"padding": "2!important", "background-color": "#fafafa"},
            #             "icon": {"color": "orange", "font-size": "25px"},
            #             "nav-link": {
            #                 "font-size": "20px",
            #                 "text-align": "left",
            #                 "margin": "1px",
            #                 "--hover-color": "#eee",
            #             },
            #             # "nav-link-selected": {"background-color": "green"},
            #         },
            
                )

    if selected_nav == "AI-Smart Search Engine":
        dashboard()
    if selected_nav == "":
        pass

