import io
import sys
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so your HTML page can communicate with this Flask server
CORS(app)

def trace_execution(code_string):
    """
    Executes Python code and captures a simplified trace of line execution,
    variable states, and print output.
    """
    trace = []
    original_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output  # Redirect stdout to capture print statements

    # Store global and local variables at each line
    def tracer(frame, event, arg):
        if event == 'line':
            lineno = frame.f_lineno
            filename = frame.f_code.co_filename
            # Only trace code from the user's input string, not internal Python files
            if filename == '<string>':
                # Capture local variables
                locals_copy = {k: repr(v) for k, v in frame.f_locals.items() if not k.startswith('__')}
                # Capture global variables that are not shadowed by locals
                globals_copy = {k: repr(v) for k, v in frame.f_globals.items() if not k.startswith('__') and k not in frame.f_locals}

                trace.append({
                    'type': 'line',
                    'line_number': lineno,
                    'variables': locals_copy,
                    'globals': globals_copy
                })
        return tracer

    sys.settrace(tracer) # Start tracing
    try:
        # Execute the user's code. '<string>' is a placeholder filename.
        exec(code_string, globals(), locals())
    except Exception as e:
        trace.append({'type': 'error', 'message': str(e)})
    finally:
        sys.settrace(None) # Stop tracing
        sys.stdout = original_stdout # Restore original stdout
        # Append captured print output to the trace
        captured_output = redirected_output.getvalue()
        if captured_output:
            trace.append({'type': 'output', 'content': captured_output})

    return trace

@app.route('/run-code', methods=['POST'])
def run_code():
    """
    API endpoint to receive Python code and return its execution trace.
    """
    data = request.get_json()
    code = data.get('code', '')
    if not code:
        return jsonify({"error": "No code provided"}), 400

    execution_trace = trace_execution(code)
    return jsonify(execution_trace)

if __name__ == '__main__':
    # Run the Flask development server
    # In a production environment, use a more robust WSGI server like Gunicorn or uWSGI
    app.run(debug=True, port=5000)