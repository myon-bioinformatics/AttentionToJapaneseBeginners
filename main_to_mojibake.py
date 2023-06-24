'''Dear English speaker
!!!!!Attention in advance: this program is a failed case!!!!!
SyntaxError: Non-UTF-8 code starting with...��this is encoded to "Shift JIS�h intentionally.
Python 3 uses "UTF-8" as default encoding. you should execute main.py instead of this
'''

'''���{��b�҂Ɍ�����
!!!!!�\��: ���̃v���O�����͎��s����ł�!!!!!
SyntaxError: Non-UTF-8 code starting with...���킴�Ƃ��̃t�@�C����"Shift JIS"�ɃG���R�[�h���Ă��܂��B
Python3�̓f�t�H���g�̃G���R�[�f�B���O�Ƃ��āuUTF-8�v���g���܂��B����ł͂Ȃ�main.py��f���Ɏ��s���Ă��������B�B
'''

import inspect

#Standard Output: harmless Shift_JIS char
def standard_output_harmless_shift_jis():
    easy_separator = easy_separator_closure()()
    for char in ["�?","�?","�?","�?","能.","a","1"]: #harmless
        print(char,char.encode("shift_jis"),sep=": ")
    easy_separator
    return

#Standard Output: HARMFUL Shift_JIS char!!
def standard_output_harmful_shift_jis():
    easy_separator = easy_separator_closure()()
    for char in ["表","能","�?","�?","�?","�?","施","�?","本","図"]: #HARMFUL!!!!
        print(char,char.encode("shift_jis"),sep=": ")
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
    easy_separator = easy_separator_closure()() #これはクロージャと�?�?機�?�
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

    #print("No problem!!") with Shift_JIS char
    print_harmless_shift_jis()
    print_harmful_shift_jis()




