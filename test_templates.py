try:
    from src.templates import get_python_prompt
    print("Import successful")
    prompt = get_python_prompt()
    print(f"Prompt generated: {prompt[:50]}...")
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
