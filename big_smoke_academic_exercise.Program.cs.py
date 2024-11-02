Sure! Here’s a humorous academic exercise program, based on **Big Smoke’s infamous order** from *GTA: San Andreas*. In this exercise, we turn Big Smoke's fast-food order into a structured program. We will simulate an academic exercise where a student needs to create a large and complicated order as part of their task.

### Big Smoke Academic Exercise Program (Python)

```python
class BigSmokeOrder:
    def __init__(self):
        self.order = []

    def add_item(self, item: str):
        self.order.append(item)
        print(f"Added {item} to the order.")

    def place_order(self):
        if len(self.order) == 0:
            print("No items in the order!")
            return
        print("\nBig Smoke's Full Order:")
        for item in self.order:
            print(f"- {item}")
        print("\nThat's a huge order!")

def big_smoke_academic_exercise():
    print("Welcome to the Big Smoke Academic Exercise!\n")
    print("Your task: Simulate Big Smoke's legendary order with correct structure and sequencing.")
    
    # Initialize Big Smoke's order
    big_smoke_order = BigSmokeOrder()
    
    # Let's add Big Smoke's full order
    big_smoke_order.add_item("Two Number 9s")
    big_smoke_order.add_item("A Number 9 Large")
    big_smoke_order.add_item("A Number 6 with Extra Dip")
    big_smoke_order.add_item("A Number 7")
    big_smoke_order.add_item("Two Number 45s, one with Cheese")
    big_smoke_order.add_item("And a Large Soda")
    
    # Place the full order
    big_smoke_order.place_order()

if __name__ == "__main__":
    big_smoke_academic_exercise()
```

### Output of the Program:

```text
Welcome to the Big Smoke Academic Exercise!

Your task: Simulate Big Smoke's legendary order with correct structure and sequencing.

Added Two Number 9s to the order.
Added A Number 9 Large to the order.
Added A Number 6 with Extra Dip to the order.
Added A Number 7 to the order.
Added Two Number 45s, one with Cheese to the order.
Added And a Large Soda to the order.

Big Smoke's Full Order:
- Two Number 9s
- A Number 9 Large
- A Number 6 with Extra Dip
- A Number 7
- Two Number 45s, one with Cheese
- And a Large Soda

That's a huge order!
```

### 中文

這是一個基於 Big Smoke 著名訂單的學術練習程序，它將這個複雜的點餐模擬為學術作業：

```python
class BigSmokeOrder:
    def __init__(self):
        self.order = []

    def add_item(self, item: str):
        self.order.append(item)
        print(f"已將 {item} 加入訂單。")

    def place_order(self):
        if len(self.order) == 0:
            print("訂單內沒有項目！")
            return
        print("\nBig Smoke 的完整訂單：")
        for item in self.order:
            print(f"- {item}")
        print("\n這是一個巨大的訂單！")

def big_smoke_academic_exercise():
    print("歡迎參加 Big Smoke 學術練習！\n")
    print("您的任務是：按照正確的結構和順序模擬 Big Smoke 的經典訂單。")
    
    # 初始化 Big Smoke 的訂單
    big_smoke_order = BigSmokeOrder()
    
    # 加入 Big Smoke 的完整訂單
    big_smoke_order.add_item("兩個 9 號餐")
    big_smoke_order.add_item("一個大號 9 號餐")
    big_smoke_order.add_item("一個 6 號餐，額外加醬")
    big_smoke_order.add_item("一個 7 號餐")
    big_smoke_order.add_item("兩個 45 號餐，一個加芝士")
    big_smoke_order.add_item("一杯大號汽水")
    
    # 下達完整訂單
    big_smoke_order.place_order()

if __name__ == "__main__":
    big_smoke_academic_exercise()
```

### Formal English

This is an academic exercise simulating Big Smoke's famous fast-food order. The exercise program uses object-oriented programming principles to structure the task:

```python
class BigSmokeOrder:
    def __init__(self):
        self.order = []

    def add_item(self, item: str):
        self.order.append(item)
        print(f"Added {item} to the order.")

    def place_order(self):
        if len(self.order) == 0:
            print("No items in the order!")
            return
        print("\nBig Smoke's Full Order:")
        for item in self.order:
            print(f"- {item}")
        print("\nThat's a huge order!")

def big_smoke_academic_exercise():
    print("Welcome to the Big Smoke Academic Exercise!\n")
    print("Your task: Simulate Big Smoke's legendary order with correct structure and sequencing.")
    
    big_smoke_order = BigSmokeOrder()
    
    big_smoke_order.add_item("Two Number 9s")
    big_smoke_order.add_item("A Number 9 Large")
    big_smoke_order.add_item("A Number 6 with Extra Dip")
    big_smoke_order.add_item("A Number 7")
    big_smoke_order.add_item("Two Number 45s, one with Cheese")
    big_smoke_order.add_item("And a Large Soda")
    
    big_smoke_order.place_order()

if __name__ == "__main__":
    big_smoke_academic_exercise()
```

### Español

Este es un ejercicio académico que simula el famoso pedido de Big Smoke. El programa utiliza programación orientada a objetos para estructurar el pedido:

```python
class BigSmokeOrder:
    def __init__(self):
        self.order = []

    def add_item(self, item: str):
        self.order.append(item)
        print(f"Añadido {item} al pedido.")

    def place_order(self):
        if len(self.order) == 0:
            print("¡No hay artículos en el pedido!")
            return
        print("\nPedido completo de Big Smoke:")
        for item in self.order:
            print(f"- {item}")
        print("\n¡Es un pedido enorme!")

def big_smoke_academic_exercise():
    print("¡Bienvenido al ejercicio académico de Big Smoke!\n")
    print("Tu tarea: Simular el legendario pedido de Big Smoke con la estructura y secuencia correctas.")
    
    big_smoke_order = BigSmokeOrder()
    
    big_smoke_order.add_item("Dos Número 9")
    big_smoke_order.add_item("Un Número 9 Grande")
    big_smoke_order.add_item("Un Número 6 con Extra Salsa")
    big_smoke_order.add_item("Un Número 7")
    big_smoke_order.add_item("Dos Número 45, uno con Queso")
    big_smoke_order.add_item("Y un Refresco Grande")
    
    big_smoke_order.place_order()

if __name__ == "__main__":
    big_smoke_academic_exercise()
```

### 文言文

此乃基於 Big Smoke 著名之訂單所作學術練習，按序模擬其複雜之點餐過程：

```python
class BigSmokeOrder:
    def __init__(self):
        self.order = []

    def add_item(self, item: str):
        self.order.append(item)
        print(f"已加 {item} 於訂單中。")

    def place_order(self):
        if len(self.order) == 0:
            print("訂單中無物！")
            return
        print("\nBig Smoke 全單：")
        for item in self.order:
            print(f"- {item}")
        print("\n此單甚巨！")

def big_smoke_academic_exercise():
    print("迎至 Big Smoke 學術練習！\n")
    print("汝任務：按正確次序模擬 Big Smoke 之經典訂單。")
    
    big_smoke_order = BigSmokeOrder()
    
    big_smoke_order.add_item("兩份 9 號")
    big_smoke_order.add_item("一份大號 9 號")
    big_smoke_order.add_item("一份 6 號，多加醬")
    big_smoke_order.add_item("一份 7 號")
    big_smoke_order.add_item("兩份 45 號，其一加芝士")
    big_smoke_order.add_item("一杯大汽水")
    
    big_smoke_order.place_order()

if __name__ == "__main__":
    big_smoke_academic_exercise()
```

