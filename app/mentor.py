from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

from app.llm import get_llm
from app.prompts import SYSTEM_PROMPT


def get_mentor_response(user_input: str, chat_history: list) -> str:
    llm = get_llm()

    # Build the full prompt payload: standing rules + prior turns + current turn
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *chat_history,
        HumanMessage(content=user_input),
    ]

    response = llm.invoke(messages)
    
    reply_text =(
        response.content
        if isinstance(response.content,str)
        else str(response.content)
    )

    # Save the turn only AFTER the model call succeeds
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=reply_text))

    return reply_text