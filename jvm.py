import psutil

def format_jvm_args(max_heap_gb: int) -> str:
    """
    Format the JVM arguments string for Minecraft Java launch.
    """
    args = [
        f"-Xmx{max_heap_gb}G",
        "-XX:+UnlockExperimentalVMOptions",
        "-XX:+UseG1GC",
        "-XX:G1NewSizePercent=20",
        "-XX:G1ReservePercent=20",
        "-XX:MaxGCPauseMillis=50",
        "-XX:G1HeapRegionSize=32M"
    ]
    return " ".join(args)

def get_suggested_max_heap() -> int:
    """
    Suggest max heap size based on system RAM.
    Use 50% to 75% of available RAM, capped between 1 and 12 GB.
    """
    total_ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    suggested = int(max(1, min(total_ram_gb * 0.75, 12)))
    return suggested

def main():
    print("Minecraft JVM Args Generator\n")

    suggested_heap = get_suggested_max_heap()
    print(f"Detected system RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")
    print(f"Suggested max heap size (-Xmx): {suggested_heap}G\n")

    user_input = input(f"Enter max heap size in GB or press Enter to use {suggested_heap}G: ").strip()
    if user_input:
        try:
            heap_size = int(user_input)
            if heap_size < 1 or heap_size > 16:
                print("Warning: Recommended heap size between 1 and 16 GB. Using suggested value instead.")
                heap_size = suggested_heap
        except ValueError:
            print("Invalid input, using suggested heap size.")
            heap_size = suggested_heap
    else:
        heap_size = suggested_heap

    jvm_args = format_jvm_args(heap_size)
    print("\nGenerated JVM arguments:")
    print(jvm_args)

if __name__ == "__main__":
    main()
