import os
import psutil
import platform

def suggest_jvm_args():
    total_ram_gb = round(psutil.virtual_memory().total / (1024 ** 3))
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    arch = platform.architecture()[0]

    # Calculate suggested JVM heap size
    max_heap = f"-Xmx{int(total_ram_gb * 0.5)}G"
    min_heap = f"-Xms{int(total_ram_gb * 0.5)}G"

    # G1GC Tuning
    g1_args = [
        "-XX:+UnlockExperimentalVMOptions",
        "-XX:+UseG1GC",
        "-XX:G1NewSizePercent=20",
        "-XX:G1ReservePercent=20",
        "-XX:MaxGCPauseMillis=50",
        "-XX:G1HeapRegionSize=16M" if total_ram_gb <= 8 else "-XX:G1HeapRegionSize=32M"
    ]

    # JVM options for 64-bit systems
    if "64" in arch:
        g1_args.append("-d64")

    print("Suggested JVM Arguments based on your system:")
    print("--------------------------------------------------")
    print(min_heap, max_heap, *g1_args)
    print(f"\n[System Specs Detected]")
    print(f"RAM: {total_ram_gb} GB")
    print(f"CPU Cores: {cpu_cores}")
    print(f"CPU Threads: {cpu_threads}")
    print(f"Arch: {arch}")

if __name__ == "__main__":
    suggest_jvm_args()
