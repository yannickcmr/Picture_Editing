from calc_unit import main as calc_main
import matplotlib.pyplot as plt
import numpy as np
import time
import codecs, sys, io, os

try:
    sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
except:
    pass  

Path_Saving = "Test_Mandelbrot"

def main():
    Mandelbrot = calc_main()

    def Save(image: Mandelbrot, decimals_: int = 6) -> None:
        path = os.path.join("Test_Mandelbrot", f"{image.ref_name}.csv")
        array_pres = np.absolute(image.array[0]).real

        with io.open(path, "w+", encoding="utf-8") as test_file:
            for line in array_pres:
                for value in line:
                    if value.real != 0: test_file.write(f"{np.around(value, decimals = decimals_)};")
                test_file.write("\n")

    def Present(image: Mandelbrot, save_: bool = False, show_center: bool = False):
        array_pres = np.absolute(image.array[0]).real
        if show_center: array_pres[int(len(array_pres)/2)][int(len(array_pres[0])/2)] = 3

        plt.imshow(array_pres)
        plt.pcolormesh(array_pres, cmap="gnuplot2")
        plt.title(f"Info:{image.ref_name}\nCenter: {image.val_center}\nRadius: {image.val_rad}")
        plt.show()

        if save_:  plt.savefig(f"{image.ref_name}.png", bbox_inches='tight')

    def Run_Mandelbrot(class_info: list, func_info: list, save_info: list, present_info: list):
        # Creating Mandelbrot Object.
        print("\ncreating the Mandelbrot class")
        Image = Mandelbrot(class_info[0], class_info[1], class_info[2], class_info[3])
        Image.Create_Array()

        print("\nstart of calculation")
        Image.Mandelbrotify(func_info[0], func_info[1], func_info[2], func_info[3])
        
        if present_info[0]:Present(Image, present_info[1], present_info[2])
        if save_info[0]: Save(Image, save_info[1])

    return Run_Mandelbrot


if __name__ == "__main__":
    'Set Values for the Mandelbrot Class'
    name = "test_while"
    center = -0.473378 + 0j
    radius = 0.9
    resolution = "1000x1000"
    'Set Values for the Mandelbrotify Function'
    max_iter = 50
    bound = 1.5
    max_rep = 50
    coef = 0.5
    "Savings Options"
    save = False
    save_decimals = 6
    "Present Options"
    present = True
    save_img = False
    show_center = False

    start_time = time.perf_counter()
    Run_Mandelbrot = main()
    Run_Mandelbrot(class_info=[name, center, radius, resolution], 
                                func_info=[max_iter, bound, max_rep, coef], 
                                present_info=[present, save_img, show_center],
                                save_info=[save, save_decimals])
    end_time = time.perf_counter()
    print(f"-> Total time: {end_time - start_time} sec")