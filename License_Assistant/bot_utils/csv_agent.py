from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import os
import random
from bot_utils.graphs_functions import plot_temporal_trends
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import plotly.express as px
from bot_utils.prompts import prompt
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine, text
# from test import ask_dataframe
# from chatbot_utils.test import ask_dataframe


load_dotenv()
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-12-01-preview"
os.environ["OPENAI_API_BASE"] = "https://ey-sandbox.openai.azure.com/"
os.environ["OPENAI_API_KEY"] = "4b81012d55fb416c9e398f6149c3071e"

# os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
# os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
# os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def get_sql_agent(uri):
    azure_llm = AzureChatOpenAI(deployment_name = "gpt-4",temperature=0)
    db = SQLDatabase.from_uri(uri)
    toolkit = SQLDatabaseToolkit(db=db, llm=azure_llm)
    agent_executor = create_sql_agent(
    llm=azure_llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    agent_executor_kwargs={"handle_parsing_errors": True}
    )
    return agent_executor

def get_csv_agent(csv_path,deployment_name):
    print("Agent is setting up...")
    llm = AzureChatOpenAI(deployment_name=deployment_name,model_name=deployment_name,temperature=0)
    agent = create_csv_agent(
        llm,
        csv_path,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )
    return agent


def remove_commas(value):
    try:
        return str(value).replace(',', '')
    except Exception as e:
        print(f"Error processing value {value}: {e}")
        return value


def dashboard():
    with st.container():
        # ask_dataframe("data_utils\myData.csv")
        
            
        col1,col2 = st.columns([0.5,0.5],gap="small")
        
        with col1:
            
            st.markdown('### Licenses Data')
            if not st.session_state.data_render:
                st.session_state.refined_data = pd.read_csv(r'data_utils\fertilizer.csv')
                # st.session_state.refined_data =data.drop(columns=["REG_YEAR","FIR_SRNO",])
                # columns_to_format =["FIR_REG_NUM", "PS_CD","Shape_Leng", "Shape_Area"]
                # for column in columns_to_format:
                #     st.session_state.refined_data[column] = st.session_state.refined_data[column].astype(str).map(remove_commas)
                #     print('ghua kuch?')
                #     print("type = ",st.session_state.refined_data[column].dtype)
                # st.session_state.refined_data.to_csv(r'data_utils\my_data.csv')
            st.dataframe(st.session_state.refined_data, use_container_width =True)
            st.session_state.data_render = True

        with col2:
            st.markdown('### Track Real time licenses application from here. ')
            user_input = st.text_input("Please type your query here")
            quote = ["Processing fertilizer license data... Because of tracking application for fertilizer license.",
                     "Crunching the data... and reducing the pendency of license is our priority.",
                     "Analyzing fertilizer license applicaiton data... having ,Application id, Process Id, Payment status and application status.",
                     "Loading insights... Together, building a safer community.",
                     "Gathering data... Your patience contributes to our diligence.",
                     "Processing pertinent info... Committed to fairness and justice.",
                     "Raising the application tracking of fertilizer license, loading your data now.",
                     "Working behind the scenes to compile the data... Your vigilance is our strength.",
                     "Processing data for a safer tomorrow... Thank you for patience.",
                     "Translating data into justice... Your wait ensures smoother operations."]

            if not st.session_state.ask_agent:
                # uri = "mysql://root:root%40123@localhost/cctns_dbms"
                print("establishing")
                # agri_uri="mssql+pyodbc://sachendra:Agriculture%40123@IN3132737W1\\SQLEXPRESS/Agriculture?driver=ODBC+Driver+17+for+SQL+Server"
                agri_uri ="mysql://root:admin@localhost/agridb"
                st.session_state.ask_agent = get_sql_agent(agri_uri)
                print("established")

            if user_input:
                with st.spinner(quote[random.randint(0,len(quote)-1)]):
                    st.info(st.session_state.ask_agent.run(prompt.format(user_input)))

    # with st.container():
    #     fig_temporal_trends = plot_temporal_histogram(st.session_state.refined_data, 'REG_DT', 'FIR Registrations Over Time')
    #     st.plotly_chart(fig_temporal_trends,use_container_width=True)
    #     fig_heatmap_trends = plot_relationship_heatmap(st.session_state.refined_data, 'State_LGD', 'REG_DT', 'Heatmap of Incidents')
    #     st.plotly_chart(fig_heatmap_trends,use_container_width=True)

    # st.divider()
    # with st.container():
    #     colu1,colu2 = st.columns([0.5,0.5],gap="large")
    #     with colu1:

    #         # Display district-wise analysis plot in Streamlit
    #         fig_district_wise_analysis = plot_top_districts(st.session_state.refined_data, 'DISTRICT_NAME', 'FIR Count in Each District')
    #         st.plotly_chart(fig_district_wise_analysis,use_container_width=True)
    #     with colu2:

    #         # Display secret FIRs distribution plot in Streamlit
    #         fig_secret_firs_distribution = plot_secret_firs_distribution(st.session_state.refined_data, 'IS_FIR_SECRET', 'Distribution of Secret FIRs')
    #         st.plotly_chart(fig_secret_firs_distribution,use_container_width=True)

    # st.divider()

    # st.map(data=st.session_state.refined_data,latitude='Lat',longitude='Long',zoom=6.5,use_container_width=True)

    # st.divider()

    # distpie = st.session_state.refined_data['DISTRICT_NAME'].value_counts().sort_index().reset_index()
    # distpie.columns = ['DISTRICT','Count']
    # fig = px.pie(distpie, values='Count', names='DISTRICT', title='Crimes by District')
    # st.plotly_chart(fig,use_container_width=True)

    # map_fig = plot_geospatial_distribution(st.session_state.refined_data,"Lat","Long","FIR_REG_NUM","REG_DT")
    # st.plotly_chart(map_fig)
    # with st.container():
    #     col3_1,col3_2 = st.columns([0.5,0.5],gap="large")
    #     with col3_1:
    #         fig_fir_status_distribution = plot_fir_status_distribution(st.session_state.refined_data, 'FIR_STATUS', 'Distribution of FIR Statuses')
    #         st.plotly_chart(fig_fir_status_distribution)

    #     with col3_2:

    #         # Display relationship heatmap in Streamlit
    #         fig_relationship_heatmap = plot_relationship_heatmap(st.session_state.refined_data, 'FIR_STATUS', 'ACTION_TAKEN_CD', 'Relationship Heatmap')
    #         st.plotly_chart(fig_relationship_heatmap)
    # st.divider()
    