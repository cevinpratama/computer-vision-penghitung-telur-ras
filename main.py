from ultralytics import YOLO
import cv2
import supervision as sv

MODEL_PATH = 'best.pt'
SOURCE_PATH = 0

LINE_START = sv.Point(320, 0)
LINE_END = sv.Point(320, 480)


model = YOLO(MODEL_PATH)

tracker = sv.ByteTrack(
    track_activation_threshold=0.25,
    lost_track_buffer=60,
    minimum_matching_threshold=0.8,
    frame_rate=30
)

line_zone = sv.LineZone(start=LINE_START, end=LINE_END)


line_annotator = sv.LineZoneAnnotator(
    thickness=2, 
    text_thickness=1, 
    text_scale=0.5,
    display_in_count=False,
    display_out_count=False
)

box_annotator = sv.BoxAnnotator(
    thickness=2,
)
label_annotator = sv.LabelAnnotator(
    text_scale=0.5, 
    text_thickness=1, 
    text_position=sv.Position.BOTTOM_CENTER
)

cap = cv2.VideoCapture(SOURCE_PATH)

print("🚀 Memulai deteksi... Tekan 'q' pada jendela yang muncul untuk keluar.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, stream=True, conf=0.4)

    for res in results:
        detections = sv.Detections.from_ultralytics(res)
        tracked_detections = tracker.update_with_detections(detections=detections)
        line_zone.trigger(detections=tracked_detections)

        labels = [
            f"ID:{tracker_id}"
            for tracker_id
            in tracked_detections.tracker_id
        ]

        annotated_frame = frame.copy()
        annotated_frame = box_annotator.annotate(
            scene=annotated_frame,
            detections=tracked_detections
        )
        annotated_frame = label_annotator.annotate(
            scene=annotated_frame,
            detections=tracked_detections,
            labels=labels
        )
        

        line_annotator.annotate(frame=annotated_frame, line_counter=line_zone)
        
        total_count = line_zone.in_count
        text = f"Total Telur: {total_count}"
        
        cv2.putText(
            annotated_frame,
            text,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0, 255, 0),
            3
        )
        
        cv2.imshow("Deteksi & Counting Telur", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Deteksi selesai.")