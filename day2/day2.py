import re
import sys

def main():

    

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    try:
        with open(sys.argv[1]) as file:
           file_data = file.read()
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")

    total = 0
    for range in file_data.split(","):
        total += total_for_line(range)

    print(total)

def total_for_line(line):
    
    nums = line.split("-")
    start = int(nums[0])
    end = int(nums[1])

    total = 0
    for id in range(start, end + 1):
        if is_invalid_id(id):
            print("invalid id: " + str(id))
            total += id

    return total

def is_invalid_id(id):

    id_length = len(str(id))
    if id_length <= 1:
        return False
    
    if id_length % 2 != 0:
        return False
    
    for i in range((id_length // 2), (id_length // 2) + 1):
        # chunk needs to cleanly divide total length
        if id_length % i != 0:
            continue

        chunk = pow(10, i)      

        valid = False
        remaining_id = id
        while remaining_id != 0:
            chunk_val = remaining_id % chunk

            if remaining_id == id:
                expected_chunk_val = chunk_val
            else:
                if chunk_val != expected_chunk_val:
                    valid = True
                    break
            
            remaining_id = remaining_id // chunk

        if not valid:
            return True
        
    return False



if __name__ == "__main__":
    main()