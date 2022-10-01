# Project Digital emotions for Tot-hackathon 1.10.22
____

# Обзор
Project Digital - это сервис для создания эмоций в digital-формате, реализованный на языке Python в виде телеграмм бота.


# Что он может
- [Распознавание голоса и перевод в текстовый формат](https://github.com/dying-dwg/Digital_emotions#Распознавание-голоса-и-перевод-в-текстовый-формат)
- [Распознавание эмоций в голосе](https://github.com/dying-dwg/Digital_emotions#Распознавание-эмоций-в-голосе)

# Планируется реализовать
- Отправка цифровых эмодзи
- Отправка AR Emoji в зависимости от настроения
- Добавление в цифровые эмодзи фона в зависимости от обстановки




## Распознавание голоса и перевод в текстовый формат
Для распознавание речи использовалась библиотека Speech Recognition - это инструмент для передачи речевых API от компаний Google, Microsoft, Sound Hound, IBM, Pocketsphinx, о работе данной библиотеке больше информации можно узнать в статье на [habr.ru](https://habr.com/ru/post/577806/)

## Распознавание эмоций в голосе
Для распознование эмоций в голосе использовали библиотеки [tensorflow](https://pypi.org/project/tensorflow/), [librosa](https://pypi.org/project/librosa/), [numpy](https://pypi.org/project/numpy/), [pandas](https://pypi.org/project/pandas/), [soundfile](https://pypi.org/project/soundfile/0.9.0/), wave, [scikit-learn](https://pypi.org/project/scikit-learn/0.24.2/), tqdm, [matplotlib](https://pypi.org/project/matplotlib/2.2.3/), pyaudio, также использовался открытый код [Emotion recognition using speech](https://github.com/x4nth055/emotion-recognition-using-speech).

В данной версии доступно 9 различных эмоций: 
1. Нейтральная
2. Спокойная
3. Радостная
4. Грустная
5. Сердитая
6. Страх
7. Отвращение
8. Удивление
9. Скука

## Отправка цифровых эмодзи
Данная функция принимает на вход голосовое сообщение от человека, распазнает 


C4Context
title System Context diagram for Internet Banking System

Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
Person(customerB, "Banking Customer B")
Person_Ext(customerC, "Banking Customer C")
System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

Enterprise_Boundary(b1, "BankBoundary") {

  SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

  System_Boundary(b2, "BankBoundary2") {
    System(SystemA, "Banking System A")
    System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts.")
  }

  System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
  SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

  Boundary(b3, "BankBoundary3", "boundary") {
    SystemQueue(SystemF, "Banking System F Queue", "A system of the bank, with personal bank accounts.")
    SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
  }
}

BiRel(customerA, SystemAA, "Uses")
BiRel(SystemAA, SystemE, "Uses")
Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
Rel(SystemC, customerA, "Sends e-mails to")
