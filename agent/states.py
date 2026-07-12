from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):

    user_request: str

    project_plan: str

    tasks: List[Dict[str, Any]]

    current_task: Dict[str, Any]

    current_code: str

    generated_files: List[str]

    review: Dict[str, Any]

    errors: List[str]

    retry_count: int

    status: str

    logs: List[str]

    execution_result: str

    completed: bool