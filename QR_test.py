import cv2
import sqlitepractice as sp
from pyzbar.pyzbar import decode


db = sp.Database()
db.create_table()

# 카메라 장치 연결 (0번 카메라, 필요에 따라 인덱스 변경)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # pyzbar를 사용하여 바코드/QR 코드 디코딩
    decoded_data = decode(frame)

    if decoded_data:
        for data in decoded_data:
            symbol_type = data.type
            code_data = data.data.decode('utf-8')
            polygon = data.polygon
            
            # 코드 영역 표시 (이미지와 동일)
            n = len(polygon)
            for i in range(n):
                cv2.line(frame, polygon[i], polygon[(i+1) % n], (0, 255, 0), 2)
            cv2.putText(frame, code_data, polygon[0], cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
            if db.compare(code_data):
                print(f"Type: {symbol_type}, Data: {code_data}")
                db.insert_bar_qr((symbol_type,code_data))
            else:
                continue


            # # 코드 영역 표시 (이미지와 동일)
            # n = len(polygon)
            # for i in range(n):
            #     cv2.line(frame, polygon[i], polygon[(i+1) % n], (0, 255, 0), 2)
            # cv2.putText(frame, code_data, polygon[0], cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            

    # 영상 프레임 표시
    cv2.imshow("Real-time Barcode/QR Code Detection", frame)

    # 'q' 키를 누르면 종료(다른거 추가해봄봄)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('x'):
        db.reset_table()
        db.create_table()
        

# 카메라 장치 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()