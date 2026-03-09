from transcribe import transcribeAudio
import streamlit as st
import tempfile
from streamlit_mic_recorder import mic_recorder
import os
st.set_page_config(layout="wide")
st.markdown(
    "<h1 style='font-size:48px;'>🎸 Melody → Guitar Tab Transcriber</h1>",
    unsafe_allow_html=True
)
st.write("upload or record an audio file to generate tabs in seconds")
st.subheader("Upload Audio")
up_file=st.file_uploader(
    "Upload audio",
    type=["wav", "mp3", "m4a", "flac", "ogg"]
)



if up_file is not None:

    suffix="."+up_file.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(delete=False,suffix=suffix) as tmp:
        tmp.write(up_file.read())
        filepath=tmp.name

    with st.spinner("generating tabs..."):
        tab,wav_path=transcribeAudio(filepath)

    st.subheader("Generated Tabs:")
    st.success("Transcription complete!")
    
    tab_text = "\n".join(tab)
    # for line in tab:
    st.code("\n".join(tab))
    st.subheader("playback")
    if os.path.exists(wav_path):
        with open(wav_path, "rb") as f:
         audio_bytes = f.read()

        st.audio(audio_bytes)

st.divider()

st.subheader("Record Audio")

audio=mic_recorder(
    start_prompt="start_recording",
    stop_prompt="stop_recording",
    key="recorder"
)

if audio:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio["bytes"])
        filepath = f.name

    st.audio(audio["bytes"])

    with st.spinner("Transcribing..."):
        tab,wav_path = transcribeAudio(filepath)
        st.write("wav path:", wav_path)
        st.write("exists:", os.path.exists(wav_path))

    st.success("Transcription complete!")
    tab_text = "\n".join(tab)
    # for line in tab:
    st.code("\n".join(tab))
    st.subheader("playback")
    if os.path.exists(wav_path):
        with open(wav_path, "rb") as f:
         audio_bytes = f.read()

        st.audio(audio_bytes)