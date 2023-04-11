import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objs as go


import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("D:\project 3\MSDhoni.csv")
df1= pd.read_csv("D:\project 3\msdvsteams.csv")
df2=pd.read_csv("D:\project 3\inground.csv")
df3=pd.read_csv("D:\project 3\dk.csv")
df4=pd.read_csv("D:\project 3\dkvsopp.csv")
df5=pd.read_csv("D:\project 3\dkinground.csv")
df6=pd.read_csv("D:\project 3\MSDVSDK.csv")
df7=pd.read_csv("D:\project 3\msposition.csv")
df8=pd.read_csv("D:\project 3\DKposition.csv")
df9=pd.read_csv("D:\project 3\msresult.csv")
df10=pd.read_csv("D:\project 3\dkresult.csv")
#1.msdmatchesvs teams
sns.barplot(x='Matches', y='Teams', data=df1)
plt.xlabel('Matches')
plt.ylabel('Teams')
plt.title('Grouped bar plot of Matches vs Teams')
plt.show()

#2.msdinningssvs teams
df = df.dropna()
sns.barplot(x='Innings', y='Teams', data=df1)
plt.xlabel('Innings')
plt.ylabel('Teams')
plt.title('Grouped bar plot of Innings vs Teams')
plt.show()

#3.msdrunssvs teams
df = df.dropna()
sns.barplot(x='Runs', y='Teams', data=df1)
plt.xlabel('Runs')
plt.ylabel('Teams')
plt.title('Grouped bar plot of Runs vs Teams')
plt.show()

#4.msdstrikeratevs teams
Df_info=df1.copy()

match_df = pd.concat([df1['Strike Rate']]).value_counts().reset_index()
match_df.set_axis(['Strike Rate','Teams'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df1, x='Strike Rate', y='Teams', text='Strike Rate',
             color ='Strike Rate', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Strike Rate per Teams",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#5.msdaveragevs teams
Df_info=df1.copy()
match_df = pd.concat([df1['Average']]).value_counts().reset_index()
match_df.set_axis(['Average','Teams'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df1, x='Average', y='Teams', text='Average',
             color ='Average', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Average per Teams",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#6.msdhighscorevs teams
sns.barplot(x='H.S', y='Teams', data=df1)
plt.xlabel('H.S')
plt.ylabel('Teams')
plt.title('Grouped bar plot of High score vs Teams')
plt.show()

#7.msdmatchin eachgrd
sns.barplot(x='Matches', y='Ground', data=df2)
plt.xlabel('Matches')
plt.ylabel('Ground')
plt.title('Grouped bar plot of Matches vs Ground')
plt.show()

#8.msdaveragevs ground
Df_info=df2.copy()

match_df = pd.concat([df2['Average']]).value_counts().reset_index()
match_df.set_axis(['Average','Ground'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df2, x='Average', y='Ground', text='Average',
             color ='Average', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Average per Ground",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#9.msdstrikeratevs ground
Df_info=df2.copy()

match_df = pd.concat([df2['Strike Rate']]).value_counts().reset_index()
match_df.set_axis(['Strike Rate','Ground'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df2, x='Strike Rate', y='Ground', text='Strike Rate',
             color ='Strike Rate', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Strike Rate per Ground",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
            
#10.msdaveragevsyear
Df_info=df.copy()

match_df = pd.concat([df['Year']]).value_counts().reset_index()
match_df.set_axis(['Year','Average'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df, x='Year', y='Average', text='Average',
             color ='Year', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Average per Year",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()

#11.msdstrikeragevsyear
Df_info=df.copy()

match_df = pd.concat([df['Year']]).value_counts().reset_index()
match_df.set_axis(['Year','Strike Rate'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df3, x='Year', y='Strike Rate', text='Strike Rate',
             color ='Year', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Strike Rate per Year",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#12.msdfiftiesvsyear
Df_info=df.copy()

match_df = pd.concat([df['Fifties']]).value_counts().reset_index()
match_df.set_axis(['Fifties','Year'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df, x='Fifties', y='Year', text='Fifties',
             color ='Fifties', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Fifties per Year",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#####

#1.dkmatchesvs teams
sns.barplot(x='Matches', y='Teams', data=df4)
plt.xlabel('Matches')
plt.ylabel('Teams')
plt.title('Grouped bar plot of Matches vs Teams')
plt.show()

#2.dkinningssvs teams
sns.barplot(x='Innings', y='Teams', data=df4)
plt.xlabel('Innings')
plt.ylabel('Teams')
plt.title('Grouped bar plot of Innings vs Teams')
plt.show()

#3.dkrunssvs teams
df = df.dropna()
sns.barplot(x='Runs', y='Teams', data=df4)
plt.xlabel('Runs')
plt.ylabel('Teams')
plt.title('Grouped bar plot of Runs vs Teams')
plt.show()
#4.dkstrikeratevs teams
Df_info=df4.copy()

match_df = pd.concat([df4['Strike Rate']]).value_counts().reset_index()
match_df.set_axis(['Strike Rate','Teams'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df4, x='Strike Rate', y='Teams', text='Strike Rate',
             color ='Strike Rate', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Strike Rate per Teams",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#5.dkaveragevs teams
Df_info=df4.copy()

match_df = pd.concat([df4['Average']]).value_counts().reset_index()
match_df.set_axis(['Average','Teams'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df4, x='Average', y='Teams', text='Average',
             color ='Average', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Average per Teams",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#6.dkhighscorevs teams
sns.barplot(x='H.S', y='Teams', data=df4)
plt.xlabel('H.S')
plt.ylabel('Teams')
plt.title('Grouped bar plot of High score vs Teams')
plt.show()
#7.dkmatchin eachgrd
sns.barplot(x='Matches', y='Ground', data=df5)
plt.xlabel('Matches')
plt.ylabel('Ground')
plt.title('Grouped bar plot of Matches vs Ground')
plt.show()
#8.dkaveragevs ground
Df_info=df5.copy()

match_df = pd.concat([df5['Average']]).value_counts().reset_index()
match_df.set_axis(['Average','Ground'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df5, x='Average', y='Ground', text='Average',
             color ='Average', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Average per Ground",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#9.dkstrikeratevs ground
Df_info=df5.copy()

match_df = pd.concat([df5['Strike Rate']]).value_counts().reset_index()
match_df.set_axis(['Strike Rate','Ground'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df5, x='Strike Rate', y='Ground', text='Strike Rate',
             color ='Strike Rate', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Strike Rate per Ground",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#10.dkaveragevsyear
Df_info=df3.copy()

match_df = pd.concat([df3['Year']]).value_counts().reset_index()
match_df.set_axis(['Year','Average'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df3, x='Year', y='Average', text='Average',
             color ='Year', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Average per Year",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#11.dkstrikeragevsyear
Df_info=df.copy()

match_df = pd.concat([df3['Year']]).value_counts().reset_index()
match_df.set_axis(['Year','Strike Rate'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df3, x='Year', y='Strike Rate', text='Strike Rate',
             color ='Year', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Strike Rate per Year",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#12.dkfiftiesvsyear
Df_info=df3.copy()

match_df = pd.concat([df3['Fifties']]).value_counts().reset_index()
match_df.set_axis(['Fifties','Year'],axis = 'columns' ,inplace = True)

def get_color(name, number):
    pal = list(sns.color_palette(palette=name, n_colors=number).as_hex())
    return pal

pal_vi = get_color('viridis_r', len(match_df))

fig = px.bar(df3, x='Fifties', y='Year', text='Fifties',
             color ='Fifties', color_discrete_sequence=pal_vi)
fig.update_layout(
    title={
        'text': "Fifties per Year",
        'y':1,
        'x':0.45,
        'xanchor': 'center',
        'yanchor': 'top'})
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout({'plot_bgcolor': 'white',
                   'paper_bgcolor': 'white'})
fig.update_layout(width=1000, height=600,
                  margin = dict(t=15, l=15, r=15, b=15))
fig.show()
#bounariescomparison
#msd
sixes= df['Sixes'].sum()
fours = df['Fours'].sum()
data = go.Pie(labels=['Sixes', 'Fours'], values=[sixes, fours])
layout = go.Layout(title='Percentage of sixes vs fours')
fig = go.Figure(data=[data], layout=layout)
fig.show()

#dk
sixes= df3['Sixes'].sum()
fours = df3['Fours'].sum()
data = go.Pie(labels=['Sixes', 'Fours'], values=[sixes, fours])
layout = go.Layout(title='Percentage of sixes vs fours')
fig = go.Figure(data=[data], layout=layout)
fig.show()

#inninigscomparison

#comparison on average
trace1 = go.Bar(x=df6['Year'], y=df6['MSD Average'], name='DK Average')
trace2 = go.Bar(x=df6['Year'], y=df6['MSD Average'], name='DK Average')
layout = go.Layout(title='Average by Year', xaxis_title='Year', yaxis_title='Average')
fig = go.Figure(data=[trace1,trace2], layout=layout)
fig.show()

#comparison on strikerate
trace1 = go.Bar(x=df6['Year'], y=df6['MSD Strike Rate'], name='DK Strike Rate')
trace2 = go.Bar(x=df6['Year'], y=df6['MSD Strike Rate'], name='DK Strike Rate')
layout = go.Layout(title='Strike Rate by Year', xaxis_title='Year', yaxis_title='Strike Rate')
fig = go.Figure(data=[trace1,trace2], layout=layout)
fig.show()

#comparison on msdgettingout
out_method = ["BOWLED","CAUGHT","CAUGHT and BOWLED","HIT WICKET","STUMPED","LBW"]
out_times = [19,75,16,0,3,5]
fig = go.Figure(data=[go.Pie(labels=out_method, values=out_times)])
fig.update_layout(title="comparison on msdgettingout")
fig.show()
#comparison on dkgettingout
out_method = ["BOWLED","CAUGHT","CAUGHT and BOWLED","HIT WICKET","STUMPED","LBW"]
out_times = [26,88,15,0,4,17]
fig = go.Figure(data=[go.Pie(labels=out_method, values=out_times)])
fig.update_layout(title="comparison on dkgettingout")
fig.show()

#performancebybattingposition
#msdavg
sns.barplot(x='Batting Position', y='Average', data=df7)
plt.xlabel('Batting Position')
plt.ylabel('Average')
plt.title('Average in Batting Position')
plt.show()

#msdsr
sns.barplot(x='Batting Position', y='Strike Rate', data=df7)
plt.xlabel('Batting Position')
plt.ylabel('Strike Rate')
plt.title('Strike Rate in Batting Position')
plt.show()

#dkavg
sns.barplot(x='Batting Position', y='Average', data=df8)
plt.xlabel('Batting Position')
plt.ylabel('Average')
plt.title('Average in Batting Position')
plt.show()

#dksr
sns.barplot(x='Batting Position', y='Strike Rate', data=df8)
plt.xlabel('Batting Position')
plt.ylabel('Strike Rate')
plt.title('Strike Rate in Batting Position')
plt.show()

#matchwinningknocksofMSd

#ratio of resulting runs
batting_positions = ["Runs% at wins","Runs% at Loss"]
Team_Runs = [2950,2054]
fig = go.Figure(data=[go.Pie(labels=batting_positions, values=Team_Runs)])
fig.update_layout(title="Performance by Match Result")
fig.show()
#strike RATEINIPLCAREERMSD
sns.barplot(x='Result', y='Strike Rate', data=df9)
plt.xlabel('RESULT')
plt.ylabel('Strike Rate')
plt.title('Strike Rate in Match Result')
plt.show()

#matchwinningknocksofdk

#ratio of resulting runs
batting_positions = ["Runs% at wins","Runs% at Loss"]
Team_Runs = [2170,2179]
fig = go.Figure(data=[go.Pie(labels=batting_positions, values=Team_Runs)])
fig.update_layout(title="Performance by Match Result")
fig.show()
#strike RATEINIPLCAREERDK
sns.barplot(x='Result', y='Strike Rate', data=df10)
plt.xlabel('RESULT')
plt.ylabel('Strike Rate')
plt.title('Strike Rate in Match Result')
plt.show()

#MSDWKPER
trace1 = go.Bar(x=df['Year'], y=df['Catches Taken'], name='Catches Taken')
trace2 = go.Bar(x=df['Year'], y=df['Stumpings'], name='Stumpings')
layout = go.Layout(title='Wicketkeeping Performance', xaxis_title='Year', yaxis_title='Catches/Stumping')
fig = go.Figure(data=[trace1,trace2], layout=layout)
fig.show()
#DKWKPER
trace1 = go.Bar(x=df3['Year'], y=df3['Catches Taken'], name='Catches Taken')
trace2 = go.Bar(x=df3['Year'], y=df3['Stumpings'], name='Stumpings')
layout = go.Layout(title='Wicketkeeping Performance', xaxis_title='Year', yaxis_title='Catches/Stumping')
fig = go.Figure(data=[trace1,trace2], layout=layout)
fig.show()

