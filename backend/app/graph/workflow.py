from langgraph.graph import StateGraph, START, END

from app.graph.state import BusinessState
from app.graph.planner import planner_node
from app.graph.analysis import analysis_node
from app.graph.recommendation import recommendation_node
from app.graph.response import response_node

# 1. Create the graph builder
builder = StateGraph(BusinessState)

# 2. Register the nodes
builder.add_node("planner", planner_node)
builder.add_node("analysis", analysis_node)
builder.add_node("recommendation", recommendation_node)
builder.add_node("response", response_node)

# 3. Connect the nodes with edges
builder.add_edge(START, "planner")
builder.add_edge("planner", "analysis")
builder.add_edge("analysis", "recommendation")
builder.add_edge("recommendation", "response")
builder.add_edge("response", END)

# 4. Compile the graph
business_graph = builder.compile()
