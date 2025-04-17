from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.express as px
import plotly
import json

app = Flask(__name__)


@app.route('/')
def dashboard():
    # Bar Chart Example
    bar_data = [go.Bar(x=['Product A', 'Product B', 'Product C'], y=[20, 14, 23])]
    bar_layout = go.Layout(title='Product Sales')

    
    line_data = [go.Scatter(x=['Jan', 'Feb', 'Mar', 'Apr'], y=[5, 10, 15, 20], mode='lines', name='Sales Growth')]
    line_layout = go.Layout(title='Sales Growth Over Time')

    
    pie_data = [go.Pie(labels=['Category A', 'Category B', 'Category C'], values=[30, 20, 50])]
    pie_layout = go.Layout(title='Market Share')

    
    bar_chart = json.dumps(bar_data, cls=plotly.utils.PlotlyJSONEncoder)
    line_chart = json.dumps(line_data, cls=plotly.utils.PlotlyJSONEncoder)
    pie_chart = json.dumps(pie_data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', bar_chart=bar_chart, line_chart=line_chart, pie_chart=pie_chart)

if __name__ == '__main__':
    app.run(debug=True)

