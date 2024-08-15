import pyautogui
import pyperclip
import time

# Pause between actions to ensure they are executed properly
pyautogui.PAUSE = 0.5

# Step 1: Click on the icon at (1153, 1051)
pyautogui.click(1375, 1050)

# Step 2: Move to the start position of the text at (610, 204)
pyautogui.moveTo(620, 196)

# Step 3: Click and hold the mouse button
pyautogui.mouseDown()

# Step 4: Drag the mouse to the end position of the text at (1842, 926)
pyautogui.moveTo(1800, 901, duration=0.5)  # Adjust duration as needed

# Step 5: Release the mouse button to complete the drag
pyautogui.mouseUp()

# Step 6: Copy the selected text to the clipboard (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')

# Optional: Add a small delay to ensure the copy operation is complete
time.sleep(0.5)

# Step 7: Get the copied text from the clipboard and store it in a variable
copied_text = pyperclip.paste()

# Print the copied text (for debugging purposes)
print(copied_text)

# Your text is now stored in the variable 'copied_text'!
