# 🚗 Vehicle Inheritance in Python

This project demonstrates **Object-Oriented Programming (OOP)** in Python using **inheritance**.  
It features three vehicle types — **Car**, **Bike**, and **Truck** — each inheriting from a common `Vehicle` class.

---

## 📁 File Structure

- `vehicles.py` → Main Python script with class definitions and object usage  
- `README.md` → Project documentation (this file)

---

## 🧠 Concepts Used

- Classes and Objects  
- Inheritance  
- Method Overriding  
- Custom Methods per Subclass

---

## 🔧 Class Structure

### `Vehicle` (Base Class)
- `start()`
- `stop()`

### `Car` (Child of Vehicle)
- `play_music()`
- `turn_on_ac()`
- `open_sunroof()`
- `drive()`

### `Bike` (Child of Vehicle)
- `wheelie()`
- `kick_start()`
- `rev_engine()`
- `park()`

### `Truck` (Child of Vehicle)
- `load_cargo()`
- `unload_cargo()`
- `attach_trailer()`
- `detach_trailer()`
- `blow_horn()`

---

## 💻 Example Output

```bash
Mercedes is playing music 🎶
Mercedes's AC is now ON ❄️
Mercedes's sunroof is open 🌞
Mercedes is driving smoothly 🚗💨

BMW is doing a wheelie! 🏍️🔥
BMW is being kick-started 🔧
BMW revs its engine: VROOOM! 💥
BMW is parked using the side stand 🛑

Cadillac is loading cargo. 📦
Cadillac has unloaded the cargo. 🛻
Cadillac's trailer is now attached. 🔗
Cadillac's trailer has been detached. ❌
Cadillac is blowing its horn: HONK HONK! 🚚📣

