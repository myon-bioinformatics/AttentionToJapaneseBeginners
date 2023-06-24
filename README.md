# 😎Summary
**🚴‍♂️(ENG)Acknowledge HARMFUL Shift_JIS, and please pay attention not to let it use as far as possible!!**

**🚴‍♀️(JSP)コメントアウトや標準出力でさえ、プログラム内にはできるだけ日本語は含まないようにしよう...**

# 🫶Notice
1. If a program includes non-alphabet character, a problem is occured by it.
1. At this time, Shift_JIS is encoded or decoded as example.
1. By the way this program(main.py) is a succeed case, a problem isn't basically occured by it


# 📝The Result of Standard Output📝
the following is the result to execute main.py

```
----------------
Called function: standard_output_harmless_shift_jis
る b'\x82\xe9'
た b'\x82\xbd'
記 b'\x8bL'
〆 b'\x81Y'
能. b'\x94\\.'
a b'a'
1 b'1'
----------------
Called function: standard_output_harmful_shift_jis
予 b'\x97\\'
能 b'\x94\\'
十 b'\x8f\\'
法 b'\x96@'
充 b'\x8f['
型 b'\x8c^'
施 b'\x8e{'
倍 b'\x94{'
本 b'\x96{'
図 b'\x90}'
----------------
Called function: print_harmless_shift_jis
No problem!!
----------------
Called function: print_harmful_shift_jis
No problem!!
```
