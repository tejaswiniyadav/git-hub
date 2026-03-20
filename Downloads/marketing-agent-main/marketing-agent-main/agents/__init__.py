from agents.domain_agent import get_domain_suggestions
from agents.logo_agent import generate_logo
from agents.strategy_agent import create_marketing_strategy
from agents.social_media_agent import create_social_media_content
from agents.email_campaign_agent import create_email_campaign
from agents.seo_agent import generate_seo_keywords
from agents.ad_copy_agent import create_ad_copy
from agents.tagline_agent import generate_taglines

tools = [
    get_domain_suggestions,
    generate_logo,
    create_marketing_strategy,
    create_social_media_content,
    create_email_campaign,
    generate_seo_keywords,
    create_ad_copy,
    generate_taglines,
]
