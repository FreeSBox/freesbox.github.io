---
weight: 1
bookFlatSection: true
title: "Поиск лагов"
---

# Ищем кто вызывает лаги

## Команда `findlag`

На сервере есть консольная команда `findlag`, она выдаёт насколько игрок нагружает сервер (в попугаях).

### Как работает findlag

1. Каждый разфриженный проп добавляет 0.5 попугаев
2. Каждый [проникающий](https://wiki.facepunch.com/gmod/PhysObj:IsPenetrating) проп добавляет 16 попугаев
3. Каждый constraint добавляет 0.5 попугаев
4. Каждый wire gate добавляет 1 попугай
5. Каждый E2/FPGA/SF chip добавляет execution time in ms*2 попугаев
6. Каждая включенная wire турель добавляет `0.05/Delay` попугаев, если у турели включен звук это число умножается на 10, если число пуль больше 5 то это число умножается на `Bullets per shot/4`

## Команда `findchips`

Выдаёт все Expression 2/FPGA/Starfall чипы на сервере.

Пример вывода команды:
```
| owner                  | E2 | Chip name                      | 0.5 ms |
| asshole                | SF | pasted blinder                 | 0.6 ms |
```

## `epoe`

**Доступно с роли operator и выше**

epoe передаёт серверные логи на легко видное окно в игре
![epoe in game](/media/epoe.png)

### Настройка

1. `+epoe`
2. Включить autologin
3. Включить show on activity
4. Включить In Ctx Menu (кнопки можно крутить на колёсико мыши)
5. `-epoe`

