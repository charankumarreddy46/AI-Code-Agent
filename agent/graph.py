from langgraph.graph import StateGraph, END

from agent.states import AgentState

from agent.nodes import (
    planner_node,
    architect_node,
    coder_node,
    reviewer_node,
    debugger_node,
)


def review_router(state: AgentState):
    """
    Decide whether to finish or send code to the debugger.
    """

    # Stop if maximum retries reached
    if state["retry_count"] >= 3:
        return "end"

    review = state["review"].upper()

    if "PASS" in review:
        return "end"

    return "debugger"


def build_graph():

    graph = StateGraph(AgentState)

    # Add Nodes
    graph.add_node("planner", planner_node)
    graph.add_node("architect", architect_node)
    graph.add_node("coder", coder_node)
    graph.add_node("reviewer", reviewer_node)
    graph.add_node("debugger", debugger_node)

    # Entry Point
    graph.set_entry_point("planner")

    # Normal Flow
    graph.add_edge("planner", "architect")
    graph.add_edge("architect", "coder")
    graph.add_edge("coder", "reviewer")

    # Conditional Routing
    graph.add_conditional_edges(
        "reviewer",
        review_router,
        {
            "end": END,
            "debugger": "debugger",
        },
    )

    # Debugger -> Reviewer
    graph.add_edge("debugger", "reviewer")

    return graph.compile()