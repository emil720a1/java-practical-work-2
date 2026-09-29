# Практична робота № 2 з ООП у Java

Практична робота з дисципліни «Конструювання програмного забезпечення Java».

## Автор

- Студент: Бондаренко Олег Вікторович
- Група: ТЦР-31
- Варіант: 0
- Клас-сутність: `Book`

## Мета роботи

Дослідити модифікатори доступу, конструктори, `this`, `static` і `final` у Java на прикладі класу `Book`.

## Структура проєкту

```text
src/
├── app/
│   └── Main.java
└── model/
    ├── Book.java
    └── ModelTest.java
```

Звіт міститься у файлі `outputs/zvit_praktychna_robota_2_bondarenko.docx`.

## Запуск

```bash
mkdir -p build
javac -d build src/model/Book.java src/model/ModelTest.java src/app/Main.java
java -cp build app.Main
```

## Результат

Програма створює об’єкти `Book` трьома способами, демонструє роботу конструкторів і виводить значення спільного статичного лічильника:

```text
1: Без назви — Невідомий автор, 0
2: Кобзар — Невідомий автор, 0
3: Java — Herbert Schildt, 2022
3
```
