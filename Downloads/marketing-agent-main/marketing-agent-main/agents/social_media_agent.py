from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

_llm = ChatBedrock(model="global.anthropic.claude-haiku-4-5-20251001-v1:0")


@tool
def create_social_media_content(business_name: str, platform: str = "") -> str:
    """Generate platform-specific social media posts for a business.
    Use this tool when the user asks for social media content, posts,
    captions, hashtags, or social media marketing for their business.
    Supports Instagram, LinkedIn, Twitter/X, and Facebook."""
    platform_instruction = (
        f"Focus specifically on {platform} content."
        if platform
        else "Create content for Instagram, LinkedIn, Twitter/X, and Facebook."
    )
    response = _llm.invoke([
        HumanMessage(content=(
            f"Create engaging social media content for the business below.\n\n"
            f"{platform_instruction}\n\n"
            f"For each platform, provide:\n"
            f"- 2 ready-to-post captions (different tones: professional and casual)\n"
            f"- Relevant hashtags (5-10 per post)\n"
            f"- A clear call-to-action (CTA)\n"
            f"- Suggested post format (carousel, reel, story, text post, etc.)\n\n"
            f"Make the content brand-aware, engaging, and optimized for each platform's algorithm.\n\n"
            f"Business Name: {business_name}\n\n"
            f"Generate social media content:"
        ))
    ])
    return response.content
