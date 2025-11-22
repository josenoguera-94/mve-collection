import threading
import time
import os
import random
from mutex import RedisMutex, LockAcquisitionError


def write_to_file(thread_id: int, filename: str = "shared_file.txt"):
    """Write to a shared file using mutex to prevent race conditions."""
    print(f"[Thread {thread_id}] Acquiring lock...")
    
    # Each thread creates its own mutex connection
    mutex = RedisMutex()
    try:
        # Use context manager for automatic lock/unlock
        with mutex.acquire("file_write_lock", wait_sec=15.0, retry_sec=0.5):
            print(f"[Thread {thread_id}] ✓ Lock acquired")
            
            # Count current lines
            try:
                with open(filename, 'r') as f:
                    line_count = len([l for l in f if l.strip()])
            except FileNotFoundError:
                line_count = 0
            
            time.sleep(random.uniform(0.1, 0.5))  # Simulate variable processing time
            
            # Write to file
            with open(filename, 'a') as f:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] Thread {thread_id} wrote line {line_count + 1}\n")
            
            print(f"[Thread {thread_id}] ✓ Done")
            # Lock is automatically released when exiting the context
            
    except LockAcquisitionError as e:
        print(f"[Thread {thread_id}] ✗ {e}")
    finally:
        mutex.close()


def main():
    print("\n=== Redis Mutex Example (using acquire context manager) ===")
    print("Multiple threads writing to the same file with mutex protection.\n")
    
    try:
        filename = "shared_file.txt"
        if os.path.exists(filename):
            os.remove(filename)
        
        # Launch multiple threads
        threads = []
        num_threads = 5
        
        for i in range(num_threads):
            thread = threading.Thread(target=write_to_file, args=(i + 1, filename))
            threads.append(thread)
            thread.start()  # Start all threads immediately to compete for the lock
        
        for thread in threads:
            thread.join()
        
        # Show results
        print(f"\n=== Results ===")
        print(f"Contents of {filename}:")
        print("-" * 60)
        with open(filename, 'r') as f:
            print(f.read(), end='')
        print("-" * 60)
        print("\n✓ All writes completed sequentially without race conditions\n")
        
    except Exception as e:
        print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
