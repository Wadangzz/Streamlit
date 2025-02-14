import streamlit as st

st.title("인터랙티브 위젯 예시")

# 1. 버튼
if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")

# 2. 슬라이더
age = st.slider("나이를 선택하세요", 0, 100, 25) # (라벨, 최소값, 최대값, 초기값)
st.write("선택된 나이:", age)

# 3. 텍스트 입력
name = st.text_input("이름을 입력하세요", "홍길동") # (라벨, 초기값)
st.write("입력된 이름:", name)

st.title("레이아웃 예시")

# 1. 컬럼 나누기
col1, col2 = st.columns(2)

with col1:
    st.header("첫 번째 컬럼")
    st.write("아 이런거구만~~~")

with col2:
    st.header("두 번째 컬럼")
    st.image("http://lol.inven.co.kr", width=150)

# 2. 사이드바
with st.sidebar:
    st.sidebar.header("사이드바 메뉴")
    menu = st.radio("메뉴 선택", ["메뉴 1", "메뉴 2", "메뉴 3"])
    st.write("선택된 메뉴:", menu)