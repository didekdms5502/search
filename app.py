import streamlit as st

today = datetime.today()
month_ago = datetime(today.year, today.month, today.day) + relativedelta(months=-1)
year = today.year
month = "{}".format(month_ago.strftime('%m'))
month_ago_2 = datetime(today.year, today.month, today.day) + relativedelta(months=-2)
month_2 = "{}".format(month_ago_2.strftime('%m'))

# 주제
st.title("🔍검색 키워드 트렌드 분석 자동화")

# 헤더/KPI
st.header("Summary")
st.markdown(f"## {year}년 {month}월 기준 검색어 요약")
st.markdown('### 월간 검색어 집계', help='전월대비 증감')
