# 😎Summary😎
## **🚴‍♂️(ENG)**

**🦆About Shift_JIS char as example, and please pay attention not to let non-alphanumeric-character use as far as possible🦆**

## **🚴‍♀️(JSP)**

**🦜コメントアウトや標準出力の利用であっても、プログラム内ではできるだけ英数字以外の文字を使わないようにしましょう🦜**


> __Note__ Now Preparing

# 🫶Notice🫶
```python
python main.py
```

**🚴‍♂️(ENG)**
1. If a program includes non-alphanumeric-character, a problem may be occured by it.
1. At this time, Shift_JIS is encoded or decoded as example.
1. By the way this program(_main.py_) is a succeed case, a problem isn't basically occured.

**🚴‍♀️(JSP)**
1. アルファベットじゃない文字を使うとそれが原因で問題が起こることがあります。
1. 今回は、Shift_JISがエンコードもしくはデコードされた時を例にします。
1. ちなみにこのプログラム(_main.py_)は成功例のため、問題は基本的に起こりません。

# 😖Cause & 😆Countermeasures
## 😖Cause
**🚴‍♂️(ENG)**

> 🤖The followings are the causes🤖☞
- Even though it appears as a single character, issues can arise due to the actual character consisting of two or more bytes. 

- About Shift_JIS (SJIS, cp932) character encoding, representative characters include those with a second byte of 0x5c, such as "\\". 

- Broadly, it can include characters with a second byte of 0x7c( "|" ), or characters overlapping with metacharacters used in regular expressions.

**🚴‍♀️(JSP)**

> 🤖以下がその原因です🤖☞

- 見かけ上は1つの文字であっても、実際には2バイト以上であることが原因で問題が起こることがあります。

- Shift_JIS（SJIS、cp932）の文字コードでは、2バイト目が0x5cの「\」（バックスラッシュ）を含む文字が代表的です。

- 広義の意味では、2バイト目が0x7cの「|」（パイプ文字）や、2バイト目が正規表現などのメタ文字と重なる文字も含みます。

### 🍮at length🍮
**🚴‍♂️(ENG)**

- The second byte of the character "能" is " \\".

- This is equivalent to writing "\" at the end of a line, indicating the end of the line.

- In the C programming language, this would result in the code being commented out until the next line.

**🚴‍♀️(JSP)**

- 例えば、「能」という文字の2バイト目は「\」です。

- それは行末に「\\」と書かれていることと同義になります。

- C言語では、これによって次の行までがコメントアウトされてしまいます。

### Example include those with a second byte of "\\"(0x5c)
```
表: b'\x95\\'
能: b'\x94\\'
十: b'\x8f\\'
```

## 😆Countermeasures
**🚴‍♂️(ENG)**

> 🥷The solutions are surprisingly simple🥷

Add a period (".") at the end of commented-out statements: **"Simple"**

Use character encoding/decoding with a character set such as "UTF-8": **"Common"**

**Avoid using non-alphanumeric characters as far as possible**: **"Important"**

**🚴‍♀️(JSP)**

> 🥷解決策は意外と単純🥷
- コメントアウトの文末に"."(ピリオド)などをつける: **「簡単」**
- エンコード/デコード時の文字コードを「UTF-8」などにする: **「通常」**
- **そもそも英数字以外はできるだけ使わない**: **「重要」**

# 📝The Result of Standard Output📝
**🚴‍♂️(ENG)** ☕️The following is the result to execute main.py as a succeed case☕️

**🚴‍♀️(JSP)** ☕️以下の例はmain.pyを実行した時の成功例の結果です☕️

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
表 b'\x95\\'
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
> __Warning__ If a problem were occured, ` "print("No problem!!") at Called function: print_harmful_shift_jis" ` wouldn't function.

# Addendum
**🚴‍♂️(ENG)**

⚠️The file "main_to_shift_jis.py" is a version of "main.py" encoded in Shift_JIS instead of UTF-8.

**🚴‍♀️(JSP)**

⚠️「main_to_shift_jis.py」は、「main.py」をUTF-8ではなくShift_JISでエンコードしたファイルです。


### 🧁Mojibake in detail🧁
>- 🤥main.py🤥
>>    easy_separator = easy_separator_closure()() #これはクロージャという機能
>
>- 😵‍💫main_to_mojibake.py(Even the Japanese speaker can't read)😵‍💫
>>    easy_separator = easy_separator_closure()() #繧ｯ繝ｭ繝ｼ繧ｸ繝｣繧剃ｽｿ逕ｨ縺励◆


# 🚴‍♂️Dear non-Japanese speaker
About "繧ｯ繝ｭ繝ｼ繧ｸ繝｣繧剃ｽｿ逕ｨ縺励◆" 👈even the Japanese speaker doesn't often use.

But, they often use the char like ["表","能","十","法","充","型","施","倍","本","図"]

> **表**(b'\x95\\') is noun and means 💹 📊 📈("chart", "table", "list" and so on).
> 
> For example: "matrix chart" equals "マトリックス表"(マトリックス=matrix)
>
> **能**(b'\x94\\') is noun, and **能力** means "ability", "talent" ,and "skill".
> >btw, "力" is noun and means "power"💪.
> 
> **十**(b'\x8f\\') is noun and means "Ten(=10)"
> 
> >🔟🔟(Twenty) expresses 20, or 二十(二=two)
> 
> About Jujutsu Kaisen, a part of characters such as Megumi Fushiguro use "Ten Shadows Technique"(十種影法術 Tokusa no Kage Bōjutsu)
>


## References
- [Variable-width_encoding](https://en.wikipedia.org/wiki/Variable-width_encoding)
- [Mojibake](https://en.wikipedia.org/wiki/Mojibake)

# 🚴‍♀️日本語話者に向けて

## 参考 
- [Shift_JISのダメ文字](https://sites.google.com/site/fudist/Home/grep/sjis-damemoji-jp?authuser=0)
- [マルチバイト文字](https://ja.wikipedia.org/wiki/%E6%96%87%E5%AD%97%E5%8C%96%E3%81%91)
- [文字化け](https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%AB%E3%83%81%E3%83%90%E3%82%A4%E3%83%88%E6%96%87%E5%AD%97)



