#Attention in advance: this program is a success case
import inspect

#Standard Output: harmless Shift_JIS char
def standard_output_harmless_shift_jis():
    easy_separator = easy_separator_closure()()
    for char in ["る","た","記","〆","能.","a","1"]: #harmless
        print(char,char.encode("shift_jis"))
    easy_separator
    return

#Standard Output: HARMFUL Shift_JIS char!!
def standard_output_harmful_shift_jis():
    easy_separator = easy_separator_closure()()
    for char in ["表","能","十","法","充","型","施","倍","本","図"]: #HARMFUL!!!!
        print(char,char.encode("shift_jis"))
    easy_separator
    return

#print("No problem!!") with harmless Shift_JIS char
def print_harmless_shift_jis():
    easy_separator = easy_separator_closure()() #クロージャを使用した
    print("No problem!!")
    easy_separator
    return

#print("No problem!!") may not function with HARMFUL Shift_JIS char!!
def print_harmful_shift_jis():
    easy_separator = easy_separator_closure()() #これはクロージャという機能
    print("No problem!!")
    easy_separator
    return

#Closure: easy_separator with showing current called function
def easy_separator_closure():
    def print_function_name():
        print("----------------")
        frame = inspect.currentframe().f_back
        function_name = frame.f_code.co_name
        print(f"Called function: {function_name}")
    return print_function_name

if __name__ == "__main__":
    #confirm shift_jis char
    standard_output_harmless_shift_jis()
    standard_output_harmful_shift_jis()

    #print("No problem!!") with Shift_JIS char comments
    print_harmless_shift_jis()
    print_harmful_shift_jis()




