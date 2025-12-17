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

        /* 🔹 라디오 버튼을 텍스트 메뉴처럼 보이게 만들기 */

        /* 점(●) 숨기기 */
        div[role='radiogroup'] > label > div:first-child {
            display: none !important;
        }

        /* 라벨 전체를 버튼처럼 보이게 */
        div[role='radiogroup'] > label {
            padding: 6px 10px;
            border-radius: 4px;
            cursor: pointer;
        }

        /* Hover 효과 */
        div[role='radiogroup'] > label:hover {
            background-color: #f2f2f2;
        }

        /* 선택된 항목 강조 */
        div[role='radiogroup'] > label[data-selected="true"] {
            background-color: #e0e0e0 !important;
            font-weight: 600;
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
# 사이드바 스타일
# ----------------------
st.markdown(
    """
    <style>
    /* 사이드바 폭 넓히기 */
    .css-1d391kg .sidebar-content {
        width: 300px;
    }

    /* 버튼 테두리 제거 */
    .sidebar .stButton>button {
        width: 100%;
        text-align: left;
        padding: 8px 12px;
        margin: 2px 0;
        border: none;
        border-radius: 0px;
        background-color: transparent;
    }

    /* 버튼 클릭 시 배경 강조 */
    .stButton>button:focus {
        background-color: #e6f0ff;
    }

    /* 섹션 제목 크기 */
    .sidebar h2 {
        font-size: 16pt;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# 메뉴 상태 초기화
# ----------------------
if "page" not in st.session_state:
    st.session_state.page = "Overview"

# ----------------------
# 사이드바 메뉴
# ----------------------
st.sidebar.markdown("### Main")
menu_main = ["📊 Overview", "📍 Recommended Questions"]
page_main = st.sidebar.radio("", menu_main, index=0, key="page_main")

st.sidebar.markdown("### Contents")
menu_contents = ["📈 Dataset", "🆎 A/B Test"]
page_contents = st.sidebar.radio("", menu_contents, index=0, key="page_contents")

# 페이지 상태 결정
if page_main in menu_main:
    st.session_state.page = page_main
elif page_contents in menu_contents:
    st.session_state.page = page_contents

# ----------------------
# 메인 화면
# ----------------------
st.title("🔹 Dashboard")
st.write(f"현재 페이지: **{st.session_state.page}**")

# ----------------------
# 페이지별 내용
# ----------------------
if st.session_state.page == "Overview":
    st.write("📊 Overview 페이지 내용")
elif st.session_state.page == "Recommended Questions":
    st.write("📍 Recommended Questions 페이지 내용")
elif st.session_state.page == "Dataset":
    st.write("📈 Dataset 페이지 내용")
elif st.session_state.page == "A/B Test":
    st.write("🆎 A/B Test 페이지 내용")
