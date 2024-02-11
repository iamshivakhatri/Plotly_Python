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
#
# df_iris = px.data.iris()
# fig=go.Figure()
# fig.add_trace(go.Scatter(
#     x=df_iris.sepal_width,
#     y=df_iris.sepal_length,
#     mode='markers',
#     marker_color=df_iris.sepal_width,
#     text=df_iris.species,
#     marker=dict(
#         showscale=True
#     )
# ))
# fig.update_traces(marker_line_width=2, marker_size=10)
#
#
#
# fig = go.Figure(data=go.Scattergl(
#     x=np.random.randn(100000),
#     y=np.random.randn(100000),
#     mode='markers',
#     marker=dict(
#         color=np.random.randn(100000),
#         colorscale='Viridis',
#         line_width=1
#     )
#
# ))
#
#
#
# # Pie chart
#
# df_asia=px.data.gapminder().query("year==2007").query("continent=='Asia'")
# fig = px.pie(df_asia, values='pop', names='country',
#        title='Population of Asian Continent',
#        color_discrete_sequence=px.colors.sequential.RdBu
#        )
#
# colors=['blue', 'green', 'black', 'purple', 'red', 'brown']
# fig = go.Figure(data=[go.Pie(labels=['Water', 'Grass', 'Normal', 'Psychic', 'Fire', 'Ground'], values=[110,90,80,80,70,60])])
# fig.update_traces(hoverinfo='label+percent', textfont_size=20, textinfo='label+percent',
#                   pull=[0.1, 0, 0.2, 0, 0, 0],
#                   marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2))
#                   )
#
# # Histogram
# dice_1 = np.random.randint(1,7,5000)
# dice_2 = np.random.randint(1,7,5000)
#
# dice_sum = dice_1 + dice_2
# print(dice_sum)
# fig  = px.histogram(dice_sum, nbins=11,
#                     labels='5000 Dice Roll Histogram',
#                     marginal='violin',
#                     color_discrete_sequence=['green']
#                     )
# fig.update_layout(
#     xaxis_title_text='Dice Roll',
#     yaxis_title_text='Dice Sum',
#     bargap=0.2, showlegend=False)
#
#
# df_tips = px.data.tips()
# fig = px.histogram(df_tips, x='total_bill', color='sex')

#
# fig = px.box(df_tips, x='sex', y='tip', points='all')
#
# fig = px.box(df_tips, x='day', y='tip',color='sex')
# fig.show()


# df_tips = px.data.tips()
# fig = go.Figure()
# fig.add_trace(go.Box(x=df_tips.sex, y=df_tips.tip, marker_color='blue',
#                      boxmean='sd'))
# fig.show()

# Violin Plots

#df_tips = px.data.tips()
# fig = px.violin(df_tips, y="total_bill", box=True, points='all')
# fig = px.violin(df_tips, y="tip", x="smoker", color="sex", box=True,
#                 points="all", hover_data=df_tips.columns
#                 )

# fig = go.Figure()
#
# fig.add_trace(go.Violin(x=df_tips['day'][df_tips['smoker'] == 'Yes'],
#                         y=df_tips['total_bill'][df_tips['smoker'] == 'Yes'],
#                         legendgroup='Yes', scalegroup='Yes', name='Yes',
#                         side='negative', line_color='blue'
#
#                         ))
# fig.add_trace(go.Violin(x=df_tips['day'][df_tips['smoker'] == 'No'],
#                         y=df_tips['total_bill'][df_tips['smoker'] == 'No'],
#                         legendgroup='Yes', scalegroup='Yes', name='No',
#                         side='positive', line_color='red'
#
#                         ))

# fig.show()

# # Density Heatmaps
# flights = sns.load_dataset("flights")
#
# fig = px.density_heatmap(flights, x='year',y='month', z='passengers', color_continuous_scale='Viridis')
# fig.show()

# 3D Scatter Plots
#
# fig = px.scatter_3d(flights, x='year', y='month', z='passengers', color='year', opacity=0.7)
#
# fig.show()

# Line Plots

# fig = px.line_3d(flights, x='year', y='month', z='passengers', color='year')
#
# fig.show()

# Scatter Matrix
# flights = sns.load_dataset("flights")
# fig = px.scatter_matrix(flights, color ='month')
# fig.show()

# Map Scatter Plots

# df = px.data.gapminder().query("year == 2007")
# fig = px.scatter_geo(df, locations="iso_alpha",
#                      color="continent",
#                      hover_name="country",
#                      size="pop",
#                      projection="orthographic"
#                      )
# fig.show()

# Choropleth Maps

# # Polar Charts
# df_wind = px.data.wind()
# fig = px.scatter_polar(
#     df_wind, r='frequency', theta="direction", color="strength", size="frequency", symbol="strength"
# )
# fig.show()
#
# # Ternary Plots
#
# df_exp = px.data.experiment()
# fig = px.scatter_ternary(df_exp, a="experiment_1", b="experiment_2",c="experiment_3", hover_name="group", color="gender")
#
# fig.show()

# Facet Plots

# df_tips = px.data.tips()
# fig = px.scatter(df_tips, x="total_bill", y="tip", color="smoker", facet_col="sex")
# fig.show()
# Animation for scatterplot
# df_cont = px.data.gapminder()
# fig = px.scatter(df_cont, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#                  size="pop", color="continent", hover_name='country',
#                  log_x=True, size_max=55, range_x=[100,100000],
#                  range_y=[25,90]
#                  )
# fig.show()

# fig = px.bar(df_cont, x='continent', y='pop', color='continent',
#              animation_frame='year', animation_group='continent',
#              range_y=[0,4000000000]
#              )
#
# fig.show()