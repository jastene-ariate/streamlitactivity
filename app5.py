import streamlit as st
import cv2
import numpy as np

# Set up the webcam capture (use index 0 for default webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    st.error("Error: Could not open webcam.")
else:
    st.title("🎥 Real-Time Video Stream with OpenCV")
    st.text("This is a real-time video stream using OpenCV and Streamlit.")
    
    # Stream the video
    frame_window = st.image([])  # Placeholder for the image to be updated

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            st.error("Error: Failed to capture frame.")
            break

        # Convert the frame from BGR to RGB (Streamlit expects RGB)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in Streamlit
        frame_window.image(frame_rgb)

        # Add a dynamic key to the button to prevent duplicate element keys
        if st.button("Stop Video Stream", key=f"stop_video_button_{st.session_state.get('frame_count', 0)}"):
            break

        # Increase the frame count for the dynamic key
        st.session_state['frame_count'] = st.session_state.get('frame_count', 0) + 1

    # Release the capture when done
    cap.release()
