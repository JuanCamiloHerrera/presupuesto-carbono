# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:40:17 2024

@author: camilo

Dashboard of net GHG emissions pathways and its correspondend quinquennial budget
"""

import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd


############################ DASH LAYOUT ##########################
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#app = dash.Dash(__name__)
server=app.server


app.css.config.serve_locally = False

app.layout = html.Div([
    # Title
    html.Div(
        children=[
            html.H1("Presupuestos de carbono nacionales", className="title"), 
        ]
    ),

    # Introduction and Instructions Box
    html.Div(
        children=[
            html.Div(
                children=[
                    html.P("Esta es una simple aplicación para visualizar una senda de emisiones netas de GEI y su implicación en los Presupuestos de carbono nacionales."),
                    html.P("Modifique la senda de emisiones netas entre los años 2025 y 2045 en sus respectivas cajas, y observe como cambian los Presupuestos de carbono quinquenales y las Emisiones acumuladas 2020-2050 en la gráfica inferior."),
                    html.P("Recuerde que se busca el cumplimiento de los criterios establecidos para el Presupuesto de Carbono nacional, dentro de los cuales se incluye:"),
                    html.Ul([
                        html.Li("El cumplimiento de la meta de la NDC en 2030 (Emitir como máximo 169.44 MtCO2e)."),
                        html.Li("Alineación con la meta de carbono neutralidad a 2050:"),
                        html.Li("Alineación con el mensaje de estabilización de las emisiones para 2025."),
                        html.Li("Alineación con el mensaje de mantener una trayectoria decreciente de las emisiones posterior a 2025."),
                    ])
                ],
                className="box",
            ),
        ]
    ),

    # Dash scenarios pathways and input boxes
    html.Div([
        dcc.Graph(id='scatter-chart'),
        html.Br(),
    html.Div([
        html.Div([
            html.Label('2025:'),
            dcc.Input(id='value-2025', type='number', min=0, max=400, value=220),
        ], style={'display': 'flex', 'align-items': 'center'}),
    
        html.Div(style={'width': '20px'}),
    
        html.Div([
            html.Label('2030:'),
            dcc.Input(id='value-2030', type='number', min=0, max=400, value=170),
        ], style={'display': 'flex', 'align-items': 'center'}),
    
        html.Div(style={'width': '20px'}),
    
        html.Div([
            html.Label('2035:'),
            dcc.Input(id='value-2035', type='number', min=0, max=400, value=120),
        ], style={'display': 'flex', 'align-items': 'center'}),
    
        html.Div(style={'width': '20px'}),
    
        html.Div([
            html.Label('2040:'),
            dcc.Input(id='value-2040', type='number', min=0, max=400, value=75),
        ], style={'display': 'flex', 'align-items': 'center'}),
    
        html.Div(style={'width': '20px'}),
    
        html.Div([
            html.Label('2045:'),
            dcc.Input(id='value-2045', type='number', min=0, max=400, value=35),
        ], style={'display': 'flex', 'align-items': 'center'}),
    ], style={'display': 'flex', 'flex-wrap': 'wrap'})

    ]),
    #Dash budget chart
    html.Div([
        dcc.Graph(id='budget-chart'),
    ])
])

app.css.append_css({
    'external_url': (
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    )
})




########################## SCENARIO PATHWAYS CHART ##########################

#Callback
@app.callback(
    Output('scatter-chart', 'figure'),
    [Input('value-2025', 'value'), Input('value-2030', 'value'),
     Input('value-2035', 'value'), Input('value-2040', 'value'),
     Input('value-2045', 'value')]
)




#Update function
def update_chart(value_2025, value_2030, value_2035, value_2040, value_2045):
    
    #Scenarios
    year = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
    lower = [293, 292, 270, 249, 229, 209, 189, 169]
    upper = [318, 319, 316, 294, 266, 237, 209, 180]
    ndc = [262,257,250,246,245,236,229,218]
    
    year1 = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050]
    lower1 = [213, 199, 187, 177, 167, 157, 147, 135, 128, 120, 113, 105, 98, 92, 85, 79, 72, 65, 58, 52, 46, 39, 33, 26, 19, 13, 5, 0]
    upper1 = [237, 226, 217, 210, 205, 200, 194, 189, 180, 172, 163, 154, 146, 139, 133, 126, 120, 114, 106, 99, 93, 87, 80, 73, 67, 60, 53, 48]
    
    year2 = [2020, 2021, 2022]
    mean2 = [253, 264, 236]
    lower2 = [236, 247, 218]
    upper2 = [270, 282, 253]
    
    year3 = [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050]
    ccdr_wb = [264, 250, 239, 227, 212, 200, 187, 174, 161, 149, 140, 128, 119, 111, 100, 89, 79, 68, 58, 49, 44, 36, 30, 23, 17, 10, 4, 0]
    bid = [206, 200, 193, 181, 168, 155, 143, 130, 126, 122, 118, 114, 110, 105, 100, 95, 89, 84, 77, 69, 62, 54, 46, 39, 32, 25, 17, 10]

    
    # Set color for all traces
    acelerador_color = 'rgba(25, 107, 36, 0.2)'  
    e2050_color = 'rgba(160, 43, 147, 0.2)' 
    inventario_color='rgba(233, 113, 50, 0.2)' 
    ccdr_color= 'rgba(78, 167, 46, 0.6)' 
    bid_color='rgba(13, 58, 78, 0.6)' 
    ndc_color='rgba(255, 192, 0, 0.6)' 
    
    #Acelerador
    trace_lower = go.Scatter(x=year, y=lower, mode='lines', name='Acelerador', line=dict(color=acelerador_color), showlegend=False)
    trace_upper = go.Scatter(x=year, y=upper, mode='lines', name='Acelerador', fill='tonexty', fillcolor=acelerador_color, line=dict(color=acelerador_color))

    #E2050
    trace_lower1 = go.Scatter(x=year1, y=lower1, mode='lines', name='E2050', line=dict(color=e2050_color), showlegend=False)
    trace_upper1 = go.Scatter(x=year1, y=upper1, mode='lines', name='E2050', fill='tonexty', fillcolor=e2050_color, line=dict(color=e2050_color))

    #INGEI
    trace_lower2 = go.Scatter(x=year2, y=lower2, mode='lines', name='Intervalo de confianza estimación INGEI', line=dict(color=inventario_color), showlegend=False)
    trace_upper2 = go.Scatter(x=year2, y=upper2, mode='lines', name='Intervalo de confianza estimación INGEI', fill='tonexty', fillcolor=inventario_color, line=dict(color=inventario_color), showlegend=False)
    trace_mean2 = go.Scatter(x=year2, y=mean2, mode='markers+lines', name='Estimación INGEI', line=dict(color='rgba(233, 113, 50, 0.6)'))

    #Single scatter
    trace_ccdr_wb = go.Scatter(x=year3, y=ccdr_wb, mode='markers+lines', name='CCDR-WB', marker=dict(color=ccdr_color, size=6, symbol='x'))
    trace_bid = go.Scatter(x=year3, y=bid, mode='markers+lines', name='BID', marker=dict(color=bid_color, size=6, symbol='cross'))
    trace_ndc = go.Scatter(x=year, y=ndc, mode='markers+lines', name='NDC-M3', marker=dict(color=ndc_color, size=6, symbol='square'))

    #Create layout
    updated_chart_layout = go.Layout(title='Escenarios de emisiones netas GEI Colombia', yaxis=dict(title='MtCO2eq'), xaxis=dict(title='Año'),margin=dict(t=150))

    #Create figure for the updated chart
    updated_chart_fig = go.Figure(data=[trace_lower, trace_upper, trace_lower1, trace_upper1, trace_lower2, trace_upper2, trace_mean2, trace_ccdr_wb, trace_bid, trace_ndc], layout=updated_chart_layout)

    # Static datapoints at the beginning and end
    updated_chart_fig.add_trace(go.Scatter(x=[2020, 2050], y=[253, 0], mode='markers', marker=dict(size=15, color='blue'), name=None, showlegend=False))

    #Connecting lines
    updated_chart_fig.add_trace(go.Scatter(x=[2020, 2025, 2030, 2035, 2040, 2045, 2050], y=[253, value_2025, value_2030, value_2035, value_2040, value_2045, 0], mode='lines', line=dict(color='blue',width=4), name='Senda emisiones netas'))

    #Data points as markers
    updated_chart_fig.add_trace(go.Scatter(x=[2025, 2030, 2035, 2040, 2045], y=[value_2025, value_2030, value_2035, value_2040, value_2045], mode='markers', marker=dict(size=15, color='red'), name='Petricor&Geosmina', showlegend=False))
    
    #Legend position
    updated_chart_fig.update_layout(height=700,legend=dict(orientation="h", yanchor="top", y=1.1, x=-0.03))
        
    return updated_chart_fig

#################### BUDGET CHART ############################

#Callback
@app.callback(
    Output('budget-chart', 'figure'),
    [Input('value-2025', 'value'), Input('value-2030', 'value'),
     Input('value-2035', 'value'), Input('value-2040', 'value'),
     Input('value-2045', 'value')]
)


#Update function
def update_chart1(value_2025, value_2030, value_2035, value_2040, value_2045):
    global df_budget, total_budget
    #Initial static values
    years = list(range(2020, 2051))
    emissions = [253] + [0] * (len(years) - 2) + [0]
    
    # Create the initial DataFrame
    df = pd.DataFrame({'Year': years, 'NetEmissions': emissions})
    
    
    #Callback years and values (replace these with your actual callback values)
    callback_years = [2025, 2030, 2035, 2040, 2045]
    callback_values = {
        2025: value_2025,
        2030: value_2030,
        2035: value_2035,
        2040: value_2040,
        2045: value_2045
    }
    
    #Update dynamic values in the DataFrame
    for year in callback_years:
        if year in callback_values:
            df.loc[df['Year'] == year, 'NetEmissions'] = callback_values[year]

    # Interpolate values inbetween
    df = df.set_index('Year')
    for i in range(2020,2050,5):
        for j in range(i+1,i+5):
            df.loc[j,'NetEmissions'] = df.loc[i,'NetEmissions'] + (df.loc[i+5,'NetEmissions'] - df.loc[i,'NetEmissions'] )*(j-i)/5
            #df.NetEmissions[df['Year']==j] = df.NetEmissions[df['Year']==i] + (df.NetEmissions[df['Year']==i+5] - df.NetEmissions[df['Year']==i] )*(j-i)/5
    
    
    #Budget estimation
    p1=752.914+df.loc[2023:2025,'NetEmissions'].sum() #Mean of estimated emissions from 2020 to 2022 (752.914) plus the output of the pathway form 2023 to 2025
    p2=df.loc[2026:2030,'NetEmissions'].sum()
    p3=df.loc[2031:2035,'NetEmissions'].sum()
    p4=df.loc[2036:2040,'NetEmissions'].sum()
    p5=df.loc[2041:2045,'NetEmissions'].sum()
    p6=df.loc[2046:2050,'NetEmissions'].sum()
    budgetname = ['2020-2025','2026-2030','2031-2035','2036-2040','2041-2045','2046-2050']
    budget=[p1,p2,p3,p4,p5,p6]
    df_budget = pd.DataFrame({'budgetname':budgetname,'budget':budget})
    total_budget = round(df.loc[:,'NetEmissions'].sum())
        
    
    fig = go.Figure()
    
    #Add bar trace with data labels
    fig.add_trace(go.Bar(
        x=df_budget['budgetname'],
        y=df_budget['budget'],
        marker_color='steelblue',
        text=round(df_budget['budget']),
        textposition=['inside' if i == 0 else 'auto' for i in range(len(df_budget))],
        error_y=dict(type='data', array=[52], visible=True, color='magenta', thickness=2, width=4), 
    ))
    
    
    #Add text box
    fig.add_annotation(
        text=f"Emisiones acumuladas 2020-2050: {total_budget} MtCO2eq",
        showarrow=False,
        xref='paper', yref='paper',
        x=0.5, y=1.15,
        font=dict(size=18, color='red', family='Arial'),
        bordercolor='black',
        borderwidth=2,
    )
    
    
    fig.update_layout(
        title='Presupuestos de carbono quinquenales',
        xaxis_title='Presupuesto',
        yaxis_title='MtCO2eq',
    )
    
        
    
    return fig





#app.run_server()  #Para correr en spyder IDE activar esta linea y ocultar la de heroku
if __name__ == '__main__':
    app.run_server(debug=True)   #Para correr en Heroku app activar esta linea y ocultar la de spyder
