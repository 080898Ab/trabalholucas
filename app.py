import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Dados simulados (substitua pelo DataFrame real se necessário)
data = {
    'Aspecto': ['Fachada', 'Interior', 'Mesa', 'Apresent. Atendente', 'Produtos',
                'Banheiro', 'Serviço do Garçom', 'Caixa'],
    'Nota Média': [8.22, 7.6892, 5.9372, 9.56, 5.4612, 4.909, 6.342, 3.75]
}
df = pd.DataFrame(data)

app = dash.Dash(__name__)
app.title = "Dashboard de Avaliação - Restaurante"

fig = px.bar(df, x='Aspecto', y='Nota Média',
             color='Nota Média',
             color_continuous_scale='RdYlGn',
             title='Notas por Aspecto Avaliado',
             labels={'Nota Média': 'Nota Média'})

app.layout = html.Div([
    html.H1("Dashboard de Avaliação do Restaurante", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig),
    html.P("Desenvolvido com Dash + Plotly", style={'textAlign': 'center', 'color': 'gray'})
])

if __name__ == '__main__':
    import os
    app.run(debug=os.getenv("DASH_DEBUG_MODE", "False") == "True", use_reloader=False)
