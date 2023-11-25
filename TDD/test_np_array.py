import numpy as np

# 크기가 다른 두 배열 생성
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6, 7,8])

# 크기가 다른 배열 더하기
result = array1 + array2[:len(array1)]  # 예시로 두 배열의 길이를 맞춰 더하기

print("Array 1:", array1)
print("Array 2:", array2)
print(array2[len(array1):] )
print(np.append(result,array2[len(array1):] ))
print("Result:", result)
