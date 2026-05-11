import streamlit as st
import google.generativeai as genai

st.title("💬 Chatbot")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

if "messages" not in st.session_state:
	st.session_state.messages = []

for msg in st.session_state.messages:
	with st.chat_message(msg["role"]):
		st.write(msg["content"])

if prompt := st.chat_input("請輸入訊息..."):
	st.session_state.messages.append({"role": "user", "content": prompt})
	with st.chat_message("user"):
		st.write(prompt)

	try:
		response = model.generate_content(prompt)
		reply = response.text

		st.session_state.messages.append({"role": "assistant", "content": reply})
		with st.chat_message("assistant"):
			st.write(reply)
	except Exception as e:
		st.error(f"Error generating response: {e}")
sed -i 's/gemini-2.0-flash/gemini-2.0-flash/g' streamlit_app.py && git add . && git commit -m "update model" && git push