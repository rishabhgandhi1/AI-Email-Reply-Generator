import requests
import streamlit as st

st.set_page_config(
    page_title="AI Email Reply Generator",
    page_icon="📧",
    layout="wide",
)

st.title("📧 AI Email Reply Generator")
st.caption("Generate professional email replies using Google's Gemini AI")

left, right = st.columns([2, 1])

with left:

    email = st.text_area(
        "Paste Email",
        height=350,
        placeholder="Paste your email here..."
    )
    st.caption(f"Characters: {len(email)}")

with right:

    tone = st.selectbox(
        "Reply Tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "HR",
            "Customer Support"
        ]
    )

    st.write("")

    generate = st.button(
    "🚀 Generate Reply",
    use_container_width=True,
    disabled=len(email.strip()) == 0
)

if generate:
    if not email.strip():
        st.warning("Please enter an email.")
    else:
        payload = {
            "email": email,
            "tone": tone
        }

        with st.spinner("Generating AI reply..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/generate",
                    json=payload
                )
                if response.status_code == 200:
                    reply = response.json()["reply"]
                    st.subheader("✨ Generated Reply")
                    st.text_area(
    "",
    value=reply,
    height=250,
    disabled=True
)

                    st.download_button(
    "📄 Download Reply",
    data=reply,
    file_name="email_reply.txt"
)
                    st.subheader("Generated Reply")
                    st.code(reply, language=None)
                else:
                    st.error(f"Backend Error ({response.status_code}): {response.text}")
            except Exception as e:
                st.error(str(e))