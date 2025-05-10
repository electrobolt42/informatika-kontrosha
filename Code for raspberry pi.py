import cv2
from picamera2 import Picamera2

# Инициализация камеры
picam2 = Picamera2()

# Настройка конфигурации для предпросмотра
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)

# Запуск камеры
picam2.start()

try:
    while True:
        # Получение кадра с камеры
        frame = picam2.capture_array()
        
        # Конвертация из RGB (который использует picamera2) в BGR (который использует OpenCV)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Отображение кадра
        cv2.imshow('Raspberry Pi Camera', frame)
        
        # Выход по нажатию 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Остановка камеры и закрытие окон
    picam2.stop()
    cv2.destroyAllWindows()
