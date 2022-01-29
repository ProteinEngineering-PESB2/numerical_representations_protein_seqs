import plotly.graph_objects as go
encoders=['DNA-Binding', 'Folding class', 'Function estimation', 'Enzyme Family']

fig = go.Figure(data=[
    go.Bar(name='One Hot', x=encoders, y=[0.53, 0.61, 0.35, 0.48]),
    go.Bar(name='Tape Embedding', x=encoders, y=[0.65, 0.52, 0.54, 0.66]),
    go.Bar(name='Alpha Structure',x=encoders, y=[0.86, 0.91, 0.86, 0.90]),
    go.Bar(name='Beta Structure', x=encoders, y=[0.81, 0.88, 0.80, 0.84]),
    go.Bar(name='Hydrophobicity', x=encoders, y=[0.86, 0.84, 0.87, 0.86]),
    go.Bar(name='Energy',  x=encoders, y=[0.86, 0.92, 0.90, 0.81]),
    go.Bar(name='Volume', x=encoders, y=[0.80, 0.93, 0.86, 0.87]),
    go.Bar(name='Other Indexes', x=encoders, y=[0.81, 0.91, 0.89, 0.87]),
    go.Bar(name='Hydropathy', x=encoders, y=[0.78, 0.89, 0.91, 0.92])
])

fig.update_layout(barmode='group')
fig.write_image("fig2_c.svg")