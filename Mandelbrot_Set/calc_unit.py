from dataclasses import dataclass
import numpy as np
import time
import codecs, sys, os, io
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))


try:
    sys.stdin = codecs.getreader("utf-8")(sys.stdin.detach())
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
except:
    pass  

Path_Saving = "Test_Mandelbrot"

def main():

    def Mandelbrot_Function(line: np.ndarray, range_: int, max_bound: float, max_repetition: int, coef: float = 0.7) -> np.ndarray:
        start_calc = time.perf_counter()
        base =  line[1].copy()
        vec = line[0].copy()

        vec, base = vec.flatten(), base.flatten()
        #base = tf.constant(base)
        vec_return = np.zeros(vec.shape, dtype="complex64")
        pos = np.arange(0, len(vec))

        stops = 0
        print(f"end of conversion: {time.perf_counter() - start_calc}")
        while (stops <  range_):
            rep = 0
            while (np.absolute(np.mean(vec)) < max_bound):
                #vec = tf.math.square(vec)
                #vec = tf.math.add(vec, base)
                vec = np.multiply(vec, vec)
                vec = np.add(vec, base)
                rep += 1
                if rep > max_repetition: break
            
            print(f"end of {stops}. while-loop: {time.perf_counter() - start_calc}")
            vec = np.nan_to_num(vec, nan =0)
            active =  np.where(np.absolute(vec) < max_bound)
            vec = vec[active]
            pos = pos[active]
            base = base[active]
            
            if len(vec) == 0: return vec_return
            if (rep > coef * max_repetition): stops += 1
        
        print(len(pos), len(base), len(vec))
        for x in range(0, len(pos)):  vec_return[pos[x]] = vec[x]
        print(f"end of calculation: {time.perf_counter() - start_calc}")
        return vec_return


    @dataclass
    class Mandelbrot:
        ref_name: str
        val_center: float
        val_rad: float
        resolution: str = "10x10"
        array: list = np.zeros((1,1))

        def Create_Array(self) -> np.array:
            res = self.resolution.split("x")
            pos_top, pos_bot = self.val_center + float(self.val_rad)*1j, self.val_center - float(self.val_rad)*1j
            top_array = np.linspace(pos_top - self.val_rad, pos_top + self.val_rad, int(res[0]))
            bot_array = np.linspace(pos_bot - self.val_rad, pos_bot + self.val_rad, int(res[0]))

            array_calc = np.linspace(start = top_array, stop = bot_array, num= int(res[0]))
            array_pres = np.zeros((int(res[0]), int(res[1])))

            array_cmp = np.array([array_pres, array_calc])
            self.array = array_cmp
            return array_cmp

        def Mandelbrotify(self, range_: int, max_: int, rep_: int, coef_: float = 0.5):
            shape = self.array[0].shape
            array_cache = Mandelbrot_Function(self.array, range_, max_, rep_, coef_)
            array_cache = array_cache.reshape(shape)
            
            self.array = np.array([array_cache, self.array[1]])


    return Mandelbrot

def Save(array: np.ndarray) -> None:
    path = os.path.join("Test_Mandelbrot", "test_array.txt")
    with io.open(path, "w+", encoding="utf-8") as test_file:
        for line in array:
            test_file.write(f"{line}\n")


if __name__ == "__main__1":
    start_time = time.perf_counter()
    Mandelbrot = main()

    # Creating a test case
    test = Mandelbrot("test", 0+ 1j, 0.3)
    test.Create_Array()
    test.Mandelbrotify()

    end_time = time.perf_counter()
    #print(f"-> Total time: {end_time - start_time}")