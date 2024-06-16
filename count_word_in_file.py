
def count_word(file_path):
    counter = {}
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                word = word.strip()  # Loại bỏ khoảng trắng không mong muốn
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
    return counter

file_path = "C:/Users/bathi/OneDrive/Desktop/AIO_Exercises/AIO_Exercises/P1_data.txt"
result = count_word ( file_path )
assert result ['who'] == 3
print (result ['man'])

