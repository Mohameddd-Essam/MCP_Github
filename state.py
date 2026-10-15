from typing import Annotated, Optional, TypedDict
from langgraph.graph import add_messages

class State(TypedDict):
    """
    State shared across the LangGraph workflow.
    """
    messages: Annotated[list, add_messages]
    repo: Optional[str]