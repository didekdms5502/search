import streamlit as st
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import time
import altair as alt
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

# 내부 데이터 사용 불가. 임의로 추가
day_col, month_col, year_col = st.columns(3)

daily_value = random.randint(10_000, 50_000)
weekly_value = random.randint(700_000, 1_000_000)
monthly_value = random.randint(5_500_000, 7_500_000)

day_col.metric(
    label="Daily",
    value=f"{daily_value:,}",
    delta=f"{random.uniform(-5, 5):.1f}%",
    border=True
)

month_col.metric(
    label="Weekly",
    value=f"{weekly_value:,}",
    delta=f"{random.uniform(-3, 3):.1f}%",
    border=True
)

year_col.metric(
    label="Monthly",
    value=f"{monthly_value:,}",
    delta=f"{random.uniform(-3, 3):.1f}%",
    border=True
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
    st.subheader("내부 검색어 추이")  

    # 내부 데이터 사용 불가. 임의로 추가
    keywords_internal = [
        "겨울 테마주", "미국금리", "금투자", "환율", "적금",
        "투자", "신용대출", "후불교통", "상생페이백", "ISA"
    ]

    data_internal = {
        "순위": list(range(1, 11)),
        "keyword": keywords_internal,
        "발생건수": [random.randint(500, 1000) for _ in range(10)],
        "전일 대비": [f"{random.randint(-10, 15)}%" for _ in range(10)],
    }

    df_internal = pd.DataFrame(data_internal)    

    # ----------------------
    # 🔥 내부 키워드 발생건수 변화 선 그래프
    # ----------------------

    # 1) 날짜 생성 (이번 달 1일 ~ 오늘)
    end_date = datetime.today()
    start_date = end_date.replace(day=1)
    dates = pd.date_range(start=start_date, end=end_date)
    date_labels = dates.strftime("%Y-%m-%d")

    # 2) 키워드
    keywords = df_internal["keyword"].tolist()

    # 3) 초기 데이터
    data = []
    for kw in keywords:
        data.append({
            "date": date_labels[0],
            "keyword": kw,
            "count": np.random.randint(500, 5000)
        })

    df_chart = pd.DataFrame(data)

    # 4) Altair 차트 생성 함수
    def make_chart(df):
        return (
            alt.Chart(df)
            .mark_line(point=True)
            .encode(
                x=alt.X(
                    "date:N",
                    title=None,
                    axis=alt.Axis(
                        labelAngle=-30,     
                        labelFontSize=10,   
                        labelOverlap=False
                    )
                ),
                y=alt.Y("count:Q", title=None, axis=alt.Axis(labelFontSize=10)),
                color=alt.Color("keyword:N", title="keyword", 
                                legend=alt.Legend(
                                    labelFontSize=10,
                                    titleFontSize=10,
                                    symbolSize=40,
                                    symbolStrokeWidth=1)),
                tooltip=["date", "keyword", "count"]
            )
            .properties(height=400)
        )

    chart_area = st.altair_chart(make_chart(df_chart), use_container_width=True)
    progress = st.progress(0)

    # 5) 날짜가 흐르면서 데이터 추가
    for i in range(1, len(date_labels)):
        new_rows = []
        for kw in keywords:
            new_rows.append({
                "date": date_labels[i],
                "keyword": kw,
                "count": np.random.randint(500, 5000)
            })

        df_chart = pd.concat([df_chart, pd.DataFrame(new_rows)], ignore_index=True)
        chart_area.altair_chart(make_chart(df_chart), use_container_width=True)

        progress.progress(int((i / (len(date_labels) - 1)) * 100))
        time.sleep(0.10)

    progress.empty()

    # ----------------------
    # 표 출력
    # ----------------------

    table_html_internal = df_internal.to_html(index=False, classes="trend-table")
    today = datetime.today()
    st.markdown(
        f"""
        <p style="
            font-size:20px;
            font-weight:600;
            margin-bottom:6px;
        ">
            {today.year}년 {today.month}월 {today.day}일 기준 내부 검색어 Top 10
        </p>
        """,
        unsafe_allow_html=True
    )

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
    st.subheader("외부 키워드 추이")

    # ----------------------
    # 1️⃣ CSV 로드 (당일 파일명)
    # ----------------------
    today = datetime.today()
    today_str = today.strftime("%Y%m%d")

    csv_url = f"https://raw.githubusercontent.com/didekdms5502/search/main/search_trend_{today_str}.csv"

    trend_df = pd.read_csv(csv_url)

    # keyword 컬럼 필수 체크
    if "keyword" not in trend_df.columns:
        st.error("CSV 파일에 'keyword' 컬럼이 없습니다.")
        st.stop()

    # TOP 10
    top10 = trend_df.head(10).copy()

    # 발생건수 / 전일대비 생성
    top10["발생건수"] = [random.randint(500, 5000) for _ in range(len(top10))]
    top10["전일 대비"] = [f"{random.randint(-10, 15)}%" for _ in range(len(top10))]
    top10.insert(0, "순위", range(1, len(top10) + 1))

    # ----------------------
    # 2️⃣ 🔥 외부 키워드 발생건수 변화 그래프 (Altair, 내부와 동일)
    # ----------------------
    end_date = datetime.today()
    start_date = end_date.replace(day=1)
    dates = pd.date_range(start=start_date, end=end_date)
    date_labels = dates.strftime("%Y-%m-%d")

    keywords_ext = top10["keyword"].tolist()

    # 초기 데이터
    data = []
    for kw in keywords_ext:
        data.append({
            "date": date_labels[0],
            "keyword": kw,
            "count": random.randint(500, 5000)
        })

    df_chart_ext = pd.DataFrame(data)

    def make_chart_ext(df):
        return (
            alt.Chart(df)
            .mark_line(point=True)
            .encode(
                x=alt.X(
                    "date:N",
                    title=None,
                    axis=alt.Axis(
                        labelAngle=-30,
                        labelFontSize=10,
                        labelOverlap=False
                    )
                ),
                y=alt.Y(
                    "count:Q",
                    title=None,
                    axis=alt.Axis(
                        labelFontSize=10,
                        format=","
                    )
                ),
                color=alt.Color(
                    "keyword:N",
                    title="keyword",
                    legend=alt.Legend(
                        labelFontSize=10,
                        titleFontSize=10,
                        symbolSize=40,
                        symbolStrokeWidth=1
                    )
                ),
                tooltip=["date", "keyword", "count"]
            )
            .properties(height=400)
        )

    chart_area_ext = st.altair_chart(make_chart_ext(df_chart_ext), use_container_width=True)
    progress_ext = st.progress(0)

    for i in range(1, len(date_labels)):
        new_rows = []
        for kw in keywords_ext:
            new_rows.append({
                "date": date_labels[i],
                "keyword": kw,
                "count": random.randint(500, 5000)
            })

        df_chart_ext = pd.concat([df_chart_ext, pd.DataFrame(new_rows)], ignore_index=True)
        chart_area_ext.altair_chart(make_chart_ext(df_chart_ext), use_container_width=True)

        progress_ext.progress(int((i / (len(date_labels) - 1)) * 100))
        time.sleep(0.10)   # 🔥 내부와 동일한 속도

    progress_ext.empty()

    # ----------------------
    # 3️⃣ 표 출력
    # ----------------------
    top10 = top10.drop(columns=["count"])
    table_html_external = top10.to_html(index=False, classes="trend-table")

    st.markdown(
        f"""
        <p style="
            font-size:20px;
            font-weight:600;
            margin-bottom:6px;
        ">
            {today.year}년 {today.month}월 {today.day}일 기준 외부 키워드 Top 10
        </p>
        """,
        unsafe_allow_html=True
    )

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

    st.markdown(table_html_external, unsafe_allow_html=True)

    # the end
