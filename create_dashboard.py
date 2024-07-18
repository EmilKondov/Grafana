from grafanalib.core import (Dashboard, Graph, GridPos, Row, Target, TimeRange, YAxis)
from grafanalib._gen import DashboardEncoder
import json

dashboard_title = input("Enter Dashboard Title")
graph_title = input("Enter Graph Name")


# Define your dashboard
dashboard = Dashboard(
    title= dashboard_title,
    rows=[
        Row(
            panels=[
                Graph(
                    title= graph_title,
                    dataSource='Your Data Source',
                    targets=[
                        Target(
                            expr='rate(http_requests_total[5m])',
                            legendFormat='{{ handler }}',
                        ),
                    ],
                    yAxes=[
                        YAxis(format=1000),
                        YAxis(format=2000),
                    ],
                    gridPos=GridPos(h=8, w=24, x=0, y=0),
                ),
            ],
        ),
    ],
)

# Convert dashboard to JSON
dashboard_json = json.dumps(dashboard.to_json_data(), cls=DashboardEncoder)
with open('dashboard.json', 'w') as f:
    f.write(dashboard_json)

