import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import dash
from plotly import *
import plotly.graph_objects as go


df_stocks = px.data.stocks()

# fig = go.Figure()
#
# fig.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AAPL,
#                          mode='lines', name='Apple'
#                         ))
# fig.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AMZN,
#                          mode='lines+markers', name='Amazon'
# ))
#
# fig.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.GOOG,
#                          mode='lines+markers', name='Google',
#                          line=dict(
#                              width=2,
#                              color='firebrick',
#                              dash='dashdot'
#                          )
# ))
#
# fig.update_layout(title='Stock Price Data 2018-2020',
#                   xaxis=dict(
#                       showline=True,
#                       showgrid=False,
#                       showticklabels=True,
#                       linecolor='rgb(204,204,204)',
#                       linewidth=2, ticks='outside',
#                       tickfont=dict(
#                           family='Arial', size=12, color='rgb(82,82,82)'
#                       )
#                   ),
#                   yaxis=dict(
#                       showgrid=False,
#                       zeroline=False,
#                       showline=False,
#                       showticklabels=False
#                   ),
#                   autosize=False,
#                   margin=dict(
#                       autoexpand=False,
#                       l=100,
#                       r=20,
#                       t=110
#                   ),
#                   showlegend=False,
#                   plot_bgcolor='white'
#
#                 )
#
# fig.show()
# Bar Chart

# df_us = px.data.gapminder().query("country == 'United States'")
# fig = px.bar(df_us, x='year', y='pop')
# fig.show()

# df_tips = px.data.tips()
# fig = px.bar(df_tips, x='day', y='tip', color='sex',
#              title='Tips by Sex on Each Day',
#              labels={
#                  'tip':'Tip Amount',
#                  'day':'Day of the week'
#              }
#              )
# fig.show()

# df_tips = px.data.tips()
# fig = px.bar(df_tips, x='sex', y='total_bill', color='smoker',
#              barmode='group')
# fig.show()
#
# df_europe = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
# fig = px.bar(df_europe, y='pop', x='country', text='pop', color='country')
# fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
# fig.update_layout(uniformtext_minsize=8,
#                   xaxis_tickangle=-45
#                   )
# fig.show()
#
#
# # Scatter Plots
# df_iris = px.data.iris()
# fig = px.scatter(df_iris, x='sepal_width', y='sepal_length',
#                  color='species', size='petal_length',
#                  hover_data=['petal_width']
#                  )
# fig.show()

df_iris = px.data.iris()
fig=go.Figure()
fig.add_trace(go.Scatter(
    x=df_iris.sepal_width,
    y=df_iris.sepal_length,
    mode='markers',
    marker_color=df_iris.sepal_width,
    text=df_iris.species,
    marker=dict(
        showscale=True
    )
))
fig.update_traces(marker_line_width=2, marker_size=10)



fig = go.Figure(data=go.Scattergl(
    x=np.random.randn(100000),
    y=np.random.randn(100000),
    mode='markers',
    marker=dict(
        color=np.random.randn(100000),
        colorscale='Viridis',
        line_width=1
    )

))



# Pie chart

df_asia=px.data.gapminder().query("year==2007").query("continent=='Asia'")
fig = px.pie(df_asia, values='pop', names='country',
       title='Population of Asian Continent',
       color_discrete_sequence=px.colors.sequential.RdBu
       )

colors=['blue', 'green', 'black', 'purple', 'red', 'brown']
fig = go.Figure(data=[go.Pie(labels=['Water', 'Grass', 'Normal', 'Psychic', 'Fire', 'Ground'], values=[110,90,80,80,70,60])])
fig.update_traces(hoverinfo='label+percent', textfont_size=20, textinfo='label+percent',
                  pull=[0.1, 0, 0.2, 0, 0, 0],
                  marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2))
                  )

# Histogram
dice_1 = np.random.randint(1,7,5000)
dice_2 = np.random.randint(1,7,5000)

dice_sum = dice_1 + dice_2
print(dice_sum)
fig  = px.histogram(dice_sum, nbins=11,
                    labels='5000 Dice Roll Histogram',
                    marginal='violin',
                    color_discrete_sequence=['green']
                    )
fig.update_layout(
    xaxis_title_text='Dice Roll',
    yaxis_title_text='Dice Sum',
    bargap=0.2, showlegend=False)


df_tips = px.data.tips()
fig = px.histogram(df_tips, x='total_bill', color='sex')


fig = px.box(df_tips, x='sex', y='tip', points='all')

fig = px.box(df_tips, x='day', y='tip',color='sex')
fig.show()
