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
st.markdown(f'{today.year}년 {today.month}월 {today.day}일 기준 채팅수 Summary', help='전일대비 증감')

day, month, year = st.columns(3)
day.metric(label="Daily", value="30,080", delta="3.8%",  border=True)
month.metric(label="Weekly", value="728,459", delta="1.5%",  border=True)
year.metric(label="Monthly", value="5,897,125", delta="-1.8%",  border=True)


# ----------------------
# 사이드바 스타일 적용
# ----------------------
st.sidebar.markdown(
    """
    <style>
    /* 사이드바 제목 */
    .sidebar .sidebar-content h1 {
        font-size: 10pt;
        color: gray;
    }
    /* 사이드바 섹션(subheader) */
    .sidebar .sidebar-content h2 {
        font-size: 18pt;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# 사이드바 제목
# ----------------------
st.sidebar.title("Menu")

# ----------------------
# Main 섹션
# ----------------------
st.sidebar.markdown("<h2>Main</h2>", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "Overview"

if st.sidebar.button("📊 Overview"):
    st.session_state.page = "Overview"
if st.sidebar.button("📍 Recommended Questions"):
    st.session_state.page = "Recommended Questions"

# ----------------------
# Contents 섹션
# ----------------------
st.sidebar.markdown("<h2>Contents</h2>", unsafe_allow_html=True)

if st.sidebar.button("📈 Dataset"):
    st.session_state.page = "Dataset"
if st.sidebar.button("🆎 A/B Test"):
    st.session_state.page = "A/B Test"

# ----------------------
# 메인 화면
# ----------------------
st.title("🔹 My Dashboard")
st.write(f"현재 페이지: **{st.session_state.page}**")

# ----------------------
# 페이지별 콘텐츠
# ----------------------
if st.session_state.page == "Overview":
    st.write("📊 Overview 페이지 내용")
elif st.session_state.page == "Recommended Questions":
    st.write("📍 Recommended Questions 페이지 내용")
elif st.session_state.page == "Dataset":
    st.write("📈 Dataset 페이지 내용")
elif st.session_state.page == "A/B Test":
    st.write("🆎 A/B Test 페이지 내용")


#col1, col2, col3 = st.columns(3)
#col1.metric("노출수", "30,083", "1.2 %")
#col2.metric("클릭수", "1,585", "-8%")
#col3.metric("CTR", "5.3%", "-4%")