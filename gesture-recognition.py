def recognize_gesture(landmarks):
    """
    Classifies hand gesture using landmark positions
    """

    thumb_tip = landmarks[4].y
    index_tip = landmarks[8].y
    middle_tip = landmarks[12].y
    ring_tip = landmarks[16].y
    pinky_tip = landmarks[20].y

    # Thumbs Up
    if thumb_tip < index_tip and middle_tip > index_tip:
        return "Thumbs Up"

    # Fist
    if (index_tip > landmarks[6].y and
        middle_tip > landmarks[10].y and
        ring_tip > landmarks[14].y and
        pinky_tip > landmarks[18].y):
        return "Fist"

    # Open Palm
    if (index_tip < landmarks[6].y and
        middle_tip < landmarks[10].y and
        ring_tip < landmarks[14].y and
        pinky_tip < landmarks[18].y):
        return "Open Palm"

    return "Unknown"
