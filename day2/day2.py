import re
import sys

def main():

    invalid_ids = [11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859]
    valid_ids = [12345, 111112, 890890891, 12222122222]

    for id in invalid_ids:
        if not is_invalid_id(id):
            print(str(id) + " is not invalid!")

    for id in valid_ids:
        if is_invalid_id(id):
            print(str(id) + " is invalid!")


    return 

    if len(sys.argv) != 2:
        sys.exit(f"Usage: {sys.argv[0]} <file name>")

    try:
        with open(sys.argv[1]) as file:
           print("opened file!")
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]}: Unable to open file")



def is_invalid_id(id):

    id_length = len(str(id))
    if id_length <= 1:
        return False
    
    for i in range(1, (id_length // 2) + 1):
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