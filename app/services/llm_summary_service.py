from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.core.llm_config import LLMModel, LLMTemperature
from app.core.prompts import SUMMARY_PROMPT


class LLMSummaryService:
    def __init__(
        self,
        model: LLMModel = LLMModel.GPT_4O_MINI,
        temperature: LLMTemperature = LLMTemperature.LOW,
    ):
        self.llm = ChatOpenAI(
            model=model.value,
            temperature=temperature.value,
        )

        self.prompt = ChatPromptTemplate.from_template(SUMMARY_PROMPT)

        self.chain = self.prompt | self.llm

    def summarize(self, text: str, max_words: int) -> str:
        response = self.chain.invoke({
            "text": text,
            "max_words": max_words
        })

        return response.content.strip()
