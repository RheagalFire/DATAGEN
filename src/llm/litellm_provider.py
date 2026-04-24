from typing import Type

from langchain_community.chat_models import ChatLiteLLM

from .base import BaseProvider


class LiteLLMProvider(BaseProvider):
    """Provider for LiteLLM models."""

    def get_model_class(self) -> Type:
        """Returns the ChatLiteLLM class."""
        return ChatLiteLLM
