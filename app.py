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


# 주제
st.title("🔍Search Keyword Trend Analysis")

# 헤더
st.markdown(f"## {year}년 {month}월 {day}일 기준 검색어 Summary")
st.markdown('### 일별 검색어 집계', help='전일대비 증감')

st.metric(label="총 검색량", value="30,083", delta="1.2 %")

col1, col2, col3 = st.columns(3)
col1.metric("노출수", "30,083", "1.2 %")
col2.metric("클릭수", "1,585", "-8%")
col3.metric("CTR", "5.3%", "-4%")