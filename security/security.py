from datetime import datetime

def log_event(event_type, message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"{timestamp} - {event_type} - {message}\n"
    
    with open('audit_log.txt', 'a') as f:
        f.write(entry)