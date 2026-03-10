🚀 Q-Comm Insights Engine
An End-to-End Automated ETL & AI Business Intelligence Suite
📌 Project Overview
In the high-velocity world of Quick Commerce, data is often fragmented across multiple platforms (Swiggy, Blinkit, Zepto, etc.) with inconsistent naming conventions.

Q-Comm Insights Engine is a production-ready Python suite that automates the transition from raw, messy delivery logs to actionable executive insights. It features a schema-agnostic data pipeline, SQL persistence, and a natural language "AI Analyst" interface.

🛠️ Key Features
1. Resilient Data Pipeline (ETL)
Schema-Agnostic Ingestion: Uses a custom COLUMN_MAPPER engine to automatically identify and standardize inconsistent headers (e.g., mapping "App," "Company," and "Platform" all to a single platform column).

Automated Cleaning: Handles duplicate removal, numeric type coercion, and missing value treatment for logistics-critical fields like Order_Value and Delivery_Time.

2. Logic-Driven AI Business Analyst
Natural Language Queries: Instead of writing SQL, users can ask questions like "What is the revenue by city?" or "Show average ratings per platform."

Intent Detection Engine: A custom-built heuristic NLP engine (ai_analytics.py) that maps user strings to dynamic Pandas aggregations and Matplotlib visualizations.

3. Strategic Expansion Intelligence
Expansion Algorithm: A data-driven recommendation engine that identifies high-potential expansion cities by calculating a proprietary score based on order volume weighted against customer satisfaction.

4. Automated Executive Reporting
PDF Generation: Automatically generates professional, board-ready PDF reports summarizing operational efficiency, discount impacts, and demographic trends.

