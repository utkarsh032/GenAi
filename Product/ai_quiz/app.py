import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from quiz_data import questions

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        pass

    def transform(self, frame):
        return frame

def display_question(question, options):
    st.write(f"**{question}**")
    return st.radio("", options, key=question)

def main():
    # Add custom CSS for styling
    st.markdown("""
        <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .stTitle {
            color: rgb(30, 144, 255); /* Dodger Blue for title */
            text-align: center;
            
        }
        .button-container {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .button-container > button {
            width: 100px;
            height: 40px;
            background-color: rgb(30, 144, 255); /* Dodger Blue for buttons */
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .button-container > button:hover {
            background-color: rgb(0, 0, 255); /* Darker blue for hover effect */
        }
        
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="stTitle">Quiz App</div>', unsafe_allow_html=True)

    # Initialize session state
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.answers = [None] * len(questions)
        st.session_state.finished = False
        st.session_state.submitted = False
    
    if st.session_state.finished:
        # Display final score
        score = sum([1 for i in range(len(questions)) if st.session_state.answers[i] == questions[i]['answer']])
        st.write(f"Your final score is: {score}/{len(questions)}")
        st.button("Restart Quiz", on_click=lambda: st.session_state.update({'question_index': 0, 'answers': [None] * len(questions), 'finished': False, 'submitted': False}))
        return

    # Show the current question
    current_index = st.session_state.question_index
    current_question = questions[current_index]

    # Display the question and get the selected option
    if not st.session_state.submitted:
        st.markdown('<div class="question-container">', unsafe_allow_html=True)
        answer = display_question(current_question['question'], current_question['options'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            if current_index > 0:
                if st.button("Previous"):
                    st.session_state.question_index -= 1

        with col2:
            if st.button("Next"):
                st.session_state.answers[current_index] = answer
                st.session_state.question_index += 1
                st.session_state.submitted = False
        
        with col3:
            if current_index == len(questions) - 1:
                if st.button("Finish"):
                    st.session_state.answers[current_index] = answer
                    st.session_state.finished = True
                    st.session_state.submitted = True

    else:
        # Redirect to the final score display
        st.write("Review your answers and click Finish to see your score.")
        st.button("Finish", on_click=lambda: st.session_state.update({'finished': True, 'submitted': False}))

    # Display webcam feed in the top right corner
    st.markdown('<div class="webcam-container">', unsafe_allow_html=True)
    st.write("Webcam Feed")
    webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
