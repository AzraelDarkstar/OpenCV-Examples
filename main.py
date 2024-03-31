import cv2 as cv     # Импортируем OpenCV    

# Импортируем нужные нам функции tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showwarning

# Загружаем предобученные каскады для обнаружения лица и рук
face_cascade = cv.CascadeClassifier('Cascades\haarcascade_frontalface_default.xml')
hand_cascade = cv.CascadeClassifier('Cascades\haarcascade_hand.xml')
    

path = 'materials/Face and Hands.jpg'

# Функция для открытия файла
def file_open():
    global path
    path = filedialog.askopenfilename()
    print(path)


# Функция для обнаружения лиц и рук на изображении
def HandsFace():
    try:
        image = cv.imread(path)   # Загружаем изображение

        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  #Преобразовываем в черно-белый формат
    
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))         # Узнаем координаты лиц и обводим их
        for (x, y, w, h) in faces:
            cv.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv.putText(image, 'Face', (x, y-10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)
        
        hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.9, minNeighbors=3, minSize=(30, 30))          # Узнаем координаты рук и обводим их
        for (x, y, w, h) in hands:
            cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv.putText(image, 'Hand', (x, y-10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
        
         # Отображаем изображение с обнаруженными лицами и руками
        cv.imshow('Hands and Face', image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except Exception:         # Выводим сообщение об ошибке, если что-то пошло не так
        print('Неподходящий тип файла')
        showwarning(title='Ошибка', message='Неподходящий тип файла')

# Функция для обнаружения лиц на видеопотоке с веб-камеры
def webvideo():
    
    # Инициализируем видеопоток с веб-камеры
    cap = cv.VideoCapture(0)
    
    # Основной цикл
    while True:
        _, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))        # Поиск лиц на кадре
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 200, 0), 2)
            cv.putText(frame, 'Face', (x, y-10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
    
        cv.imshow('FaceDetectFromWeb', frame)     # Вывод кадра
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv.destroyAllWindows()

# Функция для обнаружения лиц на видеопотоке    
def fromvideo():
    try:
        cap = cv.VideoCapture(path)
        
        # Основной цикл 
        while True:
            _, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))         # Поиск лиц в кадре 
            for (x, y, w, h) in faces:
                cv.rectangle(frame, (x, y), (x+w, y+h), (255, 200, 0), 2)
                cv.putText(frame, 'Face', (x, y-10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)
        
            cv.imshow('FaceDetectFromWeb', frame)        # Вывод кадра
            
            if cv.waitKey(1) & 0xFF == ord('q'):          
                break
        
        cap.release()
        cv.destroyAllWindows()
    except Exception:                      
        print('Неподходящий тип файла')
        showwarning(title='Ошибка', message='Неподходящий тип файла')

# Создание окна      
root = Tk()

# Настройка окна
root.title('OpenCvExamples')
root.geometry('200x300')

# Создание виджетов и добавление их в основное окно
file_choose = ttk.Button(text='Выберите файл', command=file_open)
file_choose.pack()

HF = ttk.Button(text="Лицо и руки", command=HandsFace)
HF.pack()

WC = ttk.Button(text='Лицо на webкамере', command=webvideo)
WC.pack()

VC = ttk.Button(text='Лица на видео',command=fromvideo)
VC.pack()

root.mainloop()