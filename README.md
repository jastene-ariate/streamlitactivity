code6
![Screenshot 2025-05-07 235612](https://github.com/user-attachments/assets/bb91ce6a-f736-4127-a55b-6d372452571c)
![Screenshot 2025-05-07 235623](https://github.com/user-attachments/assets/e801d012-a329-46ec-a9e6-a2fdb14e2bfc)
output
![Screenshot 2025-05-07 232850](https://github.com/user-attachments/assets/f49a4e9d-da20-40b9-b5c2-58a3b78039fd)
![Screenshot 2025-05-07 232902](https://github.com/user-attachments/assets/11bb0444-03f9-49e4-9ddb-4e8ab581c5c0)

explanation
This Streamlit app captures a real-time video stream using OpenCV and displays it directly in the browser. The webcam feed is captured using OpenCV's cv2.VideoCapture function, and each frame is converted from BGR to RGB format (since Streamlit expects RGB) before being displayed. The app continuously updates the video feed in real-time within the Streamlit interface. A button is included to allow users to stop the video stream when needed, and dynamic keys are used for the button to ensure there are no duplicate elements. The webcam capture is released when the stream is stopped. If there are any issues, such as failure to access the webcam or capture frames, appropriate error messages are displayed.

