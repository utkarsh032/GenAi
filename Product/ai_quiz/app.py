import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from quiz_data import questions

class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        pass

    def transform(self, frame):
        return frame

def display_question(question, options):
    st.write(question)
    return st.radio("Choose an option:", options, key=question)

def main():
    st.title("Quiz App")

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
        answer = display_question(current_question['question'], current_question['options'])
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 2, 1])

        if current_index > 0:
            if col1.button("Previous"):
                st.session_state.question_index -= 1

        if col2.button("Next"):
            st.session_state.answers[current_index] = answer
            st.session_state.question_index += 1
            st.session_state.submitted = False
        
        if current_index == len(questions) - 1:
            if col2.button("Finish"):
                st.session_state.answers[current_index] = answer
                st.session_state.finished = True
                st.session_state.submitted = True

    else:
        # Redirect to the final score display
        st.write("Review your answers and click Finish to see your score.")
        st.button("Finish", on_click=lambda: st.session_state.update({'finished': True, 'submitted': False}))

    # Display webcam feed
    col1, col2 = st.columns([3, 1])  # Create two columns for layout
    with col2:
        st.write("Webcam Feed")
        webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

if __name__ == "__main__":
    main()
