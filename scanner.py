import cv2
from graphviz import Digraph

# --- Initialize webcam ---
cap = cv2.VideoCapture(0)

# --- Load authorized names ---
with open('Resources/name_list.txt') as file:
    myDataList = [line.strip().lower() for line in file.readlines()]


# --- QR detector ---
detector = cv2.QRCodeDetector()
from graphviz import Digraph

dot = Digraph(comment='QR Scanner NFA')

# States q0, q1, q2, q3, q4, q5
dot.node('q0', 'q0')  # Start
dot.node('q1', 'q1')  # QR_Detected
dot.node('q2', 'q2')  # Decode_Attempt
dot.node('q3', 'q3')  # Success
dot.node('q4', 'q4')  # Failure
dot.node('q5', 'q5')  # End

# Transitions (multiple allowed)
dot.edge('q0', 'q1', 'QR detected')
dot.edge('q1', 'q2', 'Attempt decode')
dot.edge('q2', 'q3', 'Decode success')
dot.edge('q2', 'q4', 'Decode fail')  # NFA allows multiple outcomes
dot.edge('q3', 'q5', 'Esc')
dot.edge('q4', 'q5', 'Esc')
dot.edge('q0', 'q5', 'Esc')  # escape from start

# Optional: epsilon transition
dot.edge('q1', 'q4', 'ε')  # skip decoding if error occurs

dot.render('qr_scanner_nfa_q', format='png', cleanup=True)
print("NFA diagram saved as qr_scanner_nfa_q.png")

# --- Create DFA diagram ---
from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment='QR Scanner DFA')

# DFA states as q0, q1, q2...
dot.node('q0', 'q0')  # Start
dot.node('q1', 'q1')  # QR_Detected
dot.node('q2', 'q2')  # Decode_Success
dot.node('q3', 'q3')  # Authorized
dot.node('q4', 'q4')  # UnAuthorized
dot.node('q5', 'q5')  # End

# Transitions
dot.edge('q0', 'q1', 'QR detected')
dot.edge('q1', 'q2', 'Decode successful')
dot.edge('q2', 'q3', 'Data in list')
dot.edge('q2', 'q4', 'Data not in list')
dot.edge('q0', 'q5', 'Esc')
dot.edge('q1', 'q5', 'Esc')
dot.edge('q2', 'q5', 'Esc')
dot.edge('q3', 'q5', 'Esc')
dot.edge('q4', 'q5', 'Esc')

# Render graph
dot.render('qr_scanner_dfa_q', format='png', cleanup=True)
print("DFA diagram saved as qr_scanner_dfa_q.png")


# --- DFA simulation function ---
def get_state(data, detected):
    if not detected:
        return 'S'
    if detected and not data:
        return 'D'
    if data:
        if data.strip().lower() in myDataList:  # normalize
            return 'A'
        else:
            return 'U'


# --- Main loop ---
while True:
    ret, img = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(img)
    detected = bbox is not None

    current_state = get_state(data, detected)

    # Draw QR polygon
    if detected:
        for i in range(len(bbox)):
            pt1 = (int(bbox[i][0][0]), int(bbox[i][0][1]))
            pt2 = (int(bbox[(i + 1) % len(bbox)][0][0]), int(bbox[(i + 1) % len(bbox)][0][1]))
            cv2.line(img, pt1, pt2, (255, 0, 0), 2)

        if data:
    # Normalize both sides
            person_name = data.strip().lower()  
            print(f"NAME OF PERSON: {data}")
            
            if person_name in myDataList:
                outputText = "Authorized"
                outputColor = (0, 255, 0)
            else:
                outputText = "Un-Authorized"
                outputColor = (0, 0, 255)

            cv2.putText(img, f"{outputText} (State: {current_state})",
                (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, outputColor, 2)

    else:
        # Show current state when no QR detected
        cv2.putText(img, f"State: {current_state}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 0), 2)

    cv2.imshow("QR Code Scanner with DFA/NFA", img)

    if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
        break

cap.release()
cv2.destroyAllWindows()
