import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Sample", page_icon="📈")

st.markdown("""
<p style="font-size:20px; font-weight:bold; line-height:1.6; text-align:center;">
이번 프로젝트를 기반으로,<br>
점진적인 업데이트와 개선을 통해 데이터를 보완하고 분석을 고도화하여<br>
완성도를 높여 나가려고 합니다. 감사합니다.😊🙇‍♀️
</p>
""", unsafe_allow_html=True)

# st.write(
#     """I will continue adding data over time. Thank you! """
# )
# st.write(
#     "이번 프로젝트를 기반으로,\n"
#     "점진적인 업데이트와 개선을 통해 데이터를 보완하고 분석을 고도화하여\n"
#     "완성도를 높여 나가려고 합니다. 감사합니다."
# )


progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")