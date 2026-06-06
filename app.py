import streamlit as st
import pandas as pd
import plotly.express as px

from rag.rag_engine import ask_question

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Comparative Financial Analysis Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = pd.read_csv("financial_full.csv")

df = df.sort_values(
    ["company", "year"]
)

df["growth_pct"] = (
    df.groupby("company")["revenue"]
      .pct_change() * 100
)

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📈 Comparative Financial Analysis Dashboard")

st.markdown(
    "CustomerInsights.AI - AI Engineer Intern Project"
)

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

st.subheader("📊 Executive Summary")

col1, col2 = st.columns(2)

with col1:

    st.success(
        """
**Growth Leader**

AMD demonstrates the strongest recent revenue growth trajectory among the companies analyzed.
"""
    )

    st.info(
        """
**AI Market Momentum**

NVIDIA experienced significant revenue acceleration driven by AI infrastructure and data center demand.
"""
    )

with col2:

    st.warning(
        """
**Largest Asset Base**

Intel maintains the largest asset base and overall operational scale.
"""
    )

    st.success(
        """
**AI-Powered Analysis**

The integrated RAG chatbot answers questions directly from SEC filings with source citations.
"""
    )

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

selected_companies = st.sidebar.multiselect(
    "Select Companies",
    options=df["company"].unique(),
    default=df["company"].unique()
)

filtered_df = df[
    df["company"].isin(selected_companies)
]

# --------------------------------------------------
# Latest Financial Snapshot
# --------------------------------------------------

st.subheader("💰 Latest Financial Snapshot")

latest_df = (
    filtered_df.sort_values("year")
    .groupby("company")
    .tail(1)
)

metric_cols = st.columns(
    len(latest_df)
)

for i, (_, row) in enumerate(
    latest_df.iterrows()
):

    revenue_billion = (
        row["revenue"] / 1_000_000_000
    )

    metric_cols[i].metric(
        row["company"],
        f"${revenue_billion:.2f}B"
    )

# --------------------------------------------------
# Revenue Trend
# --------------------------------------------------

st.subheader("📈 Revenue Trend Comparison")

revenue_chart = px.line(
    filtered_df,
    x="year",
    y="revenue",
    color="company",
    markers=True,
    title="Revenue Comparison Across Years"
)

revenue_chart.update_layout(
    xaxis_title="Year",
    yaxis_title="Revenue (USD)"
)

st.plotly_chart(
    revenue_chart,
    use_container_width=True
)

# --------------------------------------------------
# Revenue Growth
# --------------------------------------------------

st.subheader("🚀 Revenue Growth (%)")

growth_chart = px.bar(
    filtered_df,
    x="year",
    y="growth_pct",
    color="company",
    barmode="group",
    title="Year-over-Year Revenue Growth"
)

growth_chart.update_layout(
    xaxis_title="Year",
    yaxis_title="Growth Percentage"
)

st.plotly_chart(
    growth_chart,
    use_container_width=True
)

# --------------------------------------------------
# Asset Comparison
# --------------------------------------------------

st.subheader("🏦 Total Assets Comparison")

asset_chart = px.line(
    filtered_df,
    x="year",
    y="assets",
    color="company",
    markers=True,
    title="Assets Comparison Across Years"
)

asset_chart.update_layout(
    xaxis_title="Year",
    yaxis_title="Assets (USD)"
)

st.plotly_chart(
    asset_chart,
    use_container_width=True
)

# --------------------------------------------------
# Financial Summary
# --------------------------------------------------

st.subheader("📋 Financial Summary")

summary_df = filtered_df.copy()

summary_df["Revenue (Billions)"] = (
    summary_df["revenue"] / 1_000_000_000
).round(2)

summary_df["Assets (Billions)"] = (
    summary_df["assets"] / 1_000_000_000
).round(2)

display_columns = [
    "company",
    "year",
    "Revenue (Billions)",
    "Assets (Billions)",
    "growth_pct"
]

st.dataframe(
    summary_df[display_columns],
    use_container_width=True
)

# --------------------------------------------------
# Automated Insights
# --------------------------------------------------

st.subheader("🤖 Automated Insights")

for company in filtered_df["company"].unique():

    company_df = (
        filtered_df[
            filtered_df["company"] == company
        ]
        .sort_values("year")
    )

    growth_series = (
        company_df["growth_pct"]
        .dropna()
    )

    if len(growth_series) == 0:
        continue

    latest_growth = growth_series.iloc[-1]

    if latest_growth > 20:

        st.success(
            f"{company}: Strong revenue growth of {latest_growth:.2f}%."
        )

    elif latest_growth > 0:

        st.info(
            f"{company}: Positive revenue growth of {latest_growth:.2f}%."
        )

    else:

        st.warning(
            f"{company}: Revenue declined by {abs(latest_growth):.2f}%."
        )

# --------------------------------------------------
# Chatbot
# --------------------------------------------------

st.markdown("---")

st.header("🤖 Financial Filing Chatbot")

st.markdown(
    """
**Example Questions**

- How did Intel revenue change in 2024?
- What AI opportunities did AMD discuss?
- What risks did NVIDIA identify?
- Compare AMD and Intel business strategies.
"""
)

question = st.text_area(
    "Ask a question about SEC filings",
    height=100
)

if question:

    with st.spinner(
        "Analyzing SEC filings..."
    ):

        result = ask_question(
            question
        )

    st.subheader("Answer")

    st.write(
        result["answer"]
    )

    st.subheader("Sources")

    for source in result["sources"]:

        st.code(source)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Data Source: SEC Company Facts API + SEC EDGAR Filings | Built with Streamlit, FAISS, LangChain, OpenAI, and HuggingFace Embeddings"
)