import streamlit as st
import pandas as pd
import random
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

# ----------------------
# 전체 스타일
# ----------------------
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 3rem;
            padding-bottom: 3rem;
        }

        /* 라디오 버튼 점 숨기기 + 텍스트 메뉴 스타일 */
        div[role='radiogroup'] > label > div:first-child {
            opacity: 0 !important;
            width: 0px !important;
        }
        div[role='radiogroup'] > label {
            padding: 2px 6px !important;
            margin: 0px !important;
            cursor: pointer;
        }
        div[role='radiogroup'] > label:hover {
            background-color: #f2f2f2;
        }
        div[role='radiogroup'] > label[data-selected="true"] {
            background-color: #e0e0e0 !important;
            font-weight: 600;
        }

        /* 🔥 사이드바 제목(Main, Contents) 아래 간격 줄이기 */
        section[data-testid="stSidebar"] h3 {
            margin-bottom: 1px !important;
            padding-bottom: 1px !important;
        }

        /* 🔥 라디오 그룹 간격 줄이기 */
        section[data-testid="stSidebar"] div[role='radiogroup'] {
            margin-top: 1px !important;
            margin-bottom: 1px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------
# 주제
# ----------------------
st.title("🔍검색 키워드 트렌드 분석 자동화")

# 헤더
st.markdown(f'{today.year}년 {today.month}월 {today.day}일 기준 채팅수 Summary', help='전일대비 증감')

day, month, year = st.columns(3)
day.metric(label="Daily", value="30,080", delta="3.8%",  border=True)
month.metric(label="Weekly", value="728,459", delta="1.5%",  border=True)
year.metric(label="Monthly", value="5,897,125", delta="-1.8%",  border=True)

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
menu_contents = ["📈 Dataset", " 🆎 A/B Test"]
page_contents = st.sidebar.radio("", menu_contents, index=0, key="page_contents")

# 페이지 상태 결정
if page_main in menu_main:
    st.session_state.page = page_main
elif page_contents in menu_contents:
    st.session_state.page = page_contents

# ----------------------
# 메인 화면
# ----------------------
st.title(f"{st.session_state.page}")

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

# ----------------------
# 🔥 탭 UI
# ----------------------
ui.apply_tab_style()
tab1, tab2 = st.tabs(['내부 검색어', '외부 키워드'])

# ----------------------
# 내부 검색어 탭
# ----------------------
with tab1:
    st.subheader("내부 검색어 키워드 Top 10")

    keywords_internal = [
    "겨울 테마주", "미국금리", "금투자", "환율", "적금",
    "투자", "신용대출", "후불교통", "상생페이백", "ISA"
]

data_internal = {
        "순위": list(range(1, 11)),
        "키워드": keywords_internal,
        "발생건수": [random.randint(500, 1000) for _ in range(10)],
        "전일 대비": [f"{random.randint(-10, 15)}%" for _ in range(10)],
    }

    df_internal = pd.DataFrame(data_internal)
    table_html_internal = df_internal.to_html(index=False, classes="trend-table")

    st.markdown(
        """
        <style>
            table.trend-table {
                width: 100%;
                border-collapse: collapse;
                font-size: 14px;
            }
            table.trend-table th,
            table.trend-table td {
                text-align: center;
                padding: 6px 8px;
                border: 1px solid #ddd;
            }
            table.trend-table thead th {
                background-color: #f5f5f5;
                font-weight: 600;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(table_html_internal, unsafe_allow_html=True)

# ----------------------
# 외부 키워드 탭
# ----------------------
with tab2:
    st.subheader("외부 검색어 키워드 Top 10")

    keywords_external = [
        "AI 기술", "전기차", "반도체 수요", "유가", "금리 전망",
        "환율 변동", "부동산 정책", "ETF 투자", "해외 주식", "메타버스"
    ]

    data_external = {
        "순위": list(range(1, 11)),
        "키워드": keywords_external,
        "발생건수": [random.randint(500, 5000) for _ in range(10)],
        "전일 대비": [f"{random.randint(-10, 15)}%" for _ in range(10)],
    }

    df_external = pd.DataFrame(data_external)
    table_html_external = df_external.to_html(index=False, classes="trend-table")

    st.markdown(table_html_external, unsafe_allow_html=True)