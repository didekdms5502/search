import streamlit as st
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime
from dateutil.relativedelta import relativedelta

def plot_keyword_trends(df, title):
    # 최근 7일 날짜 생성
    dates = pd.date_range(end=pd.Timestamp.today(), periods=7)

    fig, ax = plt.subplots(figsize=(10, 5))

    # df 안의 keyword 컬럼 기준으로 그래프 생성
    for keyword in df["keyword"]:
        trend = np.random.randint(300, 5000, size=7)  # 임의 검색량
        ax.plot(dates, trend, marker="o", label=keyword)

    ax.set_title(title)
    ax.set_xlabel("날짜")
    ax.set_ylabel("검색량(임의 생성)")
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

    st.pyplot(fig)

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

tab1, tab2 = st.tabs(['내부 검색어', '외부 키워드'])

# ----------------------
# 내부 검색어 탭
# ----------------------
with tab1:
    st.subheader("내부 검색어 Top 10")

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
    # 🔥 내부 키워드 발생건수 변화 선 그래프
    # ----------------------
    import matplotlib.pyplot as plt

    # 1) 한글 폰트 설정 (Windows 기준)
    plt.rc('font', family='Malgun Gothic')
    plt.rc('axes', unicode_minus=False)

    # 2) 날짜 생성 (2025-12-01 ~ 2025-12-18)
    dates = pd.date_range(start="2025-12-01", end="2025-12-18")

    # 3) 내부 키워드 리스트
    keywords = df_internal["키워드"].tolist()

    # 4) 키워드별 발생건수 변화(임의 생성)
    trend_data = {}
    for kw in keywords:
        # 18일 동안 500~5000 사이의 랜덤 발생건수 생성
        counts = np.random.randint(500, 5000, size=len(dates))
        trend_data[kw] = counts

    # 5) 선 그래프 생성
    fig_int, ax_int = plt.subplots(figsize=(12, 6))

    colors = plt.cm.tab10(np.linspace(0, 1, len(keywords)))

    for i, kw in enumerate(keywords):
        ax_int.plot(dates, trend_data[kw], label=kw, color=colors[i], marker="o")

    # 6) y축: 발생건수 (순위 아님)
    ax_int.set_ylabel("발생건수")

    # 7) x축 라벨 제거
    ax_int.set_xlabel("")

    # 8) 그래프 제목
    ax_int.set_title("내부 검색어 발생건수 변화 추이")

    # 9) x축 날짜 라벨 회전
    plt.xticks(rotation=45)

    # 10) 범례 표시
    ax_int.legend(loc="upper left", bbox_to_anchor=(1, 1))

    st.pyplot(fig_int)

# ----------------------
# 외부 키워드 탭
# ----------------------
with tab2:
    st.subheader("외부 키워드 Top 10")

    # 1) GitHub RAW CSV URL 입력
    csv_url = "https://raw.githubusercontent.com/didekdms5502/search/main/trend_keywords.csv"

    # 2) CSV 자동 불러오기
    trend_df = pd.read_csv(csv_url)

    # 3) TOP 10만 사용
    top10 = trend_df.head(10).copy()

    # 👉 count 컬럼 제거 (CSV에 count가 있을 때 자동 제거)
    top10 = top10.drop(columns=["count"], errors="ignore")

    # 4) 발생건수 총합 100 이하로 랜덤 생성 (지금은 실제로는 사용 안 함)
    remaining = 100
    random_counts = []
    for i in range(len(top10)):
        if i == len(top10) - 1:
            value = remaining
        else:
            value = random.randint(1, max(1, remaining - (len(top10) - i - 1)))
        random_counts.append(value)
        remaining -= value

    top10["발생건수"] = [random.randint(500, 5000) for _ in range(len(top10))]

    # 5) 전일 대비 랜덤 생성 (-10% ~ +15%)
    top10["전일 대비"] = [f"{random.randint(-10, 15)}%" for _ in range(len(top10))]

    # 6) 순위 컬럼 추가
    top10.insert(0, "순위", range(1, len(top10) + 1))

    # 7) HTML 테이블 변환
    table_html_external = top10.to_html(index=False, classes="trend-table")
    st.markdown(table_html_external, unsafe_allow_html=True)

    # 🔹 외부 키워드 그래프 시각화 (발생건수 기준 막대 그래프)
    if "keyword" in top10.columns:
        st.markdown("#### 외부 키워드 발생건수 그래프")
        fig_ext, ax_ext = plt.subplots(figsize=(8, 4))
        ax_ext.bar(top10["keyword"], top10["발생건수"], color="#DD8452")
        ax_ext.set_xlabel("키워드")
        ax_ext.set_ylabel("발생건수")
        ax_ext.set_title("외부 키워드 Top 10 발생건수")
        plt.xticks(rotation=45, ha="right")
        st.pyplot(fig_ext)
    else:
        st.error("CSV 파일에 'keyword' 컬럼이 없습니다. 컬럼명을 확인해주세요.")
