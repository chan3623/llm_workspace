import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Streamlit 페이지 설정
st.set_page_config(
    page_title="OpenAI Chatbot",
    page_icon="🤖",
)

# OpenAI 클라이언트 초기화
client = OpenAI()

# 대화 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "당신은 친절하고 능숙한 AI 어시스턴트입니다. 사용자 질문에 정확하고 명쾌하게 답변해주세요.",
        }
    ]

# 제목
st.title("🤖 OpenAI Chatbot")
st.caption("GPT-4o-mini와 대화해보세요.")

# 기존 대화 화면에 출력
for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력
user_input = st.chat_input("메시지를 입력하세요.")

if user_input:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    # 사용자 메시지 화면에 출력
    with st.chat_message("user"):
        st.write(user_input)

    try:
        # OpenAI API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages,
            temperature=0.7,
        )

        # AI 응답 추출
        bot_response = response.choices[0].message.content

        # AI 응답 저장
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_response,
            }
        )

        # AI 응답 화면에 출력
        with st.chat_message("assistant"):
            st.write(bot_response)

    except Exception as e:
        st.error(f"오류가 발생했습니다: {e}")
