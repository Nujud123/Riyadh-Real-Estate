import streamlit as st
import pandas as pd

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------
st.set_page_config(
    page_title="Riyadh Real Estate Dashboard",
    layout="wide"
)

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("clean_data.csv")     # تأكدي من الاسم
    df["Price_per_m2"] = df["Price"] / df["Area"]
    return df

df = load_data()

# -------------------------------------------------------
# Sidebar - Filters
# -------------------------------------------------------
st.sidebar.title("Filters")

st.sidebar.markdown("Use the filters below to explore Riyadh real estate data interactively.")

# District filter
districts = ["All"] + sorted(df["District"].dropna().unique().tolist())
selected_district = st.sidebar.selectbox("Select District", districts)

# Property Type filter
types = sorted(df["Property Type"].dropna().unique().tolist())
selected_types = st.sidebar.multiselect(
    "Select Property Type(s)",
    types,
    default=types
)

# Price range
min_price = int(df["Price"].min())
max_price = int(df["Price"].max())
price_range = st.sidebar.slider(
    "Select Price Range",
    min_price, max_price,
    (min_price, max_price)
)

# -------------------------------------------------------
# Apply Filters
# -------------------------------------------------------
filtered = df.copy()

if selected_district != "All":
    filtered = filtered[filtered["District"] == selected_district]

filtered = filtered[
    (filtered["Property Type"].isin(selected_types)) &
    (filtered["Price"].between(price_range[0], price_range[1]))
]

# -------------------------------------------------------
# Main Title
# -------------------------------------------------------
st.title("Riyadh Real Estate Dashboard")

st.markdown(
    """
    This dashboard provides an interactive view of Riyadh real estate listings.  
    Filter by district, property type, and price to explore patterns in housing data.
    """
)

# -------------------------------------------------------
# Data Preview
# -------------------------------------------------------
st.subheader("Filtered Data Preview")
st.dataframe(filtered.head(50), height=300)

# -------------------------------------------------------
# Summary Metrics
# -------------------------------------------------------
st.subheader("Summary Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Properties", len(filtered))
col2.metric("Average Price", f"{filtered['Price'].mean():,.0f} SAR" if len(filtered) else "0")
col3.metric("Avg Price per m²", f"{filtered['Price_per_m2'].mean():,.0f} SAR" if len(filtered) else "0")

# -------------------------------------------------------
# Visualization 1 — Avg price per district
# -------------------------------------------------------
st.subheader("Average Price by District")

if len(filtered) > 0:
    avg_price_district = (
        filtered.groupby("District")["Price"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
    )

    st.bar_chart(avg_price_district)
else:
    st.write("No data available for this selection.")

# -------------------------------------------------------
# Visualization 2 — Price vs Area
# -------------------------------------------------------
st.subheader("Price vs Area (Scatter Plot)")

if len(filtered) > 0:
    st.scatter_chart(filtered, x="Area", y="Price")
else:
    st.write("No data available.")

# -------------------------------------------------------
# Visualization 3 — Count of property types
# -------------------------------------------------------
st.subheader("Property Type Distribution")

if len(filtered) > 0:
    type_counts = filtered["Property Type"].value_counts()
    st.bar_chart(type_counts)
else:
    st.write("No data available.")

# -------------------------------------------------------
# Simple Insight
# -------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    **Quick Insights:**  
    • Districts with higher average prices reflect premium areas.  
    • Larger areas tend to have higher prices, but price per m² reveals true value.  
    • Property type affects price distribution across Riyadh.
    """
)
