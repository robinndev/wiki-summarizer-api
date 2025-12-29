from enum import Enum


class LLMModel(str, Enum):
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"
    GPT_3_5 = "gpt-3.5-turbo"


class LLMTemperature(float, Enum):
    VERY_LOW = 0.0
    LOW = 0.3
    MEDIUM = 0.7
