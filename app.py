import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 날짜 계산
today = datetime.today()
month_ago = today + relativedelta(months=-1)
year = today.year
month = month_ago.strftime('%m')
day = today.day

month_ago_2 = today + relativedelta(months=-2)
month_2 = month_ago_2.strftime('%m')

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 3rem;
            padding-bottom: 3rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 주제
st.title("🔍검색 키워드 트렌드 분석 자동화")

# 헤더
st.markdown(
    f"""
    <h5 style="margin-bottom: 2rem; color: gray;">
        {year}년 {month}월 {day}일 기준 검색어 Summary
    </h4>
    """,
    help='전일대비 증감',
    unsafe_allow_html=True
)

day, month, year = st.columns(3)
day.metric(label="Daily", value="30,080", delta="3.8%",  border=True)
month.metric(label="Daily", value="728,459", delta="1.5%",  border=True)
year.metric(label="Daily", value="5,897,125", delta="1.8%",  border=True)





#col1, col2, col3 = st.columns(3)
#col1.metric("노출수", "30,083", "1.2 %")
#col2.metric("클릭수", "1,585", "-8%")
#col3.metric("CTR", "5.3%", "-4%")