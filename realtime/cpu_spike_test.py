import multiprocessing

def stress_cpu():
    while True:
        pass

if __name__ == "__main__":
    processes = []
    
    for _ in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=stress_cpu)
        p.start()
        processes.append(p)
    
    input("Press ENTER to stop...\n")
    
    for p in processes:
        p.terminate()