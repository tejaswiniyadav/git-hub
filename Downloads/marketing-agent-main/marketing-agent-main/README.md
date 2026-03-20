# Marketing Agent

An AI-powered marketing consultant that proactively guides businesses through building their entire marketing presence. Built with LangGraph, LangChain, AWS Bedrock, and Streamlit.

Rather than waiting for instructions, the agent drives the conversation — it qualifies your business, recommends a roadmap, and executes each step automatically. Responses stream token-by-token for a real-time chat experience.

## Architecture

```
app.py                    # Streamlit UI with real-time streaming
graph/
  graph.py                # LangGraph wiring (async agent node + tool node + edges)
  state.py                # AgentState (extends MessagesState)
  prompt.py               # System prompt (consultant-style, phased flow)
  tools.py                # Tool aggregation
agents/
  __init__.py             # Registers all tools
  domain_agent.py         # Domain name suggestions
  logo_agent.py           # Logo generation (Amazon Titan Image Generator v2)
  strategy_agent.py       # Marketing strategy
  social_media_agent.py   # Social media content (Instagram, LinkedIn, X, Facebook)
  email_campaign_agent.py # 3-email marketing sequence
  seo_agent.py            # SEO keywords + meta descriptions
  ad_copy_agent.py        # Google Ads + social media ad copy
  tagline_agent.py        # Brand taglines + elevator pitches
```

## How It Works

The agent uses a single LangGraph `StateGraph` with two nodes:

1. **Agent node** — Claude Sonnet 4.6 (via AWS Bedrock) with streaming enabled decides whether to respond or call tools
2. **Tool node** — Executes the selected tool(s) and returns results

### Streaming

The UI uses `graph.astream_events(version="v2")` for true token-by-token streaming:
- LLM tokens appear in real-time as they're generated
- Tool execution shows a live status indicator (e.g. "Running create_marketing_strategy...")
- A blinking cursor indicates the response is still being generated

### Conversational Flow

The agent operates in three phases:

| Phase | What happens |
|-------|-------------|
| **Greet & Qualify** | Asks for business name, industry, and target audience (1-2 questions per turn) |
| **Recommend a Roadmap** | Proposes an ordered plan: strategy, taglines, logo, social media, ads, email, SEO, domains |
| **Execute & Auto-Proceed** | Runs each tool, summarizes results, tracks progress, and moves to the next step automatically |

## Tools

| Tool | Description | Model |
|------|-------------|-------|
| `create_marketing_strategy` | Comprehensive marketing plan with channels, messaging, KPIs, and timeline | Claude Haiku 4.5 |
| `generate_taglines` | 10 brand taglines/slogans + elevator pitch + positioning statement | Claude Haiku 4.5 |
| `generate_logo` | Professional logo image (512x512 PNG) | Amazon Titan Image Generator v2 |
| `create_social_media_content` | Platform-specific posts with captions, hashtags, and CTAs | Claude Haiku 4.5 |
| `create_ad_copy` | Google Search Ads + Facebook/Instagram Ads + LinkedIn Sponsored Posts | Claude Haiku 4.5 |
| `create_email_campaign` | 3-email sequence: welcome, value, conversion | Claude Haiku 4.5 |
| `generate_seo_keywords` | Primary/long-tail keywords, meta descriptions, content topics | Claude Haiku 4.5 |
| `get_domain_suggestions` | 10 domain name ideas across .com, .net, .io | Claude Haiku 4.5 |

## Prerequisites

- **Python 3.10+**
- **AWS Account** with Bedrock access enabled for:
  - `anthropic.claude-sonnet-4-6` (orchestrator)
  - `anthropic.claude-haiku-4-5-20251001-v1:0` (tool agents)
  - `amazon.titan-image-generator-v2:0` (logo generation)
- **AWS credentials** configured (`aws configure` or environment variables)

## Setup

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd marketing_agent
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux/macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   AWS_DEFAULT_REGION=us-east-1
   ```

   AWS credentials can be set via `aws configure` or:

   ```env
   AWS_ACCESS_KEY_ID=your_key
   AWS_SECRET_ACCESS_KEY=your_secret
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`.

## Usage

### Quick Start

Just type **"hi"** — the agent will introduce itself, ask about your business, and guide you through the entire process.

### Direct Requests

Jump straight to specific tools:

```
Create a marketing strategy for PawPolish, a premium dog grooming service in Austin TX
```

### Multi-Tool Requests

Request multiple services at once and they'll run in parallel:

```
Generate social media posts and ad copy for FreshBrew
```

### Full Roadmap Test

This prompt triggers 4+ tools in sequence:

```
I'm launching a premium dog grooming business called "PawPolish" targeting busy
pet owners in Austin, TX. Build out my full marketing foundation — start with
strategy, then taglines, a logo, and social media content to launch with.
```

## Project Structure

```
marketing_agent/
  app.py                    # Streamlit frontend (async streaming)
  requirements.txt          # Python dependencies
  .env                      # Environment variables (not committed)
  graph/
    __init__.py
    graph.py                # LangGraph state machine (async agent node)
    state.py                # Agent state definition
    prompt.py               # System prompt
    tools.py                # Tool aggregation
  agents/
    __init__.py             # Tool registry
    domain_agent.py
    logo_agent.py
    strategy_agent.py
    social_media_agent.py
    email_campaign_agent.py
    seo_agent.py
    ad_copy_agent.py
    tagline_agent.py
```

## License

MIT
