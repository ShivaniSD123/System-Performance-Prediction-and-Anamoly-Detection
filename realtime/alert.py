import notification
def alert(score, data, top_process):

    cpu = data["cpu_percent"]
    ram = data["ram_percent"]
    net = data["net_bytes_per_sec"]

    p = top_process[0]
    title = " System Alert"
    message = f"{p['name']} (PID {p['pid']})"

    
    if cpu > 80 and len(top_process) > 0:
        title = " CPU Spike"
        message = f"{p['name']} (PID {p['pid']}) using {p['cpu_percent']}% CPU"

    elif ram > 90 and len(top_process) > 0:
        title = " RAM Spike"
        message = f"{p['name']} (PID {p['pid']}) using {p['memory_percent']:.2f}% RAM"

    elif net > 5:
        title = " Network Spike"
        message = f"High network usage: {net:.2f}"

    # 🔔 Universal notification
    notification.send_notification(title, message)

    print(f"🚨 ALERT | {message} | Score: {score:.3f}")