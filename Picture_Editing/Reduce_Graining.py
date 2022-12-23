import os, time
from skimage import io
import numpy as np
import random as rd
import matplotlib.pyplot as plt

Path_Images = "Tests/Test_Picture_Edit/"

def Add_Path(file) -> str:
    return os.path.join(Path_Images, file)

image1 = io.imread(Add_Path("B1.png"), as_gray = True)
image2 = io.imread(Add_Path("B2.png"), as_gray = True)
image3 = io.imread(Add_Path("B3.png"), as_gray = True)

""" Image Extention """

def Extent_Image(array: np.ndarray, size: tuple, insert_index: tuple, option: str = "zero") -> np.ndarray:
    if option == "zero":
        print("zero")
        return Zero_Extention_Array(array, size, insert_index)
    elif option == "mirror":
        print("mirror")
        return Mirroring_Array(array, size, insert_index)
    else:
        print("None")
        raise Exception("Option is not vaild")

def Mirroring_Array(array: np.ndarray, size: tuple, insertion_point: tuple) -> np.ndarray:
    if insertion_point[0] != 0:
        if insertion_point[0] == -1:
            cache = np.flip(array[0: size[0] - array.shape[0]], axis=0)
            array = np.vstack([cache, array])
        else:
            cache = np.flip(array[2* array.shape[0] - size[0]: array.shape[0]], axis=0)
            array = np.vstack([array, cache])

    if insertion_point[1] != 0:
        cache = array.transpose()
        if insertion_point[1] == -1:
            cache = np.flip(cache[0: size[1] - cache.shape[0]], axis=0).transpose()
            array = np.hstack([cache, array])
        else:
            cache = np.flip(cache[2* cache.shape[0] - size[1]: cache.shape[0]], axis=0).transpose()
            array = np.hstack([array, cache])
    return array

# inserttion_point: (v,h), where v is vertical and h is horizontal.
def Zero_Extention_Array(array: np.ndarray, size: tuple, insertion_point: tuple) -> np.ndarray:
    if insertion_point[0] != 0:
        if insertion_point[0] == -1:
            array = np.vstack([np.zeros((size[0] - array.shape[0], array.shape[1])), array])
        else:
            array = np.vstack([array, np.zeros((size[0] - array.shape[0], array.shape[1]))])

    if insertion_point[1] != 0:
        if insertion_point[1] == -1:
            array = np.hstack([np.zeros((array.shape[0], size[1] - array.shape[1])), array])
        else:
            array = np.hstack([array, np.zeros((array.shape[0], size[1] - array.shape[1]))])
    
    return array

""" Mean Value Filter """

def Identical_Weights(size: tuple) -> np.ndarray:
    return np.ones((size[0], size[1]))*np.around((1/(size[0] * size[1])), decimals=7)

def Cut_Area_Array(array: np.ndarray, pos: tuple, area: int ) -> np.ndarray:
    x_min, x_max = np.max([pos[0] - area, 0]), np.min([pos[0] + area, array.shape[0]])
    y_min, y_max = np.max([pos[1] - area, 0]), np.min([pos[1] + area, array.shape[1]])
    
    return array[x_min:x_max, y_min: y_max]

def Mean_Value_Array(array: np.ndarray, weights: np.ndarray = None) -> float:
    if weights == None:
        array_shape = array.shape
        weights = Identical_Weights(array_shape)
    
    array = array * weights
    return np.mean(array) 


# s is the neighbourhood area, options = [zero, mirror]
def Mean_Value_Filter(image: np.ndarray, s: int, options: str = "zero") -> np.ndarray:
    weights_tuple = (2*s+1, 2*s+1)
    
    arrray_return = np.zeros(image.shape)
    
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):

            if (i <= s) and (j <= s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (-1, -1), options))
            elif (i <= s) and (image.shape[1] - j <= s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (-1, 1), options))
            elif (image.shape[0] - i <= s) and (j <=s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (1, -1), options))
            elif (image.shape[0] - i <= s) and (image.shape[1] - j <= s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (1, 1), options))
            elif (i <= s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (-1, 0), options))
            elif (j <= s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (0, -1), options))
            elif (image.shape[0] - i <= s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (1, 0), options))
            elif (image.shape[1] - j <= s):
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (0, 1), options))
            else:
                arrray_return[i][j] = Mean_Value_Array(Extent_Image(Cut_Area_Array(image, (i,j), s), weights_tuple, (0, 0), options))
    
    return arrray_return
    


""" Median Value Filter """

def Median_Value_Array(array: np.ndarray) -> float:
    pass

def Median_Value_Filter(image: np.ndarray) -> np.ndarray:
    pass

""" Tests """

if __name__ == "__main__":
    start = time.perf_counter()
    test_array1 = np.ones((5, 10))
    test_array2 = np.ones((8,7))
    test_array3 = np.arange(54).reshape((6,9))

    #print(f"{type(image1)} \n{image1}")
    #print(Identical_Weights(100,100))
    #print(Mean_Value_Array(test_array1))
    #print(Extent_Image(test_array1, (10, 10), (-1, 0)))
    #print(Extent_Image(test_array2, (10, 10), (-1, 1)))
    #print(test_array3)
    #print(Extent_Image(test_array3, (10, 10), (0,1), "mirror"))


    io.imsave(Add_Path("test_b1.png") ,Mean_Value_Filter(image1, 3, options = "mirror"))
    print(f"Done in {time.perf_counter() - start} sec.\n")
    
