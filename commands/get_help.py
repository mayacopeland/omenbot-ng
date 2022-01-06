def send_help() -> str:
    # could maybe categorise it?
    return """
    ```Currently handled commands:
    - help              displays this message
    - runtimes          shows all the languages omenbot can run
    - run               runs code in a given block (run <language> <code block>) 
    - inspire           shows a very inspirational message
    - roll              roll a number
    
    Admins:
    - remind            reminds everyone of coursework due
    - warn              warns of current topic <topic/rules/spam>
    - update_presence   update's presence with string given

    Source Code: https://github.com/mayacopeland/omenbot-ng
    [Licensed under Apache 2.0]
    ```
    """