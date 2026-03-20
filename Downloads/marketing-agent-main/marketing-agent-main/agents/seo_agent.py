from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

_llm = ChatBedrock(model="global.anthropic.claude-haiku-4-5-20251001-v1:0")


@tool
def generate_seo_keywords(business_name: str) -> str:
    """Generate SEO keywords, meta descriptions, and content topic ideas for a business.
    Use this tool when the user asks for SEO help, keyword research, search engine
    optimization, meta tags, or content strategy for organic search."""
    response = _llm.invoke([
        HumanMessage(content=(
            f"Generate a comprehensive SEO keyword strategy for the business below.\n\n"
            f"Provide:\n"
            f"1. **Primary Keywords** (5-7): High-intent keywords directly related to the business. "
            f"For each, include estimated search intent (informational, navigational, transactional) "
            f"and relative difficulty (low, medium, high).\n\n"
            f"2. **Long-Tail Keywords** (8-10): Specific phrases with lower competition.\n\n"
            f"3. **Meta Description**: A compelling 150-160 character meta description for the homepage.\n\n"
            f"4. **Content Topic Ideas** (5): Blog post or page ideas that target the keywords above, "
            f"with a brief description of each.\n\n"
            f"5. **Quick SEO Wins**: 3 actionable tips the business can implement immediately.\n\n"
            f"Business Name: {business_name}\n\n"
            f"Generate SEO strategy:"
        ))
    ])
    return response.content
