# Virtual Hand Gesture Calculator

A **virtual calculator** that uses hand gestures for input, built using OpenCV, the `cvzone` HandTracking module, and Python's `pyttsx3` for voice output. This project leverages a webcam to detect finger positions and simulate button presses on a virtual calculator.

## Features

- **Gesture-Based Input**: Control the calculator using hand gestures (specifically the index and middle fingers) tracked via webcam.
- **Real-time Feedback**: Displays the calculator's interface and your equation in real time on the screen.
- **Text-to-Speech (TTS)**: Provides voice feedback, such as announcing errors or when the calculator starts.
- **Basic Operations**: Supports fundamental operations like addition, subtraction, multiplication, division, and parentheses for complex expressions.
- **Clear and Delete Function**: Use `C` to clear the equation or `del` to delete the last input.

## Demo

![Virtual Calculator Demo](demo-gif-link) *(Include a link or gif showing the calculator in action)*

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- cvzone HandTrackingModule (`cvzone`)
- pyttsx3 (for Text-to-Speech)

You can install the necessary libraries with:

```bash
pip install opencv-python cvzone pyttsx3
```

## How It Works

1. **Hand Detection**: The code uses `cvzone` to detect the hand and track finger positions.
2. **Button Interaction**: When the distance between the index and middle fingers becomes small enough, the code registers it as a "click" and interacts with the buttons.
3. **TTS Integration**: The `pyttsx3` library gives voice feedback. For example, it announces the starting of the calculator and reads errors like "Syntax Error."

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/whisplnspace/CalCit.git
   cd virtual-hand-calculator
   ```

2. **Install Dependencies**:

   Install the required Python libraries using `pip`:

   ```bash
   pip install opencv-python cvzone pyttsx3
   ```

3. **Run the Program**:

   Run the `main.py` file using Python:

   ```bash
   python main.py
   ```

   Make sure your webcam is active and functioning, as the hand tracking requires a live video feed.

## Usage

- Use your **index and middle fingers** to "click" on the virtual buttons.
- Basic mathematical operations such as addition (+), subtraction (-), multiplication (*), division (/), and parentheses can be performed.
- Click the `=` button to evaluate the expression.
- Press `C` to clear the current equation or `del` to delete the last character.

### Keyboard Controls:

- **Press 'q'**: Close the program and exit.

## Screenshots

### Calculator Interface
![Calculator Interface](screenshot-link)

*(Include a screenshot of the calculator interface here.)*

## Future Improvements

- **Advanced Features**: Add more complex operations such as trigonometry, exponents, etc.
- **Enhanced Gesture Recognition**: Implement multi-hand tracking and gestures for specific operations.
- **Customization**: Allow users to customize button layout and themes.
Here’s a **Collaboration** section that you can add to your GitHub README:

---

## Collaboration

We welcome contributions from the community! If you're interested in improving the project or adding new features, feel free to get involved.

### How to Contribute

1. **Fork the Repository**: Click on the "Fork" button at the top of this page to create a copy of the repository on your GitHub account.
   
2. **Clone Your Fork**: Clone the repository to your local machine.

   ```bash
   git clone https://github.com/whisplnspace/calCit.git
   ```

3. **Create a New Branch**: Create a branch for your feature or bug fix.

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Changes**: Implement your feature or bug fix in the new branch.

5. **Commit Your Changes**: Once your changes are ready, commit them to your local repository.

   ```bash
   git add .
   git commit -m "Add your commit message here"
   ```

6. **Push to GitHub**: Push the changes back to your forked repository.

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**: Go to the original repository on GitHub and open a Pull Request. Provide a detailed explanation of the changes you made and why they are necessary.

### Reporting Issues

If you find any bugs or have suggestions for improvements, please open an issue on the [Issues](https://github.com/whisplnspace/CalCit/issues) page. Be as detailed as possible, providing steps to reproduce the issue or specific suggestions for enhancement.

---
