# Crawl4AI Documentation

## Introduction

URL: https://crawl4ai.com/mkdocs/introduction/

# Introduction

Welcome to the documentation for Crawl4AI v0.2.5! 🕷️🤖

Crawl4AI is designed to simplify the process of crawling web pages and
extracting useful information for large language models (LLMs) and AI
applications. Whether you're using it as a REST API, a Python library, or
through a Google Colab notebook, Crawl4AI provides powerful features to make
web data extraction easier and more efficient.

## Key Features ✨

  * **🆓 Completely Free and Open-Source** : Crawl4AI is free to use and open-source, making it accessible for everyone.
  * **🤖 LLM-Friendly Output Formats** : Supports JSON, cleaned HTML, and markdown formats.
  * **🌍 Concurrent Crawling** : Crawl multiple URLs simultaneously to save time.
  * **🎨 Media Extraction** : Extract all media tags including images, audio, and video.
  * **🔗 Link Extraction** : Extract all external and internal links from web pages.
  * **📚 Metadata Extraction** : Extract metadata from web pages for additional context.
  * **🔄 Custom Hooks** : Define custom hooks for authentication, headers, and page modifications before crawling.
  * **🕵️ User Agent Support** : Customize the user agent for HTTP requests.
  * **🖼️ Screenshot Capability** : Take screenshots of web pages during crawling.
  * **📜 JavaScript Execution** : Execute custom JavaScripts before crawling.
  * **📚 Advanced Chunking and Extraction Strategies** : Utilize topic-based, regex, sentence chunking, cosine clustering, and LLM extraction strategies.
  * **🎯 CSS Selector Support** : Extract specific content using CSS selectors.
  * **📝 Instruction/Keyword Refinement** : Pass instructions or keywords to refine the extraction process.

Check the
[Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md) for
more details.

## Power and Simplicity of Crawl4AI 🚀

Crawl4AI provides an easy way to crawl and extract data from web pages without
installing any library. You can use the REST API on our server or run the
local server on your machine. For more advanced control, use the Python
library to customize your crawling and extraction strategies.

Explore the documentation to learn more about the features, installation
process, usage examples, and how to contribute to Crawl4AI. Let's make the web
more accessible and useful for AI applications! 💪🌐🤖



## Installation

URL: https://crawl4ai.com/mkdocs/installation/

# Installation 💻

Crawl4AI offers flexible installation options to suit various use cases. You
can install it as a Python package, use it with Docker, or run it as a local
server.

## Option 1: Python Package Installation (Recommended)

Crawl4AI is now available on PyPI, making installation easier than ever.
Choose the option that best fits your needs:

### Basic Installation

For basic web crawling and scraping tasks:

    
    
    pip install crawl4ai
    playwright install # Install Playwright dependencies
    

### Installation with PyTorch

For advanced text clustering (includes CosineSimilarity cluster strategy):

    
    
    pip install crawl4ai[torch]
    

### Installation with Transformers

For text summarization and Hugging Face models:

    
    
    pip install crawl4ai[transformer]
    

### Full Installation

For all features:

    
    
    pip install crawl4ai[all]
    

### Development Installation

For contributors who plan to modify the source code:

    
    
    git clone https://github.com/unclecode/crawl4ai.git
    cd crawl4ai
    pip install -e ".[all]"
    playwright install # Install Playwright dependencies
    

💡 After installation with "torch", "transformer", or "all" options, it's
recommended to run the following CLI command to load the required models:

    
    
    crawl4ai-download-models
    

This is optional but will boost the performance and speed of the crawler. You
only need to do this once after installation.

## Option 2: Using Docker (Coming Soon)

Docker support for Crawl4AI is currently in progress and will be available
soon. This will allow you to run Crawl4AI in a containerized environment,
ensuring consistency across different systems.

## Option 3: Local Server Installation

For those who prefer to run Crawl4AI as a local server, instructions will be
provided once the Docker implementation is complete.

## Verifying Your Installation

After installation, you can verify that Crawl4AI is working correctly by
running a simple Python script:

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(url="https://www.example.com")
            print(result.markdown[:500])  # Print first 500 characters
    
    if __name__ == "__main__":
        asyncio.run(main())
    

This script should successfully crawl the example website and print the first
500 characters of the extracted content.

## Getting Help

If you encounter any issues during installation or usage, please check the
[documentation](https://crawl4ai.com/mkdocs/) or raise an issue on the [GitHub
repository](https://github.com/unclecode/crawl4ai/issues).

Happy crawling! 🕷️🤖



## Quick Start

URL: https://crawl4ai.com/mkdocs/quickstart/

# Quick Start Guide 🚀

Welcome to the Crawl4AI Quickstart Guide! In this tutorial, we'll walk you
through the basic usage of Crawl4AI with a friendly and humorous tone. We'll
cover everything from basic usage to advanced features like chunking and
extraction strategies, all with the power of asynchronous programming. Let's
dive in! 🌟

## Getting Started 🛠️

First, let's import the necessary modules and create an instance of
`AsyncWebCrawler`. We'll use an async context manager, which handles the setup
and teardown of the crawler for us.

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            # We'll add our crawling code here
            pass
    
    if __name__ == "__main__":
        asyncio.run(main())
    

### Basic Usage

Simply provide a URL and let Crawl4AI do the magic!

    
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(url="https://www.nbcnews.com/business")
            print(f"Basic crawl result: {result.markdown[:500]}")  # Print first 500 characters
    
    asyncio.run(main())
    

### Taking Screenshots 📸

Let's take a screenshot of the page!

    
    
    import base64
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(url="https://www.nbcnews.com/business", screenshot=True)
            with open("screenshot.png", "wb") as f:
                f.write(base64.b64decode(result.screenshot))
            print("Screenshot saved to 'screenshot.png'!")
    
    asyncio.run(main())
    

### Understanding Parameters 🧠

By default, Crawl4AI caches the results of your crawls. This means that
subsequent crawls of the same URL will be much faster! Let's see this in
action.

    
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            # First crawl (caches the result)
            result1 = await crawler.arun(url="https://www.nbcnews.com/business")
            print(f"First crawl result: {result1.markdown[:100]}...")
    
            # Force to crawl again
            result2 = await crawler.arun(url="https://www.nbcnews.com/business", bypass_cache=True)
            print(f"Second crawl result: {result2.markdown[:100]}...")
    
    asyncio.run(main())
    

### Adding a Chunking Strategy 🧩

Let's add a chunking strategy: `RegexChunking`! This strategy splits the text
based on a given regex pattern.

    
    
    from crawl4ai.chunking_strategy import RegexChunking
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://www.nbcnews.com/business",
                chunking_strategy=RegexChunking(patterns=["\n\n"])
            )
            print(f"RegexChunking result: {result.extracted_content[:200]}...")
    
    asyncio.run(main())
    

### Adding an Extraction Strategy 🧠

Let's get smarter with an extraction strategy: `JsonCssExtractionStrategy`!
This strategy extracts structured data from HTML using CSS selectors.

    
    
    from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
    import json
    
    async def main():
        schema = {
            "name": "News Articles",
            "baseSelector": "article.tease-card",
            "fields": [
                {
                    "name": "title",
                    "selector": "h2",
                    "type": "text",
                },
                {
                    "name": "summary",
                    "selector": "div.tease-card__info",
                    "type": "text",
                }
            ],
        }
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://www.nbcnews.com/business",
                extraction_strategy=JsonCssExtractionStrategy(schema, verbose=True)
            )
            extracted_data = json.loads(result.extracted_content)
            print(f"Extracted {len(extracted_data)} articles")
            print(json.dumps(extracted_data[0], indent=2))
    
    asyncio.run(main())
    

### Using LLMExtractionStrategy 🤖

Time to bring in the big guns: `LLMExtractionStrategy`! This strategy uses a
large language model to extract relevant information from the web page.

    
    
    from crawl4ai.extraction_strategy import LLMExtractionStrategy
    import os
    from pydantic import BaseModel, Field
    
    class OpenAIModelFee(BaseModel):
        model_name: str = Field(..., description="Name of the OpenAI model.")
        input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
        output_fee: str = Field(..., description="Fee for output token for the OpenAI model.")
    
    async def main():
        if not os.getenv("OPENAI_API_KEY"):
            print("OpenAI API key not found. Skipping this example.")
            return
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://openai.com/api/pricing/",
                word_count_threshold=1,
                extraction_strategy=LLMExtractionStrategy(
                    provider="openai/gpt-4o",
                    api_token=os.getenv("OPENAI_API_KEY"),
                    schema=OpenAIModelFee.schema(),
                    extraction_type="schema",
                    instruction="""From the crawled content, extract all mentioned model names along with their fees for input and output tokens. 
                    Do not miss any models in the entire content. One extracted model JSON format should look like this: 
                    {"model_name": "GPT-4", "input_fee": "US$10.00 / 1M tokens", "output_fee": "US$30.00 / 1M tokens"}.""",
                ),
                bypass_cache=True,
            )
            print(result.extracted_content)
    
    asyncio.run(main())
    

### Interactive Extraction 🖱️

Let's use JavaScript to interact with the page before extraction!

    
    
    async def main():
        js_code = """
        const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More'));
        loadMoreButton && loadMoreButton.click();
        """
    
        wait_for = """() => {
            return Array.from(document.querySelectorAll('article.tease-card')).length > 10;
        }"""
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://www.nbcnews.com/business",
                js_code=js_code,
                wait_for=wait_for,
                css_selector="article.tease-card",
                bypass_cache=True,
            )
            print(f"JavaScript interaction result: {result.extracted_content[:500]}")
    
    asyncio.run(main())
    

### Advanced Session-Based Crawling with Dynamic Content 🔄

In modern web applications, content is often loaded dynamically without
changing the URL. This is common in single-page applications (SPAs) or
websites using infinite scrolling. Traditional crawling methods that rely on
URL changes won't work here. That's where Crawl4AI's advanced session-based
crawling comes in handy!

Here's what makes this approach powerful:

  1. **Session Preservation** : By using a `session_id`, we can maintain the state of our crawling session across multiple interactions with the page. This is crucial for navigating through dynamically loaded content.

  2. **Asynchronous JavaScript Execution** : We can execute custom JavaScript to trigger content loading or navigation. In this example, we'll click a "Load More" button to fetch the next page of commits.

  3. **Dynamic Content Waiting** : The `wait_for` parameter allows us to specify a condition that must be met before considering the page load complete. This ensures we don't extract data before the new content is fully loaded.

Let's see how this works with a real-world example: crawling multiple pages of
commits on a GitHub repository. The URL doesn't change as we load more
commits, so we'll use these advanced techniques to navigate and extract data.

    
    
    import json
    from bs4 import BeautifulSoup
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            url = "https://github.com/microsoft/TypeScript/commits/main"
            session_id = "typescript_commits_session"
            all_commits = []
    
            js_next_page = """
            const button = document.querySelector('a[data-testid="pagination-next-button"]');
            if (button) button.click();
            """
    
            wait_for = """() => {
                const commits = document.querySelectorAll('li.Box-sc-g0xbh4-0 h4');
                if (commits.length === 0) return false;
                const firstCommit = commits[0].textContent.trim();
                return firstCommit !== window.lastCommit;
            }"""
    
            schema = {
                "name": "Commit Extractor",
                "baseSelector": "li.Box-sc-g0xbh4-0",
                "fields": [
                    {
                        "name": "title",
                        "selector": "h4.markdown-title",
                        "type": "text",
                        "transform": "strip",
                    },
                ],
            }
            extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
            for page in range(3):  # Crawl 3 pages
                result = await crawler.arun(
                    url=url,
                    session_id=session_id,
                    css_selector="li.Box-sc-g0xbh4-0",
                    extraction_strategy=extraction_strategy,
                    js_code=js_next_page if page > 0 else None,
                    wait_for=wait_for if page > 0 else None,
                    js_only=page > 0,
                    bypass_cache=True,
                    headless=False,
                )
    
                assert result.success, f"Failed to crawl page {page + 1}"
    
                commits = json.loads(result.extracted_content)
                all_commits.extend(commits)
    
                print(f"Page {page + 1}: Found {len(commits)} commits")
    
            await crawler.crawler_strategy.kill_session(session_id)
            print(f"Successfully crawled {len(all_commits)} commits across 3 pages")
    
    asyncio.run(main())
    

In this example, we're crawling multiple pages of commits from a GitHub
repository. The URL doesn't change as we load more commits, so we use
JavaScript to click the "Load More" button and a `wait_for` condition to
ensure the new content is loaded before extraction. This powerful combination
allows us to navigate and extract data from complex, dynamically-loaded web
applications with ease!

## Congratulations! 🎉

You've made it through the Crawl4AI Quickstart Guide! Now go forth and crawl
the web asynchronously like a pro! 🕸️

Remember, these are just a few examples of what Crawl4AI can do. For more
advanced usage, check out our other documentation pages:

  * [LLM Extraction](../examples/llm_extraction/)
  * [JS Execution & CSS Filtering](../examples/js_execution_css_filtering/)
  * [Hooks & Auth](../examples/hooks_auth/)
  * [Summarization](../examples/summarization/)
  * [Research Assistant](../examples/research_assistant/)

Happy crawling! 🚀



## Intro

URL: https://crawl4ai.com/mkdocs/examples/

# Examples

Welcome to the examples section of Crawl4AI documentation! In this section,
you will find practical examples demonstrating how to use Crawl4AI for various
web crawling and data extraction tasks. Each example is designed to showcase
different features and capabilities of the library.

## Examples Index

### [LLM Extraction](llm_extraction/)

This example demonstrates how to use Crawl4AI to extract information using
Large Language Models (LLMs). You will learn how to configure the
`LLMExtractionStrategy` to get structured data from web pages.

### [JSON CSS Extraction](json_css_extraction/)

This example demonstrates how to use Crawl4AI to extract structured data
without using LLM, and just focusing on page structure. You will learn how to
use the `JsonCssExtractionStrategy` to extract data using CSS selectors.

### [JS Execution & CSS Filtering](js_execution_css_filtering/)

Learn how to execute custom JavaScript code and filter data using CSS
selectors. This example shows how to perform complex web interactions and
extract specific content from web pages.

### [Hooks & Auth](hooks_auth/)

This example covers the use of custom hooks for authentication and other pre-
crawling tasks. You will see how to set up hooks to modify headers,
authenticate sessions, and perform other preparatory actions before crawling.

### [Summarization](summarization/)

Discover how to use Crawl4AI to summarize web page content. This example
demonstrates the summarization capabilities of the library, helping you
extract concise information from lengthy web pages.

### [Research Assistant](research_assistant/)

In this example, Crawl4AI is used as a research assistant to gather and
organize information from multiple sources. You will learn how to use various
extraction and chunking strategies to compile a comprehensive report.

* * *

Each example includes detailed explanations and code snippets to help you
understand and implement the features in your projects. Click on the links to
explore each example and start making the most of Crawl4AI!



## Structured Data Extraction

URL: https://crawl4ai.com/mkdocs/examples/json_css_extraction/

# JSON CSS Extraction Strategy with AsyncWebCrawler

The `JsonCssExtractionStrategy` is a powerful feature of Crawl4AI that allows
you to extract structured data from web pages using CSS selectors. This method
is particularly useful when you need to extract specific data points from a
consistent HTML structure, such as tables or repeated elements. Here's how to
use it with the AsyncWebCrawler.

## Overview

The `JsonCssExtractionStrategy` works by defining a schema that specifies: 1\.
A base CSS selector for the repeating elements 2\. Fields to extract from each
element, each with its own CSS selector

This strategy is fast and efficient, as it doesn't rely on external services
like LLMs for extraction.

## Example: Extracting Cryptocurrency Prices from Coinbase

Let's look at an example that extracts cryptocurrency prices from the Coinbase
explore page.

    
    
    import json
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
    
    async def extract_structured_data_using_css_extractor():
        print("\n--- Using JsonCssExtractionStrategy for Fast Structured Output ---")
    
        # Define the extraction schema
        schema = {
            "name": "Coinbase Crypto Prices",
            "baseSelector": ".cds-tableRow-t45thuk",
            "fields": [
                {
                    "name": "crypto",
                    "selector": "td:nth-child(1) h2",
                    "type": "text",
                },
                {
                    "name": "symbol",
                    "selector": "td:nth-child(1) p",
                    "type": "text",
                },
                {
                    "name": "price",
                    "selector": "td:nth-child(2)",
                    "type": "text",
                }
            ],
        }
    
        # Create the extraction strategy
        extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
        # Use the AsyncWebCrawler with the extraction strategy
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://www.coinbase.com/explore",
                extraction_strategy=extraction_strategy,
                bypass_cache=True,
            )
    
            assert result.success, "Failed to crawl the page"
    
            # Parse the extracted content
            crypto_prices = json.loads(result.extracted_content)
            print(f"Successfully extracted {len(crypto_prices)} cryptocurrency prices")
            print(json.dumps(crypto_prices[0], indent=2))
    
        return crypto_prices
    
    # Run the async function
    asyncio.run(extract_structured_data_using_css_extractor())
    

## Explanation of the Schema

The schema defines how to extract the data:

  * `name`: A descriptive name for the extraction task.
  * `baseSelector`: The CSS selector for the repeating elements (in this case, table rows).
  * `fields`: An array of fields to extract from each element:
  * `name`: The name to give the extracted data.
  * `selector`: The CSS selector to find the specific data within the base element.
  * `type`: The type of data to extract (usually "text" for textual content).

## Advantages of JsonCssExtractionStrategy

  1. **Speed** : CSS selectors are fast to execute, making this method efficient for large datasets.
  2. **Precision** : You can target exactly the elements you need.
  3. **Structured Output** : The result is already structured as JSON, ready for further processing.
  4. **No External Dependencies** : Unlike LLM-based strategies, this doesn't require any API calls to external services.

## Tips for Using JsonCssExtractionStrategy

  1. **Inspect the Page** : Use browser developer tools to identify the correct CSS selectors.
  2. **Test Selectors** : Verify your selectors in the browser console before using them in the script.
  3. **Handle Dynamic Content** : If the page uses JavaScript to load content, you may need to combine this with JS execution (see the Advanced Usage section).
  4. **Error Handling** : Always check the `result.success` flag and handle potential failures.

## Advanced Usage: Combining with JavaScript Execution

For pages that load data dynamically, you can combine the
`JsonCssExtractionStrategy` with JavaScript execution:

    
    
    async def extract_dynamic_structured_data():
        schema = {
            "name": "Dynamic Crypto Prices",
            "baseSelector": ".crypto-row",
            "fields": [
                {"name": "name", "selector": ".crypto-name", "type": "text"},
                {"name": "price", "selector": ".crypto-price", "type": "text"},
            ]
        }
    
        js_code = """
        window.scrollTo(0, document.body.scrollHeight);
        await new Promise(resolve => setTimeout(resolve, 2000));  // Wait for 2 seconds
        """
    
        extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://example.com/crypto-prices",
                extraction_strategy=extraction_strategy,
                js_code=js_code,
                wait_for=".crypto-row:nth-child(20)",  # Wait for 20 rows to load
                bypass_cache=True,
            )
    
            crypto_data = json.loads(result.extracted_content)
            print(f"Extracted {len(crypto_data)} cryptocurrency entries")
    
    asyncio.run(extract_dynamic_structured_data())
    

This advanced example demonstrates how to: 1\. Execute JavaScript to trigger
dynamic content loading. 2\. Wait for a specific condition (20 rows loaded)
before extraction. 3\. Extract data from the dynamically loaded content.

By mastering the `JsonCssExtractionStrategy`, you can efficiently extract
structured data from a wide variety of web pages, making it a valuable tool in
your web scraping toolkit.

For more details on schema definitions and advanced extraction strategies,
check out the[Advanced
JsonCssExtraction](../../full_details/advanced_jsoncss_extraction/).



## LLM Extraction

URL: https://crawl4ai.com/mkdocs/examples/llm_extraction/

# LLM Extraction with AsyncWebCrawler

Crawl4AI's AsyncWebCrawler allows you to use Language Models (LLMs) to extract
structured data or relevant content from web pages asynchronously. Below are
two examples demonstrating how to use `LLMExtractionStrategy` for different
purposes with the AsyncWebCrawler.

## Example 1: Extract Structured Data

In this example, we use the `LLMExtractionStrategy` to extract structured data
(model names and their fees) from the OpenAI pricing page.

    
    
    import os
    import json
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import LLMExtractionStrategy
    from pydantic import BaseModel, Field
    
    class OpenAIModelFee(BaseModel):
        model_name: str = Field(..., description="Name of the OpenAI model.")
        input_fee: str = Field(..., description="Fee for input token for the OpenAI model.")
        output_fee: str = Field(..., description="Fee for output token for the OpenAI model.")
    
    async def extract_openai_fees():
        url = 'https://openai.com/api/pricing/'
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url=url,
                word_count_threshold=1,
                extraction_strategy=LLMExtractionStrategy(
                    provider="openai/gpt-4o",
                    api_token=os.getenv('OPENAI_API_KEY'),
                    schema=OpenAIModelFee.model_json_schema(),
                    extraction_type="schema",
                    instruction="From the crawled content, extract all mentioned model names along with their "
                                "fees for input and output tokens. Make sure not to miss anything in the entire content. "
                                'One extracted model JSON format should look like this: '
                                '{ "model_name": "GPT-4", "input_fee": "US$10.00 / 1M tokens", "output_fee": "US$30.00 / 1M tokens" }'
                ),
                bypass_cache=True,
            )
    
        model_fees = json.loads(result.extracted_content)
        print(f"Number of models extracted: {len(model_fees)}")
    
        with open(".data/openai_fees.json", "w", encoding="utf-8") as f:
            json.dump(model_fees, f, indent=2)
    
    asyncio.run(extract_openai_fees())
    

## Example 2: Extract Relevant Content

In this example, we instruct the LLM to extract only content related to
technology from the NBC News business page.

    
    
    import os
    import json
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import LLMExtractionStrategy
    
    async def extract_tech_content():
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://www.nbcnews.com/business",
                extraction_strategy=LLMExtractionStrategy(
                    provider="openai/gpt-4o",
                    api_token=os.getenv('OPENAI_API_KEY'),
                    instruction="Extract only content related to technology"
                ),
                bypass_cache=True,
            )
    
        tech_content = json.loads(result.extracted_content)
        print(f"Number of tech-related items extracted: {len(tech_content)}")
    
        with open(".data/tech_content.json", "w", encoding="utf-8") as f:
            json.dump(tech_content, f, indent=2)
    
    asyncio.run(extract_tech_content())
    

## Advanced Usage: Combining JS Execution with LLM Extraction

This example demonstrates how to combine JavaScript execution with LLM
extraction to handle dynamic content:

    
    
    async def extract_dynamic_content():
        js_code = """
        const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More'));
        if (loadMoreButton) {
            loadMoreButton.click();
            await new Promise(resolve => setTimeout(resolve, 2000));
        }
        """
    
        wait_for = """
        () => {
            const articles = document.querySelectorAll('article.tease-card');
            return articles.length > 10;
        }
        """
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://www.nbcnews.com/business",
                js_code=js_code,
                wait_for=wait_for,
                css_selector="article.tease-card",
                extraction_strategy=LLMExtractionStrategy(
                    provider="openai/gpt-4o",
                    api_token=os.getenv('OPENAI_API_KEY'),
                    instruction="Summarize each article, focusing on technology-related content"
                ),
                bypass_cache=True,
            )
    
        summaries = json.loads(result.extracted_content)
        print(f"Number of summarized articles: {len(summaries)}")
    
        with open(".data/tech_summaries.json", "w", encoding="utf-8") as f:
            json.dump(summaries, f, indent=2)
    
    asyncio.run(extract_dynamic_content())
    

## Customizing LLM Provider

Crawl4AI uses the `litellm` library under the hood, which allows you to use
any LLM provider you want. Just pass the correct model name and API token:

    
    
    extraction_strategy=LLMExtractionStrategy(
        provider="your_llm_provider/model_name",
        api_token="your_api_token",
        instruction="Your extraction instruction"
    )
    

This flexibility allows you to integrate with various LLM providers and tailor
the extraction process to your specific needs.

## Error Handling and Retries

When working with external LLM APIs, it's important to handle potential errors
and implement retry logic. Here's an example of how you might do this:

    
    
    import asyncio
    from tenacity import retry, stop_after_attempt, wait_exponential
    
    class LLMExtractionError(Exception):
        pass
    
    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
    async def extract_with_retry(crawler, url, extraction_strategy):
        try:
            result = await crawler.arun(url=url, extraction_strategy=extraction_strategy, bypass_cache=True)
            return json.loads(result.extracted_content)
        except Exception as e:
            raise LLMExtractionError(f"Failed to extract content: {str(e)}")
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            try:
                content = await extract_with_retry(
                    crawler,
                    "https://www.example.com",
                    LLMExtractionStrategy(
                        provider="openai/gpt-4o",
                        api_token=os.getenv('OPENAI_API_KEY'),
                        instruction="Extract and summarize main points"
                    )
                )
                print("Extracted content:", content)
            except LLMExtractionError as e:
                print(f"Extraction failed after retries: {e}")
    
    asyncio.run(main())
    

This example uses the `tenacity` library to implement a retry mechanism with
exponential backoff, which can help handle temporary failures or rate limiting
from the LLM API.



## JS Execution & CSS Filtering

URL: https://crawl4ai.com/mkdocs/examples/js_execution_css_filtering/

# JS Execution & CSS Filtering with AsyncWebCrawler

In this example, we'll demonstrate how to use Crawl4AI's AsyncWebCrawler to
execute JavaScript, filter data with CSS selectors, and use a cosine
similarity strategy to extract relevant content. This approach is particularly
useful when you need to interact with dynamic content on web pages, such as
clicking "Load More" buttons.

## Example: Extracting Structured Data Asynchronously

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.chunking_strategy import RegexChunking
    from crawl4ai.extraction_strategy import CosineStrategy
    from crawl4ai.async_crawler_strategy import AsyncPlaywrightCrawlerStrategy
    
    async def main():
        # Define the JavaScript code to click the "Load More" button
        js_code = """
        const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More'));
        if (loadMoreButton) {
            loadMoreButton.click();
            // Wait for new content to load
            await new Promise(resolve => setTimeout(resolve, 2000));
        }
        """
    
        # Define a wait_for function to ensure content is loaded
        wait_for = """
        () => {
            const articles = document.querySelectorAll('article.tease-card');
            return articles.length > 10;
        }
        """
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            # Run the crawler with keyword filtering and CSS selector
            result = await crawler.arun(
                url="https://www.nbcnews.com/business",
                js_code=js_code,
                wait_for=wait_for,
                css_selector="article.tease-card",
                extraction_strategy=CosineStrategy(
                    semantic_filter="technology",
                ),
                chunking_strategy=RegexChunking(),
            )
    
        # Display the extracted result
        print(result.extracted_content)
    
    # Run the async function
    asyncio.run(main())
    

### Explanation

  1. **Asynchronous Execution** : We use `AsyncWebCrawler` with async/await syntax for non-blocking execution.

  2. **JavaScript Execution** : The `js_code` variable contains JavaScript code that simulates clicking a "Load More" button and waits for new content to load.

  3. **Wait Condition** : The `wait_for` function ensures that the page has loaded more than 10 articles before proceeding with the extraction.

  4. **CSS Selector** : The `css_selector="article.tease-card"` parameter ensures that only article cards are extracted from the web page.

  5. **Extraction Strategy** : The `CosineStrategy` is used with a semantic filter for "technology" to extract relevant content based on cosine similarity.

  6. **Chunking Strategy** : We use `RegexChunking()` to split the content into manageable chunks for processing.

## Advanced Usage: Custom Session and Multiple Requests

For more complex scenarios where you need to maintain state across multiple
requests or execute additional JavaScript after the initial page load, you can
use a custom session:

    
    
    async def advanced_crawl():
        async with AsyncWebCrawler(verbose=True) as crawler:
            # Initial crawl with custom session
            result1 = await crawler.arun(
                url="https://www.nbcnews.com/business",
                js_code=js_code,
                wait_for=wait_for,
                css_selector="article.tease-card",
                session_id="business_session"
            )
    
            # Execute additional JavaScript in the same session
            result2 = await crawler.crawler_strategy.execute_js(
                session_id="business_session",
                js_code="window.scrollTo(0, document.body.scrollHeight);",
                wait_for_js="() => window.innerHeight + window.scrollY >= document.body.offsetHeight"
            )
    
            # Process results
            print("Initial crawl result:", result1.extracted_content)
            print("Additional JS execution result:", result2.html)
    
    asyncio.run(advanced_crawl())
    

This advanced example demonstrates how to: 1\. Use a custom session to
maintain state across requests. 2\. Execute additional JavaScript after the
initial page load. 3\. Wait for specific conditions using JavaScript
functions.

## Try It Yourself

These examples demonstrate the power and flexibility of Crawl4AI's
AsyncWebCrawler in handling complex web interactions and extracting meaningful
data asynchronously. You can customize the JavaScript code, CSS selectors,
extraction strategies, and waiting conditions to suit your specific
requirements.



## Hooks & Auth

URL: https://crawl4ai.com/mkdocs/examples/hooks_auth/

# Hooks & Auth for AsyncWebCrawler

Crawl4AI's AsyncWebCrawler allows you to customize the behavior of the web
crawler using hooks. Hooks are asynchronous functions that are called at
specific points in the crawling process, allowing you to modify the crawler's
behavior or perform additional actions. This example demonstrates how to use
various hooks to customize the asynchronous crawling process.

## Example: Using Crawler Hooks with AsyncWebCrawler

Let's see how we can customize the AsyncWebCrawler using hooks! In this
example, we'll:

  1. Configure the browser when it's created.
  2. Add custom headers before navigating to the URL.
  3. Log the current URL after navigation.
  4. Perform actions after JavaScript execution.
  5. Log the length of the HTML before returning it.

### Hook Definitions

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.async_crawler_strategy import AsyncPlaywrightCrawlerStrategy
    from playwright.async_api import Page, Browser
    
    async def on_browser_created(browser: Browser):
        print("[HOOK] on_browser_created")
        # Example customization: set browser viewport size
        context = await browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = await context.new_page()
    
        # Example customization: logging in to a hypothetical website
        await page.goto('https://example.com/login')
        await page.fill('input[name="username"]', 'testuser')
        await page.fill('input[name="password"]', 'password123')
        await page.click('button[type="submit"]')
        await page.wait_for_selector('#welcome')
    
        # Add a custom cookie
        await context.add_cookies([{'name': 'test_cookie', 'value': 'cookie_value', 'url': 'https://example.com'}])
    
        await page.close()
        await context.close()
    
    async def before_goto(page: Page):
        print("[HOOK] before_goto")
        # Example customization: add custom headers
        await page.set_extra_http_headers({'X-Test-Header': 'test'})
    
    async def after_goto(page: Page):
        print("[HOOK] after_goto")
        # Example customization: log the URL
        print(f"Current URL: {page.url}")
    
    async def on_execution_started(page: Page):
        print("[HOOK] on_execution_started")
        # Example customization: perform actions after JS execution
        await page.evaluate("console.log('Custom JS executed')")
    
    async def before_return_html(page: Page, html: str):
        print("[HOOK] before_return_html")
        # Example customization: log the HTML length
        print(f"HTML length: {len(html)}")
        return page
    

### Using the Hooks with the AsyncWebCrawler

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.async_crawler_strategy import AsyncPlaywrightCrawlerStrategy
    
    async def main():
        print("\n🔗 Using Crawler Hooks: Let's see how we can customize the AsyncWebCrawler using hooks!")
    
        crawler_strategy = AsyncPlaywrightCrawlerStrategy(verbose=True)
        crawler_strategy.set_hook('on_browser_created', on_browser_created)
        crawler_strategy.set_hook('before_goto', before_goto)
        crawler_strategy.set_hook('after_goto', after_goto)
        crawler_strategy.set_hook('on_execution_started', on_execution_started)
        crawler_strategy.set_hook('before_return_html', before_return_html)
    
        async with AsyncWebCrawler(verbose=True, crawler_strategy=crawler_strategy) as crawler:
            result = await crawler.arun(
                url="https://example.com",
                js_code="window.scrollTo(0, document.body.scrollHeight);",
                wait_for="footer"
            )
    
        print("📦 Crawler Hooks result:")
        print(result)
    
    asyncio.run(main())
    

### Explanation

  * `on_browser_created`: This hook is called when the Playwright browser is created. It sets up the browser context, logs in to a website, and adds a custom cookie.
  * `before_goto`: This hook is called right before Playwright navigates to the URL. It adds custom HTTP headers.
  * `after_goto`: This hook is called after Playwright navigates to the URL. It logs the current URL.
  * `on_execution_started`: This hook is called after any custom JavaScript is executed. It performs additional JavaScript actions.
  * `before_return_html`: This hook is called before returning the HTML content. It logs the length of the HTML content.

### Additional Ideas

  * **Handling authentication** : Use the `on_browser_created` hook to handle login processes or set authentication tokens.
  * **Dynamic header modification** : Modify headers based on the target URL or other conditions in the `before_goto` hook.
  * **Content verification** : Use the `after_goto` hook to verify that the expected content is present on the page.
  * **Custom JavaScript injection** : Inject and execute custom JavaScript using the `on_execution_started` hook.
  * **Content preprocessing** : Modify or analyze the HTML content in the `before_return_html` hook before it's returned.

By using these hooks, you can customize the behavior of the AsyncWebCrawler to
suit your specific needs, including handling authentication, modifying
requests, and preprocessing content.



## Summarization

URL: https://crawl4ai.com/mkdocs/examples/summarization/

# Summarization Example with AsyncWebCrawler

This example demonstrates how to use Crawl4AI's `AsyncWebCrawler` to extract a
summary from a web page asynchronously. The goal is to obtain the title, a
detailed summary, a brief summary, and a list of keywords from the given page.

## Step-by-Step Guide

  1. **Import Necessary Modules**

First, import the necessary modules and classes:

`python import os import json import asyncio from crawl4ai import
AsyncWebCrawler from crawl4ai.extraction_strategy import LLMExtractionStrategy
from crawl4ai.chunking_strategy import RegexChunking from pydantic import
BaseModel, Field`

  2. **Define the URL to be Crawled**

Set the URL of the web page you want to summarize:

`python url =
'https://marketplace.visualstudio.com/items?itemName=Unclecode.groqopilot'`

  3. **Define the Data Model**

Use Pydantic to define the structure of the extracted data:

`python class PageSummary(BaseModel): title: str = Field(...,
description="Title of the page.") summary: str = Field(...,
description="Summary of the page.") brief_summary: str = Field(...,
description="Brief summary of the page.") keywords: list = Field(...,
description="Keywords assigned to the page.")`

  4. **Create the Extraction Strategy**

Set up the `LLMExtractionStrategy` with the necessary parameters:

`python extraction_strategy = LLMExtractionStrategy( provider="openai/gpt-4o",
api_token=os.getenv('OPENAI_API_KEY'), schema=PageSummary.model_json_schema(),
extraction_type="schema", apply_chunking=False, instruction=( "From the
crawled content, extract the following details: " "1. Title of the page " "2.
Summary of the page, which is a detailed summary " "3. Brief summary of the
page, which is a paragraph text " "4. Keywords assigned to the page, which is
a list of keywords. " 'The extracted JSON format should look like this: ' '{
"title": "Page Title", "summary": "Detailed summary of the page.", '
'"brief_summary": "Brief summary in a paragraph.", "keywords": ["keyword1",
"keyword2", "keyword3"] }' ) )`

  5. **Define the Async Crawl Function**

Create an asynchronous function to run the crawler:

`python async def crawl_and_summarize(url): async with
AsyncWebCrawler(verbose=True) as crawler: result = await crawler.arun(
url=url, word_count_threshold=1, extraction_strategy=extraction_strategy,
chunking_strategy=RegexChunking(), bypass_cache=True, ) return result`

  6. **Run the Crawler and Process Results**

Use asyncio to run the crawler and process the results:

```python async def main(): result = await crawl_and_summarize(url)

    
        if result.success:
        page_summary = json.loads(result.extracted_content)
        print("Extracted Page Summary:")
        print(json.dumps(page_summary, indent=2))
    
        # Save the extracted data
        with open(".data/page_summary.json", "w", encoding="utf-8") as f:
            json.dump(page_summary, f, indent=2)
        print("Page summary saved to .data/page_summary.json")
    else:
        print(f"Failed to crawl and summarize the page. Error: {result.error_message}")
    

# Run the async main function

asyncio.run(main()) ```

## Explanation

  * **Importing Modules** : We import the necessary modules, including `AsyncWebCrawler` and `LLMExtractionStrategy` from Crawl4AI.
  * **URL Definition** : We set the URL of the web page to crawl and summarize.
  * **Data Model Definition** : We define the structure of the data to extract using Pydantic's `BaseModel`.
  * **Extraction Strategy Setup** : We create an instance of `LLMExtractionStrategy` with the schema and detailed instructions for the extraction process.
  * **Async Crawl Function** : We define an asynchronous function `crawl_and_summarize` that uses `AsyncWebCrawler` to perform the crawling and extraction.
  * **Main Execution** : In the `main` function, we run the crawler, process the results, and save the extracted data.

## Advanced Usage: Crawling Multiple URLs

To demonstrate the power of `AsyncWebCrawler`, here's how you can summarize
multiple pages concurrently:

    
    
    async def crawl_multiple_urls(urls):
        async with AsyncWebCrawler(verbose=True) as crawler:
            tasks = [crawler.arun(
                url=url,
                word_count_threshold=1,
                extraction_strategy=extraction_strategy,
                chunking_strategy=RegexChunking(),
                bypass_cache=True
            ) for url in urls]
            results = await asyncio.gather(*tasks)
        return results
    
    async def main():
        urls = [
            'https://marketplace.visualstudio.com/items?itemName=Unclecode.groqopilot',
            'https://marketplace.visualstudio.com/items?itemName=GitHub.copilot',
            'https://marketplace.visualstudio.com/items?itemName=ms-python.python'
        ]
        results = await crawl_multiple_urls(urls)
    
        for i, result in enumerate(results):
            if result.success:
                page_summary = json.loads(result.extracted_content)
                print(f"\nSummary for URL {i+1}:")
                print(json.dumps(page_summary, indent=2))
            else:
                print(f"\nFailed to summarize URL {i+1}. Error: {result.error_message}")
    
    asyncio.run(main())
    

This advanced example shows how to use `AsyncWebCrawler` to efficiently
summarize multiple web pages concurrently, significantly reducing the total
processing time compared to sequential crawling.

By leveraging the asynchronous capabilities of Crawl4AI, you can perform
advanced web crawling and data extraction tasks with improved efficiency and
scalability.



## Research Assistant

URL: https://crawl4ai.com/mkdocs/examples/research_assistant/

# Research Assistant Example with AsyncWebCrawler

This example demonstrates how to build an advanced research assistant using
`Chainlit`, `Crawl4AI`'s `AsyncWebCrawler`, and various AI services. The
assistant can crawl web pages asynchronously, answer questions based on the
crawled content, and handle audio inputs.

## Step-by-Step Guide

  1. **Install Required Packages**

Ensure you have the necessary packages installed:

`bash pip install chainlit groq openai crawl4ai`

  2. **Import Libraries**

```python import os import time import asyncio from openai import AsyncOpenAI
import chainlit as cl import re from io import BytesIO from chainlit.element
import ElementBased from groq import Groq from crawl4ai import AsyncWebCrawler
from crawl4ai.extraction_strategy import NoExtractionStrategy from
crawl4ai.chunking_strategy import RegexChunking

client = AsyncOpenAI(base_url="https://api.groq.com/openai/v1",
api_key=os.getenv("GROQ_API_KEY"))

# Instrument the OpenAI client

cl.instrument_openai() ```

  3. **Set Configuration**

`python settings = { "model": "llama3-8b-8192", "temperature": 0.5,
"max_tokens": 500, "top_p": 1, "frequency_penalty": 0, "presence_penalty": 0,
}`

  4. **Define Utility Functions**

```python def extract_urls(text): url_pattern = re.compile(r'(https?://\S+)')
return url_pattern.findall(text)

async def crawl_urls(urls): async with AsyncWebCrawler(verbose=True) as
crawler: results = await crawler.arun_many( urls=urls,
word_count_threshold=10, extraction_strategy=NoExtractionStrategy(),
chunking_strategy=RegexChunking(), bypass_cache=True ) return [result.markdown
for result in results if result.success] ```

  5. **Initialize Chat Start Event**

`python @cl.on_chat_start async def on_chat_start():
cl.user_session.set("session", { "history": [], "context": {} }) await
cl.Message(content="Welcome to the chat! How can I assist you today?").send()`

  6. **Handle Incoming Messages**

```python @cl.on_message async def on_message(message: cl.Message):
user_session = cl.user_session.get("session")

    
        # Extract URLs from the user's message
    urls = extract_urls(message.content)
    
    if urls:
        crawled_contents = await crawl_urls(urls)
        for url, content in zip(urls, crawled_contents):
            ref_number = f"REF_{len(user_session['context']) + 1}"
            user_session["context"][ref_number] = {
                "url": url,
                "content": content
            }
    
    user_session["history"].append({
        "role": "user",
        "content": message.content
    })
    
    # Create a system message that includes the context
    context_messages = [
        f'<appendix ref="{ref}">\n{data["content"]}\n</appendix>'
        for ref, data in user_session["context"].items()
    ]
    system_message = {
        "role": "system",
        "content": (
            "You are a helpful bot. Use the following context for answering questions. "
            "Refer to the sources using the REF number in square brackets, e.g., [1], only if the source is given in the appendices below.\n\n"
            "If the question requires any information from the provided appendices or context, refer to the sources. "
            "If not, there is no need to add a references section. "
            "At the end of your response, provide a reference section listing the URLs and their REF numbers only if sources from the appendices were used.\n\n"
            "\n\n".join(context_messages)
        ) if context_messages else "You are a helpful assistant."
    }
    
    msg = cl.Message(content="")
    await msg.send()
    
    # Get response from the LLM
    stream = await client.chat.completions.create(
        messages=[system_message, *user_session["history"]],
        stream=True,
        **settings
    )
    
    assistant_response = ""
    async for part in stream:
        if token := part.choices[0].delta.content:
            assistant_response += token
            await msg.stream_token(token)
    
    # Add assistant message to the history
    user_session["history"].append({
        "role": "assistant",
        "content": assistant_response
    })
    await msg.update()
    
    # Append the reference section to the assistant's response
    if user_session["context"]:
        reference_section = "\n\nReferences:\n"
        for ref, data in user_session["context"].items():
            reference_section += f"[{ref.split('_')[1]}]: {data['url']}\n"
        msg.content += reference_section
        await msg.update()
    

```

  7. **Handle Audio Input**

```python @cl.on_audio_chunk async def on_audio_chunk(chunk: cl.AudioChunk):
if chunk.isStart: buffer = BytesIO() buffer.name =
f"input_audio.{chunk.mimeType.split('/')[1]}"
cl.user_session.set("audio_buffer", buffer)
cl.user_session.set("audio_mime_type", chunk.mimeType)
cl.user_session.get("audio_buffer").write(chunk.data)

@cl.step(type="tool") async def speech_to_text(audio_file): response = await
client.audio.transcriptions.create( model="whisper-large-v3", file=audio_file
) return response.text

@cl.on_audio_end async def on_audio_end(elements: list[ElementBased]):
audio_buffer: BytesIO = cl.user_session.get("audio_buffer")
audio_buffer.seek(0) audio_file = audio_buffer.read() audio_mime_type: str =
cl.user_session.get("audio_mime_type")

    
        start_time = time.time()
    transcription = await speech_to_text((audio_buffer.name, audio_file, audio_mime_type))
    end_time = time.time()
    print(f"Transcription took {end_time - start_time} seconds")
    
    user_msg = cl.Message(author="You", type="user_message", content=transcription)
    await user_msg.send()
    await on_message(user_msg)
    

```

  8. **Run the Chat Application**

`python if __name__ == "__main__": from chainlit.cli import run_chainlit
run_chainlit(__file__)`

## Explanation

  * **Libraries and Configuration** : We import necessary libraries, including `AsyncWebCrawler` from `crawl4ai`.
  * **Utility Functions** : 
  * `extract_urls`: Uses regex to find URLs in messages.
  * `crawl_urls`: An asynchronous function that uses `AsyncWebCrawler` to fetch content from multiple URLs concurrently.
  * **Chat Start Event** : Initializes the chat session and sends a welcome message.
  * **Message Handling** : 
  * Extracts URLs from user messages.
  * Asynchronously crawls the URLs using `AsyncWebCrawler`.
  * Updates chat history and context with crawled content.
  * Generates a response using the LLM, incorporating the crawled context.
  * **Audio Handling** : Captures, buffers, and transcribes audio input, then processes the transcription as text.
  * **Running the Application** : Starts the Chainlit server for interaction with the assistant.

## Key Improvements

  1. **Asynchronous Web Crawling** : Using `AsyncWebCrawler` allows for efficient, concurrent crawling of multiple URLs.
  2. **Improved Context Management** : The assistant now maintains a context of crawled content, allowing for more informed responses.
  3. **Dynamic Reference System** : The assistant can refer to specific sources in its responses and provide a reference section.
  4. **Seamless Audio Integration** : The ability to handle audio inputs makes the assistant more versatile and user-friendly.

This updated Research Assistant showcases how to create a powerful,
interactive tool that can efficiently fetch and process web content, handle
various input types, and provide informed responses based on the gathered
information.



## Crawl Request Parameters

URL: https://crawl4ai.com/mkdocs/full_details/crawl_request_parameters/

# Crawl Request Parameters for AsyncWebCrawler

The `arun` method in Crawl4AI's `AsyncWebCrawler` is designed to be highly
configurable, allowing you to customize the crawling and extraction process to
suit your needs. Below are the parameters you can use with the `arun` method,
along with their descriptions, possible values, and examples.

## Parameters

### url (str)

**Description:** The URL of the webpage to crawl. **Required:** Yes
**Example:**

    
    
    url = "https://www.nbcnews.com/business"
    

### word_count_threshold (int)

**Description:** The minimum number of words a block must contain to be
considered meaningful. The default value is defined by `MIN_WORD_THRESHOLD`.
**Required:** No **Default Value:** `MIN_WORD_THRESHOLD` **Example:**

    
    
    word_count_threshold = 10
    

### extraction_strategy (ExtractionStrategy)

**Description:** The strategy to use for extracting content from the HTML. It
must be an instance of `ExtractionStrategy`. If not provided, the default is
`NoExtractionStrategy`. **Required:** No **Default Value:**
`NoExtractionStrategy()` **Example:**

    
    
    extraction_strategy = CosineStrategy(semantic_filter="finance")
    

### chunking_strategy (ChunkingStrategy)

**Description:** The strategy to use for chunking the text before processing.
It must be an instance of `ChunkingStrategy`. The default value is
`RegexChunking()`. **Required:** No **Default Value:** `RegexChunking()`
**Example:**

    
    
    chunking_strategy = NlpSentenceChunking()
    

### bypass_cache (bool)

**Description:** Whether to force a fresh crawl even if the URL has been
previously crawled. The default value is `False`. **Required:** No **Default
Value:** `False` **Example:**

    
    
    bypass_cache = True
    

### css_selector (str)

**Description:** The CSS selector to target specific parts of the HTML for
extraction. If not provided, the entire HTML will be processed. **Required:**
No **Default Value:** `None` **Example:**

    
    
    css_selector = "div.article-content"
    

### screenshot (bool)

**Description:** Whether to take screenshots of the page. The default value is
`False`. **Required:** No **Default Value:** `False` **Example:**

    
    
    screenshot = True
    

### user_agent (str)

**Description:** The user agent to use for the HTTP requests. If not provided,
a default user agent will be used. **Required:** No **Default Value:** `None`
**Example:**

    
    
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    

### verbose (bool)

**Description:** Whether to enable verbose logging. The default value is
`True`. **Required:** No **Default Value:** `True` **Example:**

    
    
    verbose = True
    

### **kwargs

Additional keyword arguments that can be passed to customize the crawling
process further. Some notable options include:

  * **only_text (bool):** Whether to extract only text content, excluding HTML tags. Default is `False`.
  * **session_id (str):** A unique identifier for the crawling session. This is useful for maintaining state across multiple requests.
  * **js_code (str or list):** JavaScript code to be executed on the page before extraction.
  * **wait_for (str):** A CSS selector or JavaScript function to wait for before considering the page load complete.

**Example:**

    
    
    result = await crawler.arun(
        url="https://www.nbcnews.com/business",
        css_selector="p",
        only_text=True,
        session_id="unique_session_123",
        js_code="window.scrollTo(0, document.body.scrollHeight);",
        wait_for="article.main-article"
    )
    

## Example Usage

Here's an example of how to use the `arun` method with various parameters:

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import CosineStrategy
    from crawl4ai.chunking_strategy import NlpSentenceChunking
    
    async def main():
        # Create the AsyncWebCrawler instance 
        async with AsyncWebCrawler(verbose=True) as crawler:
            # Run the crawler with custom parameters
            result = await crawler.arun(
                url="https://www.nbcnews.com/business",
                word_count_threshold=10,
                extraction_strategy=CosineStrategy(semantic_filter="finance"),
                chunking_strategy=NlpSentenceChunking(),
                bypass_cache=True,
                css_selector="div.article-content",
                screenshot=True,
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                verbose=True,
                only_text=True,
                session_id="business_news_session",
                js_code="window.scrollTo(0, document.body.scrollHeight);",
                wait_for="footer"
            )
    
            print(result)
    
    # Run the async function
    asyncio.run(main())
    

This example demonstrates how to configure various parameters to customize the
crawling and extraction process using the asynchronous version of Crawl4AI.

## Additional Asynchronous Methods

The `AsyncWebCrawler` class also provides other useful asynchronous methods:

### arun_many

**Description:** Crawl multiple URLs concurrently. **Example:**

    
    
    urls = ["https://example1.com", "https://example2.com", "https://example3.com"]
    results = await crawler.arun_many(urls, word_count_threshold=10, bypass_cache=True)
    

### aclear_cache

**Description:** Clear the crawler's cache. **Example:**

    
    
    await crawler.aclear_cache()
    

### aflush_cache

**Description:** Completely flush the crawler's cache. **Example:**

    
    
    await crawler.aflush_cache()
    

### aget_cache_size

**Description:** Get the current size of the cache. **Example:**

    
    
    cache_size = await crawler.aget_cache_size()
    print(f"Current cache size: {cache_size}")
    

These asynchronous methods allow for efficient and flexible use of the
AsyncWebCrawler in various scenarios.



## Crawl Result Class

URL: https://crawl4ai.com/mkdocs/full_details/crawl_result_class/

# Crawl Result

The `CrawlResult` class is the heart of Crawl4AI's output, encapsulating all
the data extracted from a crawling session. This class contains various fields
that store the results of the web crawling and extraction process. Let's break
down each field and see what it holds. 🎉

## Class Definition

    
    
    from pydantic import BaseModel
    from typing import Dict, List, Optional
    
    class CrawlResult(BaseModel):
        url: str
        html: str
        success: bool
        cleaned_html: Optional[str] = None
        media: Dict[str, List[Dict]] = {}
        links: Dict[str, List[Dict]] = {}
        screenshot: Optional[str] = None
        markdown: Optional[str] = None
        extracted_content: Optional[str] = None
        metadata: Optional[dict] = None
        error_message: Optional[str] = None
        session_id: Optional[str] = None
        responser_headers: Optional[dict] = None
        status_code: Optional[int] = None
    

## Fields Explanation

### `url: str`

The URL that was crawled. This field simply stores the URL of the web page
that was processed.

### `html: str`

The raw HTML content of the web page. This is the unprocessed HTML source as
retrieved by the crawler.

### `success: bool`

A flag indicating whether the crawling and extraction were successful. If any
error occurs during the process, this will be `False`.

### `cleaned_html: Optional[str]`

The cleaned HTML content of the web page. This field holds the HTML after
removing unwanted tags like `<script>`, `<style>`, and others that do not
contribute to the useful content.

### `media: Dict[str, List[Dict]]`

A dictionary containing lists of extracted media elements from the web page.
The media elements are categorized into images, videos, and audios. Here's how
they are structured:

  * **Images** : Each image is represented as a dictionary with `src` (source URL) and `alt` (alternate text).
  * **Videos** : Each video is represented similarly with `src` and `alt`.
  * **Audios** : Each audio is represented with `src` and `alt`.

    
    
    media = {
        'images': [
            {'src': 'image_url1', 'alt': 'description1', "type": "image"},
            {'src': 'image_url2', 'alt': 'description2', "type": "image"}
        ],
        'videos': [
            {'src': 'video_url1', 'alt': 'description1', "type": "video"}
        ],
        'audios': [
            {'src': 'audio_url1', 'alt': 'description1', "type": "audio"}
        ]
    }
    

### `links: Dict[str, List[Dict]]`

A dictionary containing lists of internal and external links extracted from
the web page. Each link is represented as a dictionary with `href` (URL) and
`text` (link text).

  * **Internal Links** : Links pointing to the same domain.
  * **External Links** : Links pointing to different domains.

    
    
    links = {
        'internal': [
            {'href': 'internal_link1', 'text': 'link_text1'},
            {'href': 'internal_link2', 'text': 'link_text2'}
        ],
        'external': [
            {'href': 'external_link1', 'text': 'link_text1'}
        ]
    }
    

### `screenshot: Optional[str]`

A base64-encoded screenshot of the web page. This field stores the screenshot
data if the crawling was configured to take a screenshot.

### `markdown: Optional[str]`

The content of the web page converted to Markdown format. This is useful for
generating clean, readable text that retains the structure of the original
HTML.

### `extracted_content: Optional[str]`

The content extracted based on the specified extraction strategy. This field
holds the meaningful content blocks extracted from the web page, ready for
your AI and data processing needs.

### `metadata: Optional[dict]`

A dictionary containing metadata extracted from the web page, such as title,
description, keywords, and other meta tags.

### `error_message: Optional[str]`

If an error occurs during crawling, this field will contain the error message,
helping you debug and understand what went wrong. 🚨

### `session_id: Optional[str]`

A unique identifier for the crawling session. This can be useful for tracking
and managing multiple crawling sessions.

### `responser_headers: Optional[dict]`

A dictionary containing the response headers from the web server. This can
provide additional information about the server and the response.

### `status_code: Optional[int]`

The HTTP status code of the response. This indicates the success or failure of
the HTTP request (e.g., 200 for success, 404 for not found, etc.).



## Session Based Crawling

URL: https://crawl4ai.com/mkdocs/full_details/session_based_crawling/

# Session-Based Crawling for Dynamic Content

In modern web applications, content is often loaded dynamically without
changing the URL. Examples include "Load More" buttons, infinite scrolling, or
paginated content that updates via JavaScript. To effectively crawl such
websites, Crawl4AI provides powerful session-based crawling capabilities.

This guide will explore advanced techniques for crawling dynamic content using
Crawl4AI's session management features.

## Understanding Session-Based Crawling

Session-based crawling allows you to maintain a persistent browser session
across multiple requests. This is crucial when:

  1. The content changes dynamically without URL changes
  2. You need to interact with the page (e.g., clicking buttons) between requests
  3. The site requires authentication or maintains state across pages

Crawl4AI's `AsyncWebCrawler` class supports session-based crawling through the
`session_id` parameter and related methods.

## Basic Concepts

Before diving into examples, let's review some key concepts:

  * **Session ID** : A unique identifier for a browsing session. Use the same `session_id` across multiple `arun` calls to maintain state.
  * **JavaScript Execution** : Use the `js_code` parameter to execute JavaScript on the page, such as clicking a "Load More" button.
  * **CSS Selectors** : Use these to target specific elements for extraction or interaction.
  * **Extraction Strategy** : Define how to extract structured data from the page.
  * **Wait Conditions** : Specify conditions to wait for before considering the page loaded.

## Example 1: Basic Session-Based Crawling

Let's start with a basic example of session-based crawling:

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    
    async def basic_session_crawl():
        async with AsyncWebCrawler(verbose=True) as crawler:
            session_id = "my_session"
            url = "https://example.com/dynamic-content"
    
            for page in range(3):
                result = await crawler.arun(
                    url=url,
                    session_id=session_id,
                    js_code="document.querySelector('.load-more-button').click();" if page > 0 else None,
                    css_selector=".content-item",
                    bypass_cache=True
                )
    
                print(f"Page {page + 1}: Found {result.extracted_content.count('.content-item')} items")
    
            await crawler.crawler_strategy.kill_session(session_id)
    
    asyncio.run(basic_session_crawl())
    

This example demonstrates: 1\. Using a consistent `session_id` across multiple
`arun` calls 2\. Executing JavaScript to load more content after the first
page 3\. Using a CSS selector to extract specific content 4\. Properly closing
the session after crawling

## Advanced Technique 1: Custom Execution Hooks

Crawl4AI allows you to set custom hooks that execute at different stages of
the crawling process. This is particularly useful for handling complex loading
scenarios.

Here's an example that waits for new content to appear before proceeding:

    
    
    async def advanced_session_crawl_with_hooks():
        first_commit = ""
    
        async def on_execution_started(page):
            nonlocal first_commit
            try:
                while True:
                    await page.wait_for_selector("li.commit-item h4")
                    commit = await page.query_selector("li.commit-item h4")
                    commit = await commit.evaluate("(element) => element.textContent")
                    commit = commit.strip()
                    if commit and commit != first_commit:
                        first_commit = commit
                        break
                    await asyncio.sleep(0.5)
            except Exception as e:
                print(f"Warning: New content didn't appear after JavaScript execution: {e}")
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            crawler.crawler_strategy.set_hook("on_execution_started", on_execution_started)
    
            url = "https://github.com/example/repo/commits/main"
            session_id = "commit_session"
            all_commits = []
    
            js_next_page = """
            const button = document.querySelector('a.pagination-next');
            if (button) button.click();
            """
    
            for page in range(3):
                result = await crawler.arun(
                    url=url,
                    session_id=session_id,
                    css_selector="li.commit-item",
                    js_code=js_next_page if page > 0 else None,
                    bypass_cache=True,
                    js_only=page > 0
                )
    
                commits = result.extracted_content.select("li.commit-item")
                all_commits.extend(commits)
                print(f"Page {page + 1}: Found {len(commits)} commits")
    
            await crawler.crawler_strategy.kill_session(session_id)
            print(f"Successfully crawled {len(all_commits)} commits across 3 pages")
    
    asyncio.run(advanced_session_crawl_with_hooks())
    

This technique uses a custom `on_execution_started` hook to ensure new content
has loaded before proceeding to the next step.

## Advanced Technique 2: Integrated JavaScript Execution and Waiting

Instead of using separate hooks, you can integrate the waiting logic directly
into your JavaScript execution. This approach can be more concise and easier
to manage for some scenarios.

Here's an example:

    
    
    async def integrated_js_and_wait_crawl():
        async with AsyncWebCrawler(verbose=True) as crawler:
            url = "https://github.com/example/repo/commits/main"
            session_id = "integrated_session"
            all_commits = []
    
            js_next_page_and_wait = """
            (async () => {
                const getCurrentCommit = () => {
                    const commits = document.querySelectorAll('li.commit-item h4');
                    return commits.length > 0 ? commits[0].textContent.trim() : null;
                };
    
                const initialCommit = getCurrentCommit();
                const button = document.querySelector('a.pagination-next');
                if (button) button.click();
    
                while (true) {
                    await new Promise(resolve => setTimeout(resolve, 100));
                    const newCommit = getCurrentCommit();
                    if (newCommit && newCommit !== initialCommit) {
                        break;
                    }
                }
            })();
            """
    
            schema = {
                "name": "Commit Extractor",
                "baseSelector": "li.commit-item",
                "fields": [
                    {
                        "name": "title",
                        "selector": "h4.commit-title",
                        "type": "text",
                        "transform": "strip",
                    },
                ],
            }
            extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
            for page in range(3):
                result = await crawler.arun(
                    url=url,
                    session_id=session_id,
                    css_selector="li.commit-item",
                    extraction_strategy=extraction_strategy,
                    js_code=js_next_page_and_wait if page > 0 else None,
                    js_only=page > 0,
                    bypass_cache=True
                )
    
                commits = json.loads(result.extracted_content)
                all_commits.extend(commits)
                print(f"Page {page + 1}: Found {len(commits)} commits")
    
            await crawler.crawler_strategy.kill_session(session_id)
            print(f"Successfully crawled {len(all_commits)} commits across 3 pages")
    
    asyncio.run(integrated_js_and_wait_crawl())
    

This approach combines the JavaScript for clicking the "next" button and
waiting for new content to load into a single script.

## Advanced Technique 3: Using the `wait_for` Parameter

Crawl4AI provides a `wait_for` parameter that allows you to specify a
condition to wait for before considering the page fully loaded. This can be
particularly useful for dynamic content.

Here's an example:

    
    
    async def wait_for_parameter_crawl():
        async with AsyncWebCrawler(verbose=True) as crawler:
            url = "https://github.com/example/repo/commits/main"
            session_id = "wait_for_session"
            all_commits = []
    
            js_next_page = """
            const commits = document.querySelectorAll('li.commit-item h4');
            if (commits.length > 0) {
                window.lastCommit = commits[0].textContent.trim();
            }
            const button = document.querySelector('a.pagination-next');
            if (button) button.click();
            """
    
            wait_for = """() => {
                const commits = document.querySelectorAll('li.commit-item h4');
                if (commits.length === 0) return false;
                const firstCommit = commits[0].textContent.trim();
                return firstCommit !== window.lastCommit;
            }"""
    
            schema = {
                "name": "Commit Extractor",
                "baseSelector": "li.commit-item",
                "fields": [
                    {
                        "name": "title",
                        "selector": "h4.commit-title",
                        "type": "text",
                        "transform": "strip",
                    },
                ],
            }
            extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
            for page in range(3):
                result = await crawler.arun(
                    url=url,
                    session_id=session_id,
                    css_selector="li.commit-item",
                    extraction_strategy=extraction_strategy,
                    js_code=js_next_page if page > 0 else None,
                    wait_for=wait_for if page > 0 else None,
                    js_only=page > 0,
                    bypass_cache=True
                )
    
                commits = json.loads(result.extracted_content)
                all_commits.extend(commits)
                print(f"Page {page + 1}: Found {len(commits)} commits")
    
            await crawler.crawler_strategy.kill_session(session_id)
            print(f"Successfully crawled {len(all_commits)} commits across 3 pages")
    
    asyncio.run(wait_for_parameter_crawl())
    

This technique separates the JavaScript execution (clicking the "next" button)
from the waiting condition, providing more flexibility and clarity in some
scenarios.

## Best Practices for Session-Based Crawling

  1. **Use Unique Session IDs** : Ensure each crawling session has a unique `session_id` to prevent conflicts.
  2. **Close Sessions** : Always close sessions using `kill_session` when you're done to free up resources.
  3. **Handle Errors** : Implement proper error handling to deal with unexpected situations during crawling.
  4. **Respect Website Terms** : Ensure your crawling adheres to the website's terms of service and robots.txt file.
  5. **Implement Delays** : Add appropriate delays between requests to avoid overwhelming the target server.
  6. **Use Extraction Strategies** : Leverage `JsonCssExtractionStrategy` or other extraction strategies for structured data extraction.
  7. **Optimize JavaScript** : Keep your JavaScript execution concise and efficient to improve crawling speed.
  8. **Monitor Performance** : Keep an eye on memory usage and crawling speed, especially for long-running sessions.

## Conclusion

Session-based crawling with Crawl4AI provides powerful capabilities for
handling dynamic content and complex web applications. By leveraging session
management, JavaScript execution, and waiting strategies, you can effectively
crawl and extract data from a wide range of modern websites.

Remember to use these techniques responsibly and in compliance with website
policies and ethical web scraping practices.

For more advanced usage and API details, refer to the Crawl4AI API
documentation.



## Advanced Features

URL: https://crawl4ai.com/mkdocs/full_details/advanced_features/

# Advanced Features

Crawl4AI offers a range of advanced features that allow you to fine-tune your
web crawling and data extraction process. This section will cover some of
these advanced features, including taking screenshots, extracting media and
links, customizing the user agent, using custom hooks, and leveraging CSS
selectors.

## Taking Screenshots 📸

One of the cool features of Crawl4AI is the ability to take screenshots of the
web pages you're crawling. This can be particularly useful for visual
verification or for capturing the state of dynamic content.

Here's how you can take a screenshot:

    
    
    from crawl4ai import WebCrawler
    import base64
    
    # Create the WebCrawler instance
    crawler = WebCrawler()
    crawler.warmup()
    
    # Run the crawler with the screenshot parameter
    result = crawler.run(url="https://www.nbcnews.com/business", screenshot=True)
    
    # Save the screenshot to a file
    with open("screenshot.png", "wb") as f:
        f.write(base64.b64decode(result.screenshot))
    
    print("Screenshot saved to 'screenshot.png'!")
    

In this example, we create a `WebCrawler` instance, warm it up, and then run
it with the `screenshot` parameter set to `True`. The screenshot is saved as a
base64 encoded string in the result, which we then decode and save as a PNG
file.

## Extracting Media and Links 🎨🔗

Crawl4AI can extract all media tags (images, audio, and video) and links (both
internal and external) from a web page. This feature is useful for collecting
multimedia content or analyzing link structures.

Here's an example:

    
    
    from crawl4ai import WebCrawler
    
    # Create the WebCrawler instance
    crawler = WebCrawler()
    crawler.warmup()
    
    # Run the crawler
    result = crawler.run(url="https://www.nbcnews.com/business")
    
    print("Extracted media:", result.media)
    print("Extracted links:", result.links)
    

In this example, the `result` object contains dictionaries for media and
links, which you can access and use as needed.

## Customizing the User Agent 🕵️‍♂️

Crawl4AI allows you to set a custom user agent for your HTTP requests. This
can help you avoid detection by web servers or simulate different browsing
environments.

Here's how to set a custom user agent:

    
    
    from crawl4ai import WebCrawler
    
    # Create the WebCrawler instance
    crawler = WebCrawler()
    crawler.warmup()
    
    # Run the crawler with a custom user agent
    result = crawler.run(url="https://www.nbcnews.com/business", user_agent="Mozilla/5.0 (compatible; MyCrawler/1.0)")
    
    print("Crawl result:", result)
    

In this example, we specify a custom user agent string when running the
crawler.

## Using Custom Hooks 🪝

Hooks are a powerful feature in Crawl4AI that allow you to customize the
crawling process at various stages. You can define hooks for actions such as
driver initialization, before and after URL fetching, and before returning the
HTML.

Here's an example of using hooks:

    
    
    from crawl4ai import WebCrawler
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    # Define the hooks
    def on_driver_created(driver):
        driver.maximize_window()
        driver.get('https://example.com/login')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys('testuser')
        driver.find_element(By.NAME, 'password').send_keys('password123')
        driver.find_element(By.NAME, 'login').click()
        return driver
    
    def before_get_url(driver):
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'X-Test-Header': 'test'}})
        return driver
    
    # Create the WebCrawler instance
    crawler = WebCrawler()
    crawler.warmup()
    
    # Set the hooks
    crawler.set_hook('on_driver_created', on_driver_created)
    crawler.set_hook('before_get_url', before_get_url)
    
    # Run the crawler
    result = crawler.run(url="https://example.com")
    
    print("Crawl result:", result)
    

In this example, we define hooks to handle driver initialization and custom
headers before fetching the URL.

## Using CSS Selectors 🎯

CSS selectors allow you to target specific elements on a web page for
extraction. This can be useful for scraping structured content, such as
articles or product details.

Here's an example of using a CSS selector:

    
    
    from crawl4ai import WebCrawler
    
    # Create the WebCrawler instance
    crawler = WebCrawler()
    crawler.warmup()
    
    # Run the crawler with a CSS selector to extract only H2 tags
    result = crawler.run(url="https://www.nbcnews.com/business", css_selector="h2")
    
    print("Extracted H2 tags:", result.extracted_content)
    

In this example, we use the `css_selector` parameter to extract only the H2
tags from the web page.

* * *

With these advanced features, you can leverage Crawl4AI to perform
sophisticated web crawling and data extraction tasks. Whether you need to take
screenshots, extract specific elements, customize the crawling process, or set
custom headers, Crawl4AI provides the flexibility and power to meet your
needs. Happy crawling! 🕷️🚀



## Advanced JsonCssExtraction

URL: https://crawl4ai.com/mkdocs/full_details/advanced_jsoncss_extraction/

# Advanced Usage of JsonCssExtractionStrategy

While the basic usage of JsonCssExtractionStrategy is powerful for simple
structures, its true potential shines when dealing with complex, nested HTML
structures. This section will explore advanced usage scenarios, demonstrating
how to extract nested objects, lists, and nested lists.

## Hypothetical Website Example

Let's consider a hypothetical e-commerce website that displays product
categories, each containing multiple products. Each product has details,
reviews, and related items. This complex structure will allow us to
demonstrate various advanced features of JsonCssExtractionStrategy.

Assume the HTML structure looks something like this:

    
    
    <div class="category">
      <h2 class="category-name">Electronics</h2>
      <div class="product">
        <h3 class="product-name">Smartphone X</h3>
        <p class="product-price">$999</p>
        <div class="product-details">
          <span class="brand">TechCorp</span>
          <span class="model">X-2000</span>
        </div>
        <ul class="product-features">
          <li>5G capable</li>
          <li>6.5" OLED screen</li>
          <li>128GB storage</li>
        </ul>
        <div class="product-reviews">
          <div class="review">
            <span class="reviewer">John D.</span>
            <span class="rating">4.5</span>
            <p class="review-text">Great phone, love the camera!</p>
          </div>
          <div class="review">
            <span class="reviewer">Jane S.</span>
            <span class="rating">5</span>
            <p class="review-text">Best smartphone I've ever owned.</p>
          </div>
        </div>
        <ul class="related-products">
          <li>
            <span class="related-name">Phone Case</span>
            <span class="related-price">$29.99</span>
          </li>
          <li>
            <span class="related-name">Screen Protector</span>
            <span class="related-price">$9.99</span>
          </li>
        </ul>
      </div>
      <!-- More products... -->
    </div>
    

Now, let's create a schema to extract this complex structure:

    
    
    schema = {
        "name": "E-commerce Product Catalog",
        "baseSelector": "div.category",
        "fields": [
            {
                "name": "category_name",
                "selector": "h2.category-name",
                "type": "text"
            },
            {
                "name": "products",
                "selector": "div.product",
                "type": "nested_list",
                "fields": [
                    {
                        "name": "name",
                        "selector": "h3.product-name",
                        "type": "text"
                    },
                    {
                        "name": "price",
                        "selector": "p.product-price",
                        "type": "text"
                    },
                    {
                        "name": "details",
                        "selector": "div.product-details",
                        "type": "nested",
                        "fields": [
                            {
                                "name": "brand",
                                "selector": "span.brand",
                                "type": "text"
                            },
                            {
                                "name": "model",
                                "selector": "span.model",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "name": "features",
                        "selector": "ul.product-features li",
                        "type": "list",
                        "fields": [
                            {
                                "name": "feature",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "name": "reviews",
                        "selector": "div.review",
                        "type": "nested_list",
                        "fields": [
                            {
                                "name": "reviewer",
                                "selector": "span.reviewer",
                                "type": "text"
                            },
                            {
                                "name": "rating",
                                "selector": "span.rating",
                                "type": "text"
                            },
                            {
                                "name": "comment",
                                "selector": "p.review-text",
                                "type": "text"
                            }
                        ]
                    },
                    {
                        "name": "related_products",
                        "selector": "ul.related-products li",
                        "type": "list",
                        "fields": [
                            {
                                "name": "name",
                                "selector": "span.related-name",
                                "type": "text"
                            },
                            {
                                "name": "price",
                                "selector": "span.related-price",
                                "type": "text"
                            }
                        ]
                    }
                ]
            }
        ]
    }
    

This schema demonstrates several advanced features:

  1. **Nested Objects** : The `details` field is a nested object within each product.
  2. **Simple Lists** : The `features` field is a simple list of text items.
  3. **Nested Lists** : The `products` field is a nested list, where each item is a complex object.
  4. **Lists of Objects** : The `reviews` and `related_products` fields are lists of objects.

Let's break down the key concepts:

### Nested Objects

To create a nested object, use `"type": "nested"` and provide a `fields` array
for the nested structure:

    
    
    {
        "name": "details",
        "selector": "div.product-details",
        "type": "nested",
        "fields": [
            {
                "name": "brand",
                "selector": "span.brand",
                "type": "text"
            },
            {
                "name": "model",
                "selector": "span.model",
                "type": "text"
            }
        ]
    }
    

### Simple Lists

For a simple list of identical items, use `"type": "list"`:

    
    
    {
        "name": "features",
        "selector": "ul.product-features li",
        "type": "list",
        "fields": [
            {
                "name": "feature",
                "type": "text"
            }
        ]
    }
    

### Nested Lists

For a list of complex objects, use `"type": "nested_list"`:

    
    
    {
        "name": "products",
        "selector": "div.product",
        "type": "nested_list",
        "fields": [
            // ... fields for each product
        ]
    }
    

### Lists of Objects

Similar to nested lists, but typically used for simpler objects within the
list:

    
    
    {
        "name": "related_products",
        "selector": "ul.related-products li",
        "type": "list",
        "fields": [
            {
                "name": "name",
                "selector": "span.related-name",
                "type": "text"
            },
            {
                "name": "price",
                "selector": "span.related-price",
                "type": "text"
            }
        ]
    }
    

## Using the Advanced Schema

To use this advanced schema with AsyncWebCrawler:

    
    
    import json
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
    
    async def extract_complex_product_data():
        extraction_strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
        async with AsyncWebCrawler(verbose=True) as crawler:
            result = await crawler.arun(
                url="https://gist.githubusercontent.com/githubusercontent/2d7b8ba3cd8ab6cf3c8da771ddb36878/raw/1ae2f90c6861ce7dd84cc50d3df9920dee5e1fd2/sample_ecommerce.html",
                extraction_strategy=extraction_strategy,
                bypass_cache=True,
            )
    
            assert result.success, "Failed to crawl the page"
    
            product_data = json.loads(result.extracted_content)
            print(json.dumps(product_data, indent=2))
    
    asyncio.run(extract_complex_product_data())
    

This will produce a structured JSON output that captures the complex hierarchy
of the product catalog, including nested objects, lists, and nested lists.

## Tips for Advanced Usage

  1. **Start Simple** : Begin with a basic schema and gradually add complexity.
  2. **Test Incrementally** : Test each part of your schema separately before combining them.
  3. **Use Chrome DevTools** : The Element Inspector is invaluable for identifying the correct selectors.
  4. **Handle Missing Data** : Use the `default` key in your field definitions to handle cases where data might be missing.
  5. **Leverage Transforms** : Use the `transform` key to clean or format extracted data (e.g., converting prices to numbers).
  6. **Consider Performance** : Very complex schemas might slow down extraction. Balance complexity with performance needs.

By mastering these advanced techniques, you can use JsonCssExtractionStrategy
to extract highly structured data from even the most complex web pages, making
it a powerful tool for web scraping and data analysis tasks.



## Chunking Strategies

URL: https://crawl4ai.com/mkdocs/full_details/chunking_strategies/

## Chunking Strategies 📚

Crawl4AI provides several powerful chunking strategies to divide text into
manageable parts for further processing. Each strategy has unique
characteristics and is suitable for different scenarios. Let's explore them
one by one.

### RegexChunking

`RegexChunking` splits text using regular expressions. This is ideal for
creating chunks based on specific patterns like paragraphs or sentences.

#### When to Use

  * Great for structured text with consistent delimiters.
  * Suitable for documents where specific patterns (e.g., double newlines, periods) indicate logical chunks.

#### Parameters

  * `patterns` (list, optional): Regular expressions used to split the text. Default is to split by double newlines (`['\n\n']`).

#### Example

    
    
    from crawl4ai.chunking_strategy import RegexChunking
    
    # Define patterns for splitting text
    patterns = [r'\n\n', r'\. ']
    chunker = RegexChunking(patterns=patterns)
    
    # Sample text
    text = "This is a sample text. It will be split into chunks.\n\nThis is another paragraph."
    
    # Chunk the text
    chunks = chunker.chunk(text)
    print(chunks)
    

### NlpSentenceChunking

`NlpSentenceChunking` uses NLP models to split text into sentences, ensuring
accurate sentence boundaries.

#### When to Use

  * Ideal for texts where sentence boundaries are crucial.
  * Useful for creating chunks that preserve grammatical structures.

#### Parameters

  * None.

#### Example

    
    
    from crawl4ai.chunking_strategy import NlpSentenceChunking
    
    chunker = NlpSentenceChunking()
    
    # Sample text
    text = "This is a sample text. It will be split into sentences. Here's another sentence."
    
    # Chunk the text
    chunks = chunker.chunk(text)
    print(chunks)
    

### TopicSegmentationChunking

`TopicSegmentationChunking` employs the TextTiling algorithm to segment text
into topic-based chunks. This method identifies thematic boundaries.

#### When to Use

  * Perfect for long documents with distinct topics.
  * Useful when preserving topic continuity is more important than maintaining text order.

#### Parameters

  * `num_keywords` (int, optional): Number of keywords for each topic segment. Default is `3`.

#### Example

    
    
    from crawl4ai.chunking_strategy import TopicSegmentationChunking
    
    chunker = TopicSegmentationChunking(num_keywords=3)
    
    # Sample text
    text = "This document contains several topics. Topic one discusses AI. Topic two covers machine learning."
    
    # Chunk the text
    chunks = chunker.chunk(text)
    print(chunks)
    

### FixedLengthWordChunking

`FixedLengthWordChunking` splits text into chunks based on a fixed number of
words. This ensures each chunk has approximately the same length.

#### When to Use

  * Suitable for processing large texts where uniform chunk size is important.
  * Useful when the number of words per chunk needs to be controlled.

#### Parameters

  * `chunk_size` (int, optional): Number of words per chunk. Default is `100`.

#### Example

    
    
    from crawl4ai.chunking_strategy import FixedLengthWordChunking
    
    chunker = FixedLengthWordChunking(chunk_size=10)
    
    # Sample text
    text = "This is a sample text. It will be split into chunks of fixed length."
    
    # Chunk the text
    chunks = chunker.chunk(text)
    print(chunks)
    

### SlidingWindowChunking

`SlidingWindowChunking` uses a sliding window approach to create overlapping
chunks. Each chunk has a fixed length, and the window slides by a specified
step size.

#### When to Use

  * Ideal for creating overlapping chunks to preserve context.
  * Useful for tasks where context from adjacent chunks is needed.

#### Parameters

  * `window_size` (int, optional): Number of words in each chunk. Default is `100`.
  * `step` (int, optional): Number of words to slide the window. Default is `50`.

#### Example

    
    
    from crawl4ai.chunking_strategy import SlidingWindowChunking
    
    chunker = SlidingWindowChunking(window_size=10, step=5)
    
    # Sample text
    text = "This is a sample text. It will be split using a sliding window approach to preserve context."
    
    # Chunk the text
    chunks = chunker.chunk(text)
    print(chunks)
    

With these chunking strategies, you can choose the best method to divide your
text based on your specific needs. Whether you need precise sentence
boundaries, topic-based segmentation, or uniform chunk sizes, Crawl4AI has you
covered. Happy chunking! 📝✨



## Extraction Strategies

URL: https://crawl4ai.com/mkdocs/full_details/extraction_strategies/

## Extraction Strategies 🧠

Crawl4AI offers powerful extraction strategies to derive meaningful
information from web content. Let's dive into three of the most important
strategies: `CosineStrategy`, `LLMExtractionStrategy`, and the new
`JsonCssExtractionStrategy`.

### LLMExtractionStrategy

`LLMExtractionStrategy` leverages a Language Model (LLM) to extract meaningful
content from HTML. This strategy uses an external provider for LLM completions
to perform extraction based on instructions.

#### When to Use

  * Suitable for complex extraction tasks requiring nuanced understanding.
  * Ideal for scenarios where detailed instructions can guide the extraction process.
  * Perfect for extracting specific types of information or content with precise guidelines.

#### Parameters

  * `provider` (str, optional): Provider for language model completions (e.g., openai/gpt-4). Default is `DEFAULT_PROVIDER`.
  * `api_token` (str, optional): API token for the provider. If not provided, it will try to load from the environment variable `OPENAI_API_KEY`.
  * `instruction` (str, optional): Instructions to guide the LLM on how to perform the extraction. Default is `None`.

#### Example Without Instructions

    
    
    import asyncio
    import os
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import LLMExtractionStrategy
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            # Define extraction strategy without instructions
            strategy = LLMExtractionStrategy(
                provider='openai',
                api_token=os.getenv('OPENAI_API_KEY')
            )
    
            # Sample URL
            url = "https://www.nbcnews.com/business"
    
            # Run the crawler with the extraction strategy
            result = await crawler.arun(url=url, extraction_strategy=strategy)
            print(result.extracted_content)
    
    asyncio.run(main())
    

#### Example With Instructions

    
    
    import asyncio
    import os
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import LLMExtractionStrategy
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            # Define extraction strategy with instructions
            strategy = LLMExtractionStrategy(
                provider='openai',
                api_token=os.getenv('OPENAI_API_KEY'),
                instruction="Extract only financial news and summarize key points."
            )
    
            # Sample URL
            url = "https://www.nbcnews.com/business"
    
            # Run the crawler with the extraction strategy
            result = await crawler.arun(url=url, extraction_strategy=strategy)
            print(result.extracted_content)
    
    asyncio.run(main())
    

### JsonCssExtractionStrategy

`JsonCssExtractionStrategy` is a powerful tool for extracting structured data
from HTML using CSS selectors. It allows you to define a schema that maps CSS
selectors to specific fields, enabling precise and efficient data extraction.

#### When to Use

  * Ideal for extracting structured data from websites with consistent HTML structures.
  * Perfect for scenarios where you need to extract specific elements or attributes from a webpage.
  * Suitable for creating datasets from web pages with tabular or list-based information.

#### Parameters

  * `schema` (Dict[str, Any]): A dictionary defining the extraction schema, including base selector and field definitions.

#### Example

    
    
    import asyncio
    import json
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            # Define the extraction schema
            schema = {
                "name": "News Articles",
                "baseSelector": "article.tease-card",
                "fields": [
                    {
                        "name": "title",
                        "selector": "h2",
                        "type": "text",
                    },
                    {
                        "name": "summary",
                        "selector": "div.tease-card__info",
                        "type": "text",
                    },
                    {
                        "name": "link",
                        "selector": "a",
                        "type": "attribute",
                        "attribute": "href"
                    }
                ],
            }
    
            # Create the extraction strategy
            strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
            # Sample URL
            url = "https://www.nbcnews.com/business"
    
            # Run the crawler with the extraction strategy
            result = await crawler.arun(url=url, extraction_strategy=strategy)
    
            # Parse and print the extracted content
            extracted_data = json.loads(result.extracted_content)
            print(json.dumps(extracted_data, indent=2))
    
    asyncio.run(main())
    

#### Use Cases for JsonCssExtractionStrategy

  * Extracting product information from e-commerce websites.
  * Gathering news articles and their metadata from news portals.
  * Collecting user reviews and ratings from review websites.
  * Extracting job listings from job boards.

By choosing the right extraction strategy, you can effectively extract the
most relevant and useful information from web content. Whether you need fast,
accurate semantic segmentation with `CosineStrategy`, nuanced, instruction-
based extraction with `LLMExtractionStrategy`, or precise structured data
extraction with `JsonCssExtractionStrategy`, Crawl4AI has you covered. Happy
extracting! 🕵️‍♂️✨

For more details on schema definitions and advanced extraction strategies,
check out the[Advanced JsonCssExtraction](../advanced_jsoncss_extraction/).

### CosineStrategy

`CosineStrategy` uses hierarchical clustering based on cosine similarity to
group text chunks into meaningful clusters. This method converts each chunk
into its embedding and then clusters them to form semantical chunks.

#### When to Use

  * Ideal for fast, accurate semantic segmentation of text.
  * Perfect for scenarios where LLMs might be overkill or too slow.
  * Suitable for narrowing down content based on specific queries or keywords.

#### Parameters

  * `semantic_filter` (str, optional): Keywords for filtering relevant documents before clustering. Documents are filtered based on their cosine similarity to the keyword filter embedding. Default is `None`.
  * `word_count_threshold` (int, optional): Minimum number of words per cluster. Default is `20`.
  * `max_dist` (float, optional): Maximum cophenetic distance on the dendrogram to form clusters. Default is `0.2`.
  * `linkage_method` (str, optional): Linkage method for hierarchical clustering. Default is `'ward'`.
  * `top_k` (int, optional): Number of top categories to extract. Default is `3`.
  * `model_name` (str, optional): Model name for embedding generation. Default is `'BAAI/bge-small-en-v1.5'`.

#### Example

    
    
    import asyncio
    from crawl4ai import AsyncWebCrawler
    from crawl4ai.extraction_strategy import CosineStrategy
    
    async def main():
        async with AsyncWebCrawler(verbose=True) as crawler:
            # Define extraction strategy
            strategy = CosineStrategy(
                semantic_filter="finance economy stock market",
                word_count_threshold=10,
                max_dist=0.2,
                linkage_method='ward',
                top_k=3,
                model_name='BAAI/bge-small-en-v1.5'
            )
    
            # Sample URL
            url = "https://www.nbcnews.com/business"
    
            # Run the crawler with the extraction strategy
            result = await crawler.arun(url=url, extraction_strategy=strategy)
            print(result.extracted_content)
    
    asyncio.run(main())
    



## Change Log

URL: https://crawl4ai.com/mkdocs/changelog/

# Changelog

## [v0.2.77] - 2024-08-04

Significant improvements in text processing and performance:

  * 🚀 **Dependency reduction** : Removed dependency on spaCy model for text chunk labeling in cosine extraction strategy.
  * 🤖 **Transformer upgrade** : Implemented text sequence classification using a transformer model for labeling text chunks.
  * ⚡ **Performance enhancement** : Improved model loading speed due to removal of spaCy dependency.
  * 🔧 **Future-proofing** : Laid groundwork for potential complete removal of spaCy dependency in future versions.

These changes address issue #68 and provide a foundation for faster, more
efficient text processing in Crawl4AI.

## [v0.2.76] - 2024-08-02

Major improvements in functionality, performance, and cross-platform
compatibility! 🚀

  * 🐳 **Docker enhancements** : Significantly improved Dockerfile for easy installation on Linux, Mac, and Windows.
  * 🌐 **Official Docker Hub image** : Launched our first official image on Docker Hub for streamlined deployment.
  * 🔧 **Selenium upgrade** : Removed dependency on ChromeDriver, now using Selenium's built-in capabilities for better compatibility.
  * 🖼️ **Image description** : Implemented ability to generate textual descriptions for extracted images from web pages.
  * ⚡ **Performance boost** : Various improvements to enhance overall speed and performance.

A big shoutout to our amazing community contributors: \-
[@aravindkarnam](https://github.com/aravindkarnam) for developing the textual
description extraction feature. \-
[@FractalMind](https://github.com/FractalMind) for creating the first official
Docker Hub image and fixing Dockerfile errors. \-
[@ketonkss4](https://github.com/ketonkss4) for identifying Selenium's new
capabilities, helping us reduce dependencies.

Your contributions are driving Crawl4AI forward! 🙌

## [v0.2.75] - 2024-07-19

Minor improvements for a more maintainable codebase:

  * 🔄 Fixed typos in `chunking_strategy.py` and `crawler_strategy.py` to improve code readability
  * 🔄 Removed `.test_pads/` directory from `.gitignore` to keep our repository clean and organized

These changes may seem small, but they contribute to a more stable and
sustainable codebase. By fixing typos and updating our `.gitignore` settings,
we're ensuring that our code is easier to maintain and scale in the long run.

## v0.2.74 - 2024-07-08

A slew of exciting updates to improve the crawler's stability and robustness!
🎉

  * 💻 **UTF encoding fix** : Resolved the Windows \"charmap\" error by adding UTF encoding.
  * 🛡️ **Error handling** : Implemented MaxRetryError exception handling in LocalSeleniumCrawlerStrategy.
  * 🧹 **Input sanitization** : Improved input sanitization and handled encoding issues in LLMExtractionStrategy.
  * 🚮 **Database cleanup** : Removed existing database file and initialized a new one.

## [v0.2.73] - 2024-07-03

💡 In this release, we've bumped the version to v0.2.73 and refreshed our
documentation to ensure you have the best experience with our project.

  * Supporting website need "with-head" mode to crawl the website with head.
  * Fixing the installation issues for setup.py and dockerfile.
  * Resolve multiple issues.

## [v0.2.72] - 2024-06-30

This release brings exciting updates and improvements to our project! 🎉

  * 📚 **Documentation Updates** : Our documentation has been revamped to reflect the latest changes and additions.
  * 🚀 **New Modes in setup.py** : We've added support for three new modes in setup.py: default, torch, and transformers. This enhances the project's flexibility and usability.
  * 🐳 **Docker File Updates** : The Docker file has been updated to ensure seamless compatibility with the new modes and improvements.
  * 🕷️ **Temporary Solution for Headless Crawling** : We've implemented a temporary solution to overcome issues with crawling websites in headless mode.

These changes aim to improve the overall user experience, provide more
flexibility, and enhance the project's performance. We're thrilled to share
these updates with you and look forward to continuing to evolve and improve
our project!

## [0.2.71] - 2024-06-26

**Improved Error Handling and Performance** 🚧

  * 🚫 Refactored `crawler_strategy.py` to handle exceptions and provide better error messages, making it more robust and reliable.
  * 💻 Optimized the `get_content_of_website_optimized` function in `utils.py` for improved performance, reducing potential bottlenecks.
  * 💻 Updated `utils.py` with the latest changes, ensuring consistency and accuracy.
  * 🚫 Migrated to `ChromeDriverManager` to resolve Chrome driver download issues, providing a smoother user experience.

These changes focus on refining the existing codebase, resulting in a more
stable, efficient, and user-friendly experience. With these improvements, you
can expect fewer errors and better performance in the crawler strategy and
utility functions.

## [0.2.71] - 2024-06-25

### Fixed

  * Speed up twice the extraction function.

## [0.2.6] - 2024-06-22

### Fixed

  * Fix issue #19: Update Dockerfile to ensure compatibility across multiple platforms.

## [0.2.5] - 2024-06-18

### Added

  * Added five important hooks to the crawler:
  * on_driver_created: Called when the driver is ready for initializations.
  * before_get_url: Called right before Selenium fetches the URL.
  * after_get_url: Called after Selenium fetches the URL.
  * before_return_html: Called when the data is parsed and ready.
  * on_user_agent_updated: Called when the user changes the user_agent, causing the driver to reinitialize.
  * Added an example in `quickstart.py` in the example folder under the docs.
  * Enhancement issue #24: Replaced inline HTML tags (e.g., DEL, INS, SUB, ABBR) with textual format for better context handling in LLM.
  * Maintaining the semantic context of inline tags (e.g., abbreviation, DEL, INS) for improved LLM-friendliness.
  * Updated Dockerfile to ensure compatibility across multiple platforms (Hopefully!).

## [0.2.4] - 2024-06-17

### Fixed

  * Fix issue #22: Use MD5 hash for caching HTML files to handle long URLs



## Contact

URL: https://crawl4ai.com/mkdocs/contact/

# Contact

If you have any questions, suggestions, or feedback, please feel free to reach
out to us:

  * GitHub: [unclecode](https://github.com/unclecode)
  * Twitter: [@unclecode](https://twitter.com/unclecode)
  * Website: [crawl4ai.com](https://crawl4ai.com)

## Contributing 🤝

We welcome contributions from the open-source community to help improve
Crawl4AI and make it even more valuable for AI enthusiasts and developers. To
contribute, please follow these steps:

  1. Fork the repository.
  2. Create a new branch for your feature or bug fix.
  3. Make your changes and commit them with descriptive messages.
  4. Push your changes to your forked repository.
  5. Submit a pull request to the main repository.

For more information on contributing, please see our [contribution
guidelines](https://github.com/unclecode/crawl4ai/blob/main/CONTRIBUTING.md).

## License 📄

Crawl4AI is released under the [Apache 2.0
License](https://github.com/unclecode/crawl4ai/blob/main/LICENSE).

Let's work together to make the web more accessible and useful for AI
applications! 💪🌐🤖



