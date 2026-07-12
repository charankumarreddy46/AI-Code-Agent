from agent.graph import build_graph
from agent.states import AgentState


def main():
    print("AI CODE AGENT")

    user_request = input("\nEnter your project idea:\n\n> ")

    # Initial State
    state: AgentState = {
        "user_request": user_request,

        "project_plan": "",

        "tasks": [],

        "current_task": {},

        "current_code": "",

        "generated_files": [],

        "review": {},

        "errors": [],

        "retry_count": 0,

        "status": "started",

        "logs": [],

        "execution_result": "",

        "completed": False,
    }

    graph = build_graph()

    print("\n🚀 Building Project...\n")

    final_state = graph.invoke(state)

    print("\n" + "=" * 60)
    print("✅ BUILD FINISHED")
    print("=" * 60)

    print("\nStatus:")
    print(final_state["status"])

    print("\nGenerated Files:")

    if final_state["generated_files"]:

        for file in final_state["generated_files"]:
            print(f"  ✔ {file}")

    else:
        print("No files generated.")

    if final_state["errors"]:

        print("\nErrors:")

        for error in final_state["errors"]:
            print(f"  ❌ {error}")

    print("\nLogs:")

    for log in final_state["logs"]:
        print(f"  • {log}")

    print("\nProject Completed:", final_state["completed"])


if __name__ == "__main__":
    main()