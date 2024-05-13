import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

def plot_geospatial_distribution(data, lat_column, lon_column, hover_name_column, hover_data_columns):
    fig = px.scatter_mapbox(data, 
                            lat=lat_column, 
                            lon=lon_column,
                            hover_name=hover_name_column,
                            hover_data=hover_data_columns,
                            zoom=3)

    # Customize the map layout
    fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=5, mapbox_center={"lat": 20, "lon": 78})

    return fig

def plot_temporal_trends(data, datetime_column, y_column, title):
    fig = px.line(data, x=datetime_column, y=y_column, title=title)
    return fig

def plot_top_districts(data, district_column, title, top_n=5):
    # Count FIRs per district
    district_counts = data[district_column].value_counts().nlargest(top_n).reset_index()
    district_counts.columns = [district_column, 'count']

    fig = px.bar(district_counts, x=district_column, y='count', title=title,
                 labels={district_column: 'District', 'count': 'FIR Count'})
    return fig

def plot_secret_firs_distribution(data, secret_column, title):
    # Count secret and non-secret FIRs
    secret_counts = data[secret_column].value_counts().reset_index()
    secret_counts.columns = [secret_column, 'count']

    # Create a bar chart or pie chart
    if len(secret_counts) > 1:  # Bar chart for multiple categories
        fig = px.bar(secret_counts, x=secret_column, y='count', title=title,
                     labels={secret_column: 'Secret FIR', 'count': 'FIR Count'})
    else:  # Pie chart for binary categories
        fig = px.pie(secret_counts, names=secret_column, values='count', title=title,
                     labels={secret_column: 'Secret FIR', 'count': 'FIR Count'})

    return fig

def plot_fir_status_distribution(data, status_column, title):
    # Count FIR statuses
    status_counts = data[status_column].value_counts().reset_index()
    status_counts.columns = [status_column, 'count']

    # Create a bar chart or pie chart
    if len(status_counts) == 2:  # Bar chart for multiple categories
        fig = px.bar(status_counts, x=status_column, y='count', title=title,
                     labels={status_column: 'FIR Status', 'count': 'FIR Count'})
    else:  # Pie chart for binary categories
        fig = px.pie(status_counts, names=status_column, values='count', title=title,
                     labels={status_column: 'FIR Status', 'count': 'FIR Count'})

    return fig

def plot_relationship_heatmap(data, state_column, date_column,title):
    # Create a pivot table for the relationship between FIR status and action taken
    data[date_column] = pd.to_datetime(data[date_column], format='%Y-%m-%d %H:%M:%S')
    pivot = data.pivot_table(values=state_column, 
                       index=data[date_column].dt.day_name(), 
                       columns=data[date_column].dt.hour, 
                       aggfunc=np.sum)

    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot = pivot.reindex(weekday_order)
    fig = px.imshow(pivot,
                    labels=dict(x="Time of Day", y="Day of Week", color="Number of Incidents"),title=title,
                    color_continuous_scale='YlOrRd'
                    # x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                    # y=['Morning', 'Afternoon', 'Evening']
                )
    fig.update_xaxes(side="top")

    return fig
'''
def plot_temporal_histogram(data, datetime_column, y_column, title):
    data[datetime_column] = pd.to_datetime(data[datetime_column], format='%Y-%m-%d %H:%M:%S')

    fig = px.histogram(data, x=datetime_column, y=y_column, title=title, histfunc='sum',
                       labels={datetime_column: 'Date', y_column: 'FIR Count'},
                       category_orders={datetime_column: sorted(data[datetime_column].dt.month.unique())})
    return fig
'''
def plot_temporal_histogram(data, datetime_column, title):
    # Convert 'REG_DT' to datetime format
    data[datetime_column] = pd.to_datetime(data[datetime_column], format='%Y-%m-%d %H:%M:%S')
    df1 = data[datetime_column].dt.date.value_counts().sort_index().reset_index()
    df1.columns = [datetime_column,'Count']
    
    
    # fig = px.histogram(data, x=datetime_column, title=title, histfunc='count',
    #                    labels={datetime_column: 'Time Frame', 'Count': 'Number of FIRs'},
    #                    category_orders={datetime_column: sorted(data[datetime_column].dt.month.unique())})
    fig = px.line(df1, x=datetime_column, y="Count",title=title,labels={datetime_column:'Time Frame','Count':'Count'})

    # fig = px.line(data, x=datetime_column, title=title,labels={datetime_column:'Time Frame',})
    return fig