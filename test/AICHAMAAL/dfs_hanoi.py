def tower_of_hanoi(n,source,target,auxillary):
    if n==1:
        print(f"Move Disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1,source,auxillary,target)
    print(f"Move Disk {n} from {source} to {target}")
    tower_of_hanoi(n-1,auxillary,target,source)

while True:
    try:
        num_disks = int(input("Enter the number of disks (positive integer): "))
        if num_disks > 0:
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
tower_of_hanoi(num_disks,'A','C','B')
