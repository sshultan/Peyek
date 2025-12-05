# Soal Latihan Python - Dari Mudah ke Advanced

## Panduan Penggunaan

- Kerjakan soal secara berurutan untuk hasil terbaik
- Jangan terburu-buru ke level advanced sebelum menguasai level sebelumnya
- Coba selesaikan sendiri dulu sebelum melihat hints
- Tulis kode yang clean dan readable
- Test dengan berbagai test case

---

## Level 1: Beginner (Fondasi)

### 1.1 FizzBuzz Classic

**Deskripsi:**
Buatlah program yang mencetak angka dari 1 hingga n. Tetapi:

- Untuk kelipatan 3, cetak "Fizz"
- Untuk kelipatan 5, cetak "Buzz"
- Untuk kelipatan 3 dan 5, cetak "FizzBuzz"

**Input:** `n = 15`

**Output:**

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

**Hints:**

- Gunakan operator modulo `%`
- Cek kondisi kelipatan 15 terlebih dahulu

---

### 1.2 Palindrome Checker

**Deskripsi:**
Buatlah fungsi yang mengecek apakah sebuah string adalah palindrome (dibaca sama dari depan dan belakang). Abaikan spasi dan kapitalisasi.

**Input:**

```python
check_palindrome("A man a plan a canal Panama")
check_palindrome("race a car")
```

**Output:**

```
True
False
```

**Hints:**

- Gunakan `.lower()` dan `.replace()` untuk normalisasi
- Bandingkan string dengan reversed version-nya

---

### 1.3 Count Vowels and Consonants

**Deskripsi:**
Buatlah fungsi yang menghitung jumlah huruf vokal dan konsonan dalam sebuah string. Abaikan angka dan simbol.

**Input:** `"Hello World 123!"`

**Output:**

```python
{'vowels': 3, 'consonants': 7}
```

**Hints:**

- Buat set untuk vowels: `{'a', 'e', 'i', 'o', 'u'}`
- Gunakan `.isalpha()` untuk filter huruf saja

---

## Level 2: Intermediate (Data Structures & Algorithms)

### 2.1 Two Sum Problem

**Deskripsi:**
Diberikan sebuah list angka dan target, temukan dua angka yang jika dijumlahkan menghasilkan target. Return index dari kedua angka tersebut.

**Input:**

```python
nums = [2, 7, 11, 15]
target = 9
```

**Output:** `[0, 1]` (karena nums[0] + nums[1] = 2 + 7 = 9)

**Constraints:**

- Setiap input memiliki tepat satu solusi
- Tidak boleh menggunakan elemen yang sama dua kali

\*#Hints:\*\*

- Gunakan dictionary untuk menyimpan angka yang sudah dilihat
- Time complexity target: O(n)

---

### 2.2 Group Anagrams

**Deskripsi:**
Diberikan list of strings, kelompokkan semua anagram bersamaan. Anagram adalah kata dengan huruf yang sama tapi urutan berbeda.

**Input:**

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Output:**

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

**Hints:**

- Sorted version dari anagram akan sama: sorted("eat") == sorted("tea")
- Gunakan dictionary dengan sorted string sebagai key

---

### 2.3 Longest Substring Without Repeating Characters

**Deskripsi:**
Temukan panjang substring terpanjang tanpa karakter yang berulang.

**Input:** `"abcabcbb"`

**Output:** `3` (substring "abc")

**Input:** `"pwwkew"`

**Output:** `3` (substring "wke")

**Hints:**

- Gunakan sliding window technique
- Gunakan set atau dict untuk track karakter yang sudah ada

---

### 2.4 Valid Parentheses

**Deskripsi:**
Buatlah fungsi untuk mengecek apakah string yang berisi karakter `()`, `{}`, `[]` memiliki pasangan yang valid.

**Input:** `"({[]})"` → Output: `True`

**Input:** `"([)]"` → Output: `False`

**Hints:**

- Gunakan stack (list) untuk tracking
- Push opening brackets, pop saat ketemu closing brackets

---

## Level 3: Intermediate-Advanced (Algorithms & Problem Solving)

### 3.1 Merge Intervals

**Deskripsi:**
Diberikan collection of intervals, merge semua overlapping intervals.

**Input:** `[[1,3], [2,6], [8,10], [15,18]]`

**Output:** `[[1,6], [8,10], [15,18]]`

**Penjelasan:** Intervals [1,3] dan [2,6] overlap, maka di-merge menjadi [1,6]

**Hints:**

- Sort intervals berdasarkan start time
- Track current interval dan compare dengan next

---

### 3.2 Product of Array Except Self

**Deskripsi:**
Diberikan array `nums`, return array `output` dimana `output[i]` adalah product dari semua elemen nums kecuali `nums[i]`. **Tidak boleh menggunakan division.**

**Input:** `[1, 2, 3, 4]`

**Output:** `[24, 12, 8, 6]`

**Penjelasan:**

- output[0] = 2 _ 3 _ 4 = 24
- output[1] = 1 _ 3 _ 4 = 12
- dst.

**Hints:**

- Gunakan left product dan right product array
- Bisa dioptimasi menjadi O(1) space complexity

---

### 3.3 Longest Palindromic Substring

**Deskripsi:**
Temukan substring palindrome terpanjang dalam sebuah string.

**Input:** `"babad"`

**Output:** `"bab"` atau `"aba"` (keduanya valid)

**Input:** `"cbbd"`

**Output:** `"bb"`

**Hints:**

- Expand around center approach
- Pertimbangkan palindrome dengan panjang ganjil dan genap

---

### 3.4 Binary Tree Level Order Traversal

**Deskripsi:**
Diberikan binary tree, return level order traversal dari node values (dari kiri ke kanan, level demi level).

**Contoh Tree:**

```
    3
   / \
  9  20
    /  \
   15   7
```

**Output:** `[[3], [9, 20], [15, 7]]`

**Hints:**

- Gunakan BFS (Breadth-First Search) dengan queue
- Track level dengan menambahkan marker atau menggunakan nested loop

---

## Level 4: Advanced (Complex Problems)

### 4.1 LRU Cache Implementation

**Deskripsi:**
Implementasikan LRU (Least Recently Used) cache dengan operations:

- `get(key)`: Get value dari key jika ada, return -1 jika tidak ada
- `put(key, value)`: Set atau insert value. Jika cache penuh, hapus item yang paling lama tidak digunakan.

**Contoh:**

```python
cache = LRUCache(2)  # capacity = 2
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)       # returns 1
cache.put(3, 3)    # evicts key 2
cache.get(2)       # returns -1 (not found)
```

**Requirements:**

- `get` dan `put` harus O(1) time complexity

**Hints:**

- Gunakan kombinasi dictionary dan doubly linked list
- Dictionary untuk O(1) access, linked list untuk O(1) reordering

---

### 4.2 Word Ladder

**Deskripsi:**
Diberikan `beginWord`, `endWord`, dan `wordList`, temukan panjang sequence transformasi terpendek dari beginWord ke endWord. Setiap transformasi hanya boleh mengubah satu huruf, dan setiap word yang ditransformasi harus ada di wordList.

**Input:**

```python
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
```

**Output:** `5`

**Penjelasan:** Sequence: "hit" → "hot" → "dot" → "dog" → "cog"

**Hints:**

- Gunakan BFS untuk shortest path
- Build graph dari words yang differ by one character

---

### 4.3 Serialize and Deserialize Binary Tree

**Deskripsi:**
Design algorithm untuk serialize dan deserialize binary tree. Serialization adalah proses mengconvert tree ke string, deserialize adalah kebalikannya.

**Contoh:**

```python
    1
   / \
  2   3
     / \
    4   5

serialize(root) → "1,2,None,None,3,4,None,None,5,None,None"
deserialize(data) → [tree structure reconstructed]
```

**Hints:**

- Gunakan preorder/level order traversal untuk serialize
- Gunakan None marker untuk null nodes
- Deserialize dengan rekonstruksi menggunakan same traversal order

---

### 4.4 Regular Expression Matching

**Deskripsi:**
Implementasikan regex pattern matching dengan support untuk:

- `.` : Match any single character
- `*` : Match zero or more dari preceding element

**Input:** `s = "aab"`, `p = "c*a*b"`

**Output:** `True`

**Penjelasan:**

- `c*` matches zero 'c'
- `a*` matches two 'a'
- `b` matches 'b'

**Input:** `s = "mississippi"`, `p = "mis*is*p*."`

**Output:** `False`

**Hints:**

- Gunakan dynamic programming
- Create 2D DP table
- Handle `*` special case dengan care

---

### 4.5 Design a Text Editor

**Deskripsi:**
Design text editor dengan operations berikut:

- `insert(text)`: Insert text at cursor
- `delete(k)`: Delete k characters before cursor
- `cursorLeft(k)`: Move cursor k positions left
- `cursorRight(k)`: Move cursor k positions right
- `undo()`: Undo last operation
- `redo()`: Redo last undone operation

**Requirements:**

- Semua operations harus efficient
- Support unlimited undo/redo

**Hints:**

- Gunakan dua stacks untuk left dan right dari cursor
- Stack terpisah untuk undo/redo history
- Command pattern untuk encapsulate operations

---

## Level 5: Expert (System Design & Optimization)

### 5.1 Design URL Shortener

**Deskripsi:**
Design sistem URL shortener seperti bit.ly dengan features:

- `encode(long_url)`: Convert long URL ke short URL
- `decode(short_url)`: Convert short URL kembali ke long URL

**Requirements:**

- Short URL harus unik dan short (6-7 characters)
- Handle collision
- O(1) encode dan decode time

**Pertimbangan:**

- Base62 encoding (a-z, A-Z, 0-9)
- Counter vs Random generation
- Database design
- Scalability

---

### 5.2 Design In-Memory File System

**Deskripsi:**
Implementasikan in-memory file system dengan operations:

- `ls(path)`: List files/directories di path
- `mkdir(path)`: Create directory
- `addContentToFile(path, content)`: Add content ke file
- `readContentFromFile(path)`: Read content dari file

**Contoh:**

```python
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
fs.readContentFromFile("/a/b/c/d")  # returns "hello"
fs.ls("/a/b")  # returns ["c"]
```

**Hints:**

- Gunakan trie/tree structure
- Node bisa represent directory atau file
- Handle path parsing dengan care

---

### 5.3 Task Scheduler dengan Dependencies

**Deskripsi:**
Design task scheduler yang dapat handle tasks dengan dependencies. Setiap task memiliki:

- ID unik
- Duration
- List of dependency task IDs yang harus selesai dulu

Return minimum time untuk complete semua tasks dengan parallel execution.

**Input:**

```python
tasks = [
    {"id": 1, "duration": 5, "deps": []},
    {"id": 2, "duration": 3, "deps": [1]},
    {"id": 3, "duration": 4, "deps": [1]},
    {"id": 4, "duration": 2, "deps": [2, 3]}
]
```

**Output:** `12`

**Penjelasan:** Task 2 dan 3 bisa parallel setelah task 1 selesai.

**Hints:**

- Topological sort untuk dependency resolution
- Calculate critical path
- Dynamic programming untuk optimization

---

## Tips untuk Progress ke Advanced Level

### 1. **Master Big O Notation**

Pahami time dan space complexity dari setiap solution Anda.

### 2. **Practice Pattern Recognition**

Kenali common patterns:

- Sliding Window
- Two Pointers
- Fast & Slow Pointers
- Binary Search
- BFS/DFS
- Dynamic Programming
- Backtracking

### 3. **Study Data Structures**

Dalam order priority:

1. Arrays & Strings
2. Hash Tables (Dict)
3. Stacks & Queues
4. Linked Lists
5. Trees & Graphs
6. Heaps
7. Tries

### 4. **Write Clean Code**

- Gunakan meaningful variable names
- Add comments untuk complex logic
- Follow PEP 8 style guide
- Write unit tests

### 5. **Debug Effectively**

- Print intermediate values
- Use debugger (pdb)
- Test edge cases
- Think about error handling

### 6. **Review & Optimize**

Setelah solve problem:

- Bisakah lebih efficient?
- Bisakah lebih readable?
- Edge cases apa yang missed?

---

## Resources untuk Lanjut Belajar

1. **LeetCode** - Practice problems dengan berbagai difficulty
2. **HackerRank** - Structured learning paths
3. **Project Euler** - Math-focused programming challenges
4. **Real Python** - In-depth Python tutorials
5. **Python Documentation** - Official docs adalah sumber terbaik

---

## Tracking Progress Anda

Buat file terpisah untuk solutions Anda dengan format:

```
solutions/
├── level_1/
│   ├── 1.1_fizzbuzz.py
│   ├── 1.2_palindrome.py
│   └── 1.3_count_vowels.py
├── level_2/
│   ├── 2.1_two_sum.py
│   └── ...
└── level_3/
    └── ...
```

Selamat berlatih! Remember: **Consistency beats intensity.** Lebih baik 1 jam setiap hari daripada 7 jam sekali seminggu. 🚀

