# --- Stack-Dynamic Simulation ---
def session_counter():
    # reset to 0 every function call
    counter = 0 
    counter += 1
    print(f"Session visits: {counter}")


# --- Static Local Simulation ---
def kiosk_usage():
    if not hasattr(kiosk_usage, "total_users"): # "hey, does this exist? if not, do this" | "create this attribute in this funct"
        kiosk_usage.total_users = 0
    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")

# --- Execution ---
if __name__ == "__main__": # "are we in the main execution part, or did someone import this file to borrow a function?"
    # "we're in the main execution? ok good proceed."
    # step 4 bullet 3 requirement
    print("--- Testing Stack-Dynamic (Session Counter) 5 Times ---")
    for _ in range(5):
        session_counter()
        
    print("\n--- Simulating 3 Main Customer Sessions ---")
    # Step 2 & 3 Requirement: Simulate 3 distinct customer sessions calling both functions
    for i in range(1, 4):
        print(f"\n[Customer {i} arrives]")
        session_counter()  # Will always output 1
        kiosk_usage()      # Will increment consecutively (1, then 2, then 3)