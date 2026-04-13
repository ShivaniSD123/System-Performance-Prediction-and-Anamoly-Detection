import os

def send_notification(title, message):
    try:
        from plyer import notification
        notification.notify(
            title=title,
            message=message,
            timeout=5
        )
    except:
        # 🔥 Fallback for macOS
        try:
            os.system(f'''
            osascript -e 'display notification "{message}" with title "{title}"'
            ''')
        except:
            # Final fallback (console)
            print(f"[NOTIFICATION] {title}: {message}")
