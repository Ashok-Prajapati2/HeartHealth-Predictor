import streamlit as st
import re

class Calculator:
    def __init__(self):
        self.value = 0
        self.history = []

    def evaluate(self, expression):
        try:
            # Remove spaces from the expression
            expression = expression.replace(" ", "")
            
            # Define the allowed characters and match the expression
            if not re.match(r"^[0-9+\-*/%.()]*$", expression):
                raise ValueError("Invalid characters in the expression")
            
            # Perform the calculation manually
            result = self.calculate_expression(expression)
            self.value = result
            self.history.append(f"Evaluated expression: {expression} = {result}")
        except Exception as e:
            self.history.append(f"Error evaluating expression: {e}")
            result = None
        return result

    def calculate_expression(self, expression):
        # Convert the expression to a list of tokens
        tokens = re.findall(r"\d+\.\d+|\d+|[-+*/%()]", expression)
        
        # First, handle multiplication, division, and modulus (BODMAS order)
        tokens = self.handle_operations(tokens, ["*", "/", "%"])
        
        # Then, handle addition and subtraction
        result = self.handle_operations(tokens, ["+", "-"])
        
        return result

    def handle_operations(self, tokens, operations):
        # Perform operations in the correct order
        i = 0
        while i < len(tokens):
            if tokens[i] in operations:
                left = float(tokens[i - 1])
                right = float(tokens[i + 1])
                
                if tokens[i] == "+":
                    result = left + right
                elif tokens[i] == "-":
                    result = left - right
                elif tokens[i] == "*":
                    result = left * right
                elif tokens[i] == "/":
                    if right != 0:
                        result = left / right
                    else:
                        raise ZeroDivisionError("Division by zero")
                elif tokens[i] == "%":
                    result = left % right
                
                tokens[i - 1] = str(result)
                del tokens[i:i + 2]
                i -= 1
            i += 1
        return float(tokens[0])

    def get_result(self):
        return self.value

    def get_history(self):
        return self.history


# Initialize the Calculator object in session state if it does not exist yet
if "calc" not in st.session_state:
    st.session_state.calc = Calculator()

st.title("Interactive Calculator")

# Allow the user to input a mathematical expression
expression = st.text_input("Enter a mathematical expression (e.g., 1+2+57.6-6.5*8)", "")

if st.button("Evaluate Expression"):
    if expression:  # Check if the expression is not empty
        result = st.session_state.calc.evaluate(expression)
        if result is not None:
            st.write(f"Result: {result}")
    else:
        st.warning("Please enter a valid expression.")

# Display history
if st.button("Show History"):
    st.write("Operation History:")
    for item in st.session_state.calc.get_history():
        st.write(item)
