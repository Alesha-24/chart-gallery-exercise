import plotly
import plotly.graph_objs as go

#Chart 2 (PIE)
pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

labels = []
values = []
for x in pie_data:
    label = x["company"]
    value = x["market_share"]
    labels.append(label)
    values.append(value)

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data

trace = go.Pie(labels=labels, values=values, title = "Company Market Share")

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)

# CHART 2 (LINE)

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]
x_axis = []
y_axis = []
for x in line_data:
    x_coord = x["date"]
    y_coord = x["stock_price_usd"]
    x_axis.append(x_coord)
    y_axis.append(y_coord)
    
plotly.offline.plot({
    "data": [go.Scatter(x= x_axis, y=y_axis)],
    "layout": go.Layout(title="Stock Prices")
}, auto_open=True)


print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data


# CHART 3 (HORIZONTAL BAR)

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

x_values = []
y_values = []
for x in bar_data:
    x_value = x["viewers"]
    y_value = x["genre"]
    x_values.append(x_value)
    y_values.append(y_value)

trace = go.Bar(x=x_values, y=y_values, orientation = 'h', title = "Film Genre Popularity")

plotly.offline.plot([trace], filename="bar_chart.html", auto_open=True)


print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data
