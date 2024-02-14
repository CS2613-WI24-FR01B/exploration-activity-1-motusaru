# Tkinter: Python's Standard GUI Library

## 1. Which package/library did you select?
I selected the Tkinter library in Python.

## 2. What is the package/library? What purpose does it serve? How do you use it?
Purpose:
Tkinter, standing for "Tk Interface" is Python's standard GUI (Graphical User Interface) library. It serves as a fundamental tool for building desktop applications with tools to create desktop applications. It offers a simple and easy-to-use way to build windows, frames, buttons, labels, and other GUI components. Some of its purposes include:
- GUI Development: Tkinter facilitates the creation of GUI applications by providing a set of widgets (such as buttons, labels, entry fields, checkboxes, radio buttons, etc.) that users can interact with. These widgets are essential components for building user-friendly interfaces where users can input data, make selections, and trigger actions.
- Integration with Python: Tkinter seamlessly integrates with Python, making it an attractive choice for Python developers. Being part of the Python standard library, Tkinter offers a familiar syntax and programming model to Python developers, reducing the learning curve for building GUI applications.
- Ease of Use: Tkinter is known for its simplicity and ease of use. It provides a straightforward API (Application Programming Interface) that allows developers to create GUI components and define their behavior with minimal effort. Tkinter's simplicity makes it accessible to beginners while still offering enough flexibility for advanced usage.
- Customizability: Tkinter provides extensive customization options for widgets, allowing developers to adjust their appearance and behavior to suit the application's requirements. Developers can specify attributes such as text, font, color, size, alignment, and more to create visually appealing interfaces.
- Geometry Management: Tkinter includes built-in geometry managers (pack(), grid(), and place()) that help developers organize and layout widgets within the application's window or frames. These managers simplify the process of arranging widgets in rows, columns, or specific positions, ensuring proper alignment and spacing.

Usage:
To use Tkinter, you need to import it into your Python script (`import tkinter as tk`) and then create instances of widgets like `Tk()`, `Button()`, `Entry()`, etc. You can configure these widgets with various options like text, size, color, and position. [1]

## 3. What are the main functionalities of the package/library?
Example code snippet:
```python
import tkinter as tk

def button_clicked():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("Tkinter Example")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click me", command=button_clicked)
button.pack()

root.mainloop()
```
- Import the tkinter module as tk.
- Define a function button_clicked() that changes the text of the label when the button is clicked.
- Create a root window (root) using tk.Tk() and set its title.
- Create a label (label) with the text "Hello, Tkinter!" and pack it into the root window using the pack() geometry manager.
- Create a button (button) with the text "Click me" and assign the button_clicked() function to it as a command.
- Pack the button into the root window.
- Start the Tkinter event loop with root.mainloop() to display the GUI and handle user interactions.

When you run this script, a window will appear with the label and button. Clicking the button will change the label text to "Button Clicked!". This example demonstrates the basic usage of Tkinter to create a simple GUI application in Python.

## 4. When was it created?
Tkinter was created as a GUI extension for the TCL scripting language in 1991 by John Ousterhout [2].

## 5. Why did you select this package/library?
Ever since I first learnt about GUIs in my Java-1 (CS1073) class, I was impressed at the versitality and flexibility offered by them and the ability to customize them completely as per your liking. I decided to explore Tkinter to gain further knowledge on how GUIs and how they can be implemented in Python. I also learnt that Tkinter is part of Python's standard library [3], ensuring its availability and compatibility across different Python installations.
As it is included with Python by default, there's no need for additional installations or dependencies, making it convenient to use. 

## 6. How did learning the package/library influence your learning of the language?
Learning Tkinter has enhanced my understanding of Python by allowing me to explore GUI development within the Python ecosystem. It broadened my knowledge of Python's abilities, allowing me to build interactive applications with graphical interfaces, which is both fun and useful! Additionally, understanding Tkinter's programming model has toned my grasp of Python's object-oriented and functional programming models. Along with this, having to work on this exploration activity allowed me to further improve my self-learning skills.

## 7. How was your overall experience with the package/library?
My overall experience with Tkinter has been positive. While it may not offer the most advanced features compared to other GUI libraries, its simplicity and ease of use make it an excellent choice for beginners and small to medium-sized projects. I would recommend Tkinter to anyone looking to create simple desktop applications in Python. Personally, I would continue using Tkinter to build lightweight applications where cross-platform compatibility are priorities. I think the most important part of this experience was realizing how enjoyable coding can be with the availability of so many different libraries and packages!  

## References given at the end:
[1]https://realpython.com/python-gui-tkinter/
[2]https://python-course.eu/tkinter/#:~:text=Tk%20is%20called%20Tkinter%20in,first%20release%20was%20in%201991 
[3]https://realpython.com/python-gui-tkinter/
