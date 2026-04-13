import notification
def alert(score, data, top_cpu, top_ram):

    cpu = data["cpu_percent"]
    ram = data["ram_percent"]
    net = data["net_bytes_per_sec"]

    title = " System Alert"
    message = "Unusual system behavior detected"

    if cpu > 80 and len(top_cpu) > 0:
        p = top_cpu[0]
        title = " CPU Spike"
        message = f"{p['name']} (PID {p['pid']}) using {p['cpu_percent']}% CPU"

    elif ram > 90 and len(top_ram) > 0:
        p = top_ram[0]
        title = " RAM Spike"
        message = f"{p['name']} (PID {p['pid']}) using {p['memory_percent']:.2f}% RAM"

    elif net > 5:
        title = " Network Spike"
        message = f"High network usage: {net:.2f}"

    # 🔔 Universal notification
    notification.send_notification(title, message)

    print(f"🚨 ALERT | {message} | Score: {score:.3f}")