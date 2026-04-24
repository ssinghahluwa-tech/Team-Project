
# Schema Notes: McDonald’s Financial Dataset

## Overview
This dataset contains historical financial data for McDonald’s over time (monthly from 2005–2024). It includes key financial metrics used to evaluate company performance, valuation, and financial health.

Each row represents a time period (month), and each column represents a financial variable.

---

## Key Column Groups

### 1. Time Variable
- **Date**
  - Type: Date / Time
  - Description: Represents the reporting period (monthly)
  - Use: Enables time-series analysis such as trends, growth rates, and seasonality

---

### 2. Market & Valuation Metrics
- **Market cap ($B)**
- **P/E ratio**
- **P/S ratio**
- **P/B ratio**

**Purpose:**
- Measure how the market values McDonald’s relative to earnings, sales, and assets
- Useful for identifying overvaluation or undervaluation

**Notes:**
- P/B ratio includes negative values → indicates periods of negative book value or accounting effects
- Ratios may be sensitive to fluctuations in earnings or assets

---

### 3. Revenue & Profitability Metrics
- **Revenue ($B)**
- **Earnings ($B)**
- **Operating Margin (%)**
- **EPS ($)**

**Purpose:**
- Evaluate company performance and profitability
- Track growth and efficiency over time

**Relationships:**
- Earnings = Revenue × Profitability (approximate)
- Operating Margin indicates operational efficiency
- EPS depends on earnings and shares outstanding

---

### 4. Capital Structure & Liquidity
- **Cash on Hand ($B)**
- **Total debt ($B)**
- **Total liabilities ($B)**
- **Total assets ($B)**
- **Net assets ($B)**

**Purpose:**
- Assess financial stability and leverage
- Evaluate risk and ability to meet obligations

**Notes:**
- Net assets = Total assets – Total liabilities
- High debt may indicate leverage strategy rather than risk alone

---

### 5. Shareholder Metrics
- **Shares Outstanding ($B)**
- **Dividend Yield (%)**
- **Dividend (stock split adjusted) ($)**

**Purpose:**
- Measure returns to investors
- Understand dilution and capital distribution

**Notes:**
- Dividend values are adjusted for stock splits
- Dividend yield depends on stock price changes

---

## Data Characteristics

- Dataset is **time-series structured**
- Contains **continuous numerical variables**
- Some variables show **high variance (e.g., Market cap, Debt)**
- Presence of **outliers and negative values** (e.g., P/B ratio, Net assets)
- Likely strong **correlations** between:
  - Revenue and Earnings
  - Earnings and EPS
  - Debt and Liabilities

---

## Potential Data Issues

- Missing values may exist in some columns
- Ratios can be unstable if denominators are near zero
- Financial metrics may be influenced by:
  - accounting changes
  - macroeconomic conditions
  - stock market volatility

---

## Analytical Opportunities

This dataset supports:

- Time-series trend analysis (growth in revenue, earnings)
- Financial ratio analysis (valuation trends)
- Correlation analysis between key metrics
- Regression modeling (e.g., predicting earnings or market cap)
- Visualization (line plots, distributions, heatmaps)

---

## Conclusion

The dataset provides a comprehensive view of McDonald’s financial performance over time, combining operational, valuation, and balance sheet metrics. It is well-suited for financial analysis, forecasting, and understanding long-term trends in a large public company.