from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

_llm = ChatBedrock(model="global.anthropic.claude-haiku-4-5-20251001-v1:0")


@tool
def create_marketing_strategy(business_name: str) -> str:
    """Create a comprehensive marketing strategy for a business.
    Use this tool when the user asks for marketing strategies, campaign plans,
    social media strategies, advertising ideas, or anything related to
    marketing planning and execution."""
    response = _llm.invoke([
        HumanMessage(content=(
            f"Create a comprehensive marketing strategy for the given domain/business.\n\n"
            f"Include:\n"
            f"- Target audience analysis\n"
            f"- Marketing channels (social media, content marketing, SEO, etc.)\n"
            f"- Key messaging and positioning\n"
            f"- Campaign ideas\n"
            f"- Success metrics and KPIs\n"
            f"- Implementation timeline\n\n"
            f"Provide actionable recommendations that can be implemented immediately.\n\n"
            f"Domain Name: {business_name}\n\n"
            f"Create a comprehensive marketing strategy:"
        ))
    ])
    return response.content
