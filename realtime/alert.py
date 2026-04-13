def alert(score, data):
    reasons = []
    if data["cpu_percent"] > 80:
        reasons.append(f"CPU spike: {data['cpu_percent']:.1f}%")
    if data["ram_percent"] > 90:
        reasons.append(f"RAM spike: {data['ram_percent']:.1f}%")
    if data["net_bytes_per_sec"] > 5:
        reasons.append(f"NET spike: {data['net_bytes_per_sec']:.2f} MB/s")
    
    reason_str = ", ".join(reasons) if reasons else "unusual pattern detected"
    print(f"⚠️  ANOMALY DETECTED | Score: {score:.3f} | Reason: {reason_str}")