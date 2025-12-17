import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta


# 날짜 계산
today = datetime.today()

month_ago = today + relativedelta(months=-1)
year = today.year
month = month_ago.strftime('%m')

month_ago_2 = today + relativedelta(months=-2)
month_2 = month_ago_2.strftime('%m')


# 주제
st.title("🔍검색 키워드 트렌드 분석 자동화")

# 헤더/KPI
st.header("Summary")
st.markdown(f"## {year}년 {month}월 기준 검색어 요약")
st.markdown('### 월간 검색어 집계', help='전월대비 증감')
