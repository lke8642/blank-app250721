import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# 페이지 제목과 설명
st.title("🎈 Blank App Template 예시 페이지")
st.write("이 페이지는 Streamlit에서 사용할 수 있는 다양한 요소의 예시를 보여줍니다.")

# 텍스트 요소
st.header("텍스트 요소")
st.subheader("서브헤더 예시")
st.text("일반 텍스트 예시입니다.")
st.markdown("**마크다운**을 사용할 수도 있습니다!")

# 데이터 표시
st.header("데이터 표시")
st.write("데이터프레임 예시:")
import pandas as pd
df = pd.DataFrame({
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [25, 30, 22]
})
st.dataframe(df)  # 데이터프레임 표시

st.table(df)      # 테이블 형태로 표시

# 차트 예시
st.header("차트 예시")
st.line_chart(df['나이'])  # 라인 차트
st.bar_chart(df['나이'])   # 바 차트

# 입력 요소
st.header("입력 요소")
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의하십니까?")  # 체크박스
option = st.selectbox("좋아하는 색을 선택하세요", ['빨강', '파랑', '초록'])  # 셀렉트박스
st.radio("성별을 선택하세요", ['남성', '여성'])  # 라디오 버튼
st.slider("점수를 선택하세요", 0, 100, 50)  # 슬라이더

# 파일 업로드
st.header("파일 업로드")
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("업로드된 파일 이름:", uploaded_file.name)

# 버튼
st.header("버튼")
if st.button("클릭하세요"):
    st.success("버튼이 클릭되었습니다!")

# 이미지 표시
st.header("이미지 표시")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지 예시")

# 알림 메시지
st.header("알림 메시지")
st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")

# 코드 블록 표시
st.header("코드 블록 표시")
st.code("print('Hello, Streamlit!')", language='python')
