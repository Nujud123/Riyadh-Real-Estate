import streamlit as st
import pandas as pd
from PIL import Image

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="Riyadh Real Estate Dashboard",
    layout="wide"
)

# -------------------------------------------------------
# Fixed Theme + RTL
# -------------------------------------------------------
def apply_fixed_theme():
    st.markdown("""
        <style>

        /* ===== GLOBAL TEXT STYLE ===== */
        html, body, [class*="css"]  {
            text-align: right;
            font-family: "Tahoma", "Arial", sans-serif;
        }

        /* ===== APP BACKGROUND ===== */
        .stApp {
           background: #345f7a;
            color: #ffffff !important;
        }
        
        /* Push logo upward in sidebar */
        [data-testid="stSidebar"] img {
            margin-top: -40px !important;
        }

        /* ===== SIDEBAR ===== */
        section[data-testid="stSidebar"] {
            background: #213852 !important;   /* نفس الخلفية الأساسية */
        }

        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }

        /* ===== TITLES ===== */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;        /* أبيض للعناوين */
            text-align: right;
        }

        /* ===== DATAFRAME ===== */
        .stDataFrame {
            background-color: #1b2f3f !important;   /* مشتق داكن من الأساسي */
            border-radius: 12px;
        }

        /* الجدول من اليمين */
        .stDataFrame table {
            direction: rtl;
        }

        .stDataFrame table th,
        .stDataFrame table td {
            text-align: right !important;
            color: #ffffff !important;
            background-color: #1b2f3f !important;
        }

        /* ===== PROPERTY CARD ===== */
        .property-card {
            background-color: #ffffff;
            padding: 18px;
            border-radius: 18px;
            box-shadow: 0 10px 25px rgba(30, 131, 227, 0.25);
            margin-bottom: 20px;
            color: #213852;
            border: 2px solid #1e83e3;
            height: 230px;          
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }


        .property-card h4 {
            color: #213852;
            font-weight: 700;
            margin-bottom: 10px;
            
        }

        .property-card p {
            color: #213852;
            margin: 0 0 6px 0;
            font-size: 14px;
           
        }

        /* ===== BADGE ===== */
        .badge {
            background: #56e5f7;     
            color: #213852;
            padding: 6px 16px;
            border-radius: 999px;
            font-size: 11px;
            font-weight: 700;
            display: inline-block;
            margin-top: 10px;
            width: auto !important;        
            align-self: flex-start;
        }

        /* ===== FORM ELEMENTS ===== */
        .stSlider,
        .stMultiSelect,
        .stRadio {
            text-align: right;
        }

        /* Selectbox بدون قلب الاتجاه */
        .stSelectbox {
            text-align: right;
        }

        /* ===== METRICS (KPIs) ===== */
        div[data-testid="stMetric"] {
            direction: ltr;
            text-align: right;
        }

        div[data-testid="stMetric"] > div {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
        }

        div[data-testid="stMetric"] label {
            color: #56e5f7 !important;    /* لون عنوان المؤشر */
        }

        div[data-testid="stMetric"] div {
            color: #ffffff !important;   /* الرقم أبيض */
        }

        /* ===== FORM ELEMENTS ===== */
        .stSlider {
            text-align: right;  /* بس نخلي الليبل يمين، بدون ألوان */
        }


        /* Multiselect tags */
        span[data-baseweb="tag"] {
            background-color: #1e83e3 !important;
            color: white !important;
            border-radius: 12px !important;
        }

        /* Multiselect tag remove (×) */
        span[data-baseweb="tag"] svg {
            color: white !important;
        }

        /* Radio buttons */
        .stRadio label div[role="radiogroup"] div {
            accent-color: #56e5f7;
        }

        /* Selectbox border */
        .stSelectbox div[data-baseweb="select"] {
            border: 1px solid #56e5f7 !important;
            background-color: #213852 !important;
            color: white !important;
        }

        </style>
    """, unsafe_allow_html=True)

apply_fixed_theme()

# -------------------------------------------------------
# Load Data
# -------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("clean_data.csv")

    if "Price_per_m2" not in df.columns:
        df["Price_per_m2"] = df["Price"] / df["Area"]

    return df


df = load_data()

# -------------------------------------------------------
# Sidebar - Filters
# -------------------------------------------------------
logo = Image.open("Logo of Riyadh Real Estate.png")
st.sidebar.image(logo, use_container_width=True)

st.sidebar.title("الفلاتر")
st.sidebar.markdown("استخدم هذه الفلاتر للتحكم في البيانات المعروضة")

districts = ["الكل"] + sorted(df["District"].dropna().unique().tolist())
selected_district = st.sidebar.selectbox("اختيار الحي", districts)

property_types = sorted(df["Property Type"].dropna().unique().tolist())
selected_types = st.sidebar.multiselect(
    "اختيار نوع العقار",
    property_types,
    default=property_types
)

min_price = int(df["Price"].min())
max_price = int(df["Price"].max())

price_min, price_max = st.sidebar.slider(
    "نطاق السعر (ريال)",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)  # Range: (min, max)
)

# -------------------------------------------------------
# Apply Filters
# -------------------------------------------------------
filtered_df = df.copy()

if selected_district != "الكل":
    filtered_df = filtered_df[filtered_df["District"] == selected_district]

filtered_df = filtered_df[
    (filtered_df["Property Type"].isin(selected_types)) &
    (filtered_df["Price"].between(price_min, price_max))
]


# -------------------------------------------------------
# Main Title
# -------------------------------------------------------
st.title("لوحة بيانات سوق العقار في مدينة الرياض")

st.markdown("""
،هذه اللوحة تتيح لك استكشاف سوق العقار في الرياض  
.مع توصيات ذكية لكل نوع عقار بناءً على تفضيل المستخدم
""")

# -------------------------------------------------------
# Data Preview
# -------------------------------------------------------
st.subheader("معاينة البيانات")
st.markdown("""
<style>
.rtl-table {
    direction: rtl;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

#filtered_df = filtered_df.iloc[:, ::-1] 
table_df = filtered_df.drop(columns=["Property_ID",'City'], errors="ignore")
cols = list(table_df.columns)

if "Price" in cols and "Area" in cols and "Price_per_m2" in cols:
    cols.remove("Price_per_m2")
    area_index = cols.index("Area")
    cols.insert(area_index, "Price_per_m2")

table_df = table_df[cols]

st.dataframe(table_df.head(30), use_container_width=True)



# -------------------------------------------------------
# Summary Metrics
# -------------------------------------------------------
st.subheader("مؤشرات عامة")

col1, col2, col3 = st.columns(3)

total_props = len(filtered_df)
avg_price = filtered_df["Price"].mean() if total_props > 0 else 0
avg_m2 = filtered_df["Price_per_m2"].mean() if total_props > 0 else 0

col1.metric("عدد العقارات", total_props)
col2.metric("متوسط السعر (ريال)", f"{avg_price:,.0f}")
col3.metric("متوسط سعر المتر(ريال)", f"{avg_m2:,.0f}")

# -------------------------------------------------------
# Charts
# -------------------------------------------------------
st.subheader("متوسط السعر حسب الحي (أعلى 15 حي)")

if len(filtered_df) > 0:
    avg_price_district = (
        filtered_df.groupby("District")["Price"]
        .mean()
        .sort_values(ascending=False)
        .head(15)
    )
    st.bar_chart(avg_price_district)

st.subheader("العلاقة بين المساحة والسعر")
if len(filtered_df) > 0:
    st.scatter_chart(filtered_df, x="Area", y="Price")

st.subheader("توزيع أنواع العقارات")
if len(filtered_df) > 0:
    type_counts = filtered_df["Property Type"].value_counts()
    st.bar_chart(type_counts)

# -------------------------------------------------------
# Recommendations Section — Dropdown + Cards
# -------------------------------------------------------
st.markdown("---")
st.subheader("التوصيات الذكية لكل نوع عقار")

# نخلي الدروب داون في عمود على اليمين
col_empty, col_filter = st.columns([2, 1])  # مساحة فاضية يسار، والدروب داون يمين

with col_filter:
    st.markdown("#### كيف تفضل أسعار العقارات؟")
    method_label = st.selectbox(
        "",
        [
            "أسعار تنافسية غير مكلفة",
            "متوسط أسعار السوق",
            "فاخرة مرتفعة السعر",
            "لا يوجد تفضيل"
        ],
        index=0,
        label_visibility="collapsed"
    )


if method_label.startswith("أسعار"):
    recommendation_method = "best"
elif method_label.startswith("متوسط"):
    recommendation_method = "rep"
elif method_label.startswith("فاخرة"):
    recommendation_method = "high"
else:
    recommendation_method = "random"

if len(filtered_df) == 0:
    st.info("لا توجد بيانات مطابقة للفلاتر الحالية")
else:
    rec_source = filtered_df.copy()
    recommendations = []

    for p_type, group in rec_source.groupby("Property Type"):
        if len(group) == 0:
            continue

        if len(group) >= 10:
            q1 = group["Area"].quantile(0.25)
            q3 = group["Area"].quantile(0.75)
            group = group[(group["Area"] >= q1) & (group["Area"] <= q3)]
            if len(group) == 0:
                continue

        if recommendation_method == "best":
            idx = group["Price_per_m2"].idxmin()
            chosen = group.loc[idx]

        elif recommendation_method == "rep":
            target = group["Price_per_m2"].mean()
            idx = (group["Price_per_m2"] - target).abs().idxmin()
            chosen = group.loc[idx]

        elif recommendation_method == "high":
            idx = group["Price_per_m2"].idxmax()
            chosen = group.loc[idx]

        else:  # random
            chosen = group.sample(1).iloc[0]

        recommendations.append(chosen)

    rec_df = pd.DataFrame(recommendations)
    rec_df = rec_df.rename(columns={"Property Type": "Property_Type"})

    if recommendation_method == "best":
        badge_label = "سعر تنافسي"
    elif recommendation_method == "rep":
        badge_label = "يمثل السوق"
    elif recommendation_method == "high":
        badge_label = "عقار فاخر"
    else:
        badge_label = "خيار عشوائي"

    cards_per_row = 3
    total_rows = (len(rec_df) + cards_per_row - 1) // cards_per_row

    for r in range(total_rows):
        row_slice = rec_df.iloc[r*cards_per_row:(r+1)*cards_per_row]
        cols = st.columns(3)

        start_index = 3 - len(row_slice)   # ✅ يدفع الكروت إلى اليمين تلقائياً

        for i in range(len(row_slice)):
            rec = row_slice.iloc[i]
            with cols[start_index + i]:
                st.markdown(
                    f"""
                    <div class="property-card">
                        <p><b>نوع العقار:</b> {rec.Property_Type}</p>
                        <p><b>الحي:</b> {rec.District}</p>
                        <p><b>المساحة:</b> {rec.Area:.0f} م²</p>
                        <p><b>السعر:</b> {rec.Price:,.0f} ريال</p>
                        <p><b>سعر المتر:</b> {rec.Price_per_m2:,.0f} ريال</p>
                        <span class="badge">{badge_label}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# -------------------------------------------------------
# Final Notes
# -------------------------------------------------------
st.markdown("---")
st.markdown("""
**ملاحظات تحليلية:**  
 التوصيات تتحدّث تلقائيًا مع أي تغيير في الفلاتر أو البيانات.  
 "أفضل قيمة" تعتمد على أقل سعر للمتر المربع.  
 "يمثل السوق" تعتمد على عقار قريب من متوسط سعر المتر.  
 "الاختيار العشوائي" لعرض عينة متنوعة بدون تحيز.
""")
