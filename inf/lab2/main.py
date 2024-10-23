import re

def main():
    while True:
        input_str = input("enter a message consisting of 7 digits 0 or 1, written without spaces:")
        if len(input_str) == 7 and re.fullmatch(r'[01]*', input_str):
            int_arr = [int(char) for char in input_str]
            break
        else:
            print("you must enter 7 bits containing only 0 and 1!")

    s1 = (int_arr[0] + int_arr[2] + int_arr[4] + int_arr[6]) % 2
    s2 = (int_arr[1] + int_arr[2] + int_arr[5] + int_arr[6]) % 2
    s3 = (int_arr[3] + int_arr[4] + int_arr[5] + int_arr[6]) % 2

    err_pos = s1 + s2 * 2 + s3 * 4

    bit_type = {
        0: "correct",
        1: "r1",
        2: "r2",
        3: "i1",
        4: "r3",
        5: "i2",
        6: "i3",
        7: "i4"
    }.get(err_pos, "unknown")

    print(bit_type)

    with open("result.txt", "w") as file:
        file.write(bit_type)

if __name__ == "__main__":
    main()