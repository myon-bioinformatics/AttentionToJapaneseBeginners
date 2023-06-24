'''Dear English speaker
!!!!!Attention in advance: this program is a failed case!!!!!
SyntaxError: Non-UTF-8 code starting with...←this is encoded to "Shift JIS” intentionally.
Python 3 uses "UTF-8" as default encoding. you should execute main.py instead of this
'''

'''日本語話者に向けて
!!!!!予め: このプログラムは失敗事例です!!!!!
SyntaxError: Non-UTF-8 code starting with...←わざとこのファイルを"Shift JIS"にエンコードしています。
Python3はデフォルトのエンコーディングとして「UTF-8」を使います。これではなくmain.pyを素直に実行してください。。
'''

import inspect

#Standard Output: harmless Shift_JIS char
def standard_output_harmless_shift_jis():
    easy_separator = easy_separator_closure()()
    for char in ["繧?","縺?","險?","縲?","閭ｽ.","a","1"]: #harmless
        print(char,char.encode("shift_jis"))
    easy_separator
    return

#Standard Output: HARMFUL Shift_JIS char!!
def standard_output_harmful_shift_jis():
    easy_separator = easy_separator_closure()()
    for char in ["陦ｨ","閭ｽ","蜊?","豕?","蜈?","蝙?","譁ｽ","蛟?","譛ｬ","蝗ｳ"]: #HARMFUL!!!!
        print(char,char.encode("shift_jis"))
    easy_separator
    return

#print("No problem!!") with harmless Shift_JIS char
def print_harmless_shift_jis():
    easy_separator = easy_separator_closure()() #繧ｯ繝ｭ繝ｼ繧ｸ繝｣繧剃ｽｿ逕ｨ縺励◆
    print("No problem!!")
    easy_separator
    return

#print("No problem!!") may not function with HARMFUL Shift_JIS char!!
def print_harmful_shift_jis():
    easy_separator = easy_separator_closure()() #縺薙ｌ縺ｯ繧ｯ繝ｭ繝ｼ繧ｸ繝｣縺ｨ縺?縺?讖溯?ｽ
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




