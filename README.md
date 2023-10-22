<!---->

<div align="center">
 <h1 align="center"> <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
    <br>SCC</h1>
    <h3>A basic C compiler written in Python.</h3>
    <h3>Developed with the software and tools below.</h3>
</div>

<div align="center">
  <a href="https://skillicons.dev">
    <img src=https://skillicons.dev/icons?i=,py,git,github,md,/>
  </a>
</div>



---

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [📦 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [⚙️ Modules](#modules)
- [🚀 Getting Started](#-getting-started)
    - [🔧 Installation](#-installation)
    - [🤖 Running SCC](#-running-SCC.git)
    - [🧪 Tests](#-tests)

---

## 📍 Overview

Welcome to SCC - a basic C compiler written in Python.

---

## 📦 Features

- **Token Verification**: The compiler performs lexical analysis to verify and validate tokens in the source code.

- **Expressions**: It supports the parsing and evaluation of C expressions, including arithmetic and logical operations.

- **Variables**: SCC handles the declaration and management of variables, ensuring proper scoping.

- **Conditional Statements**: The compiler supports conditional statements such as `if`, `else if`, and `else`, allowing
  for branching in the code.

- **Loops**: SCC provides support for various types of loops, including `while` and `for`, enabling repetitive execution
  of code blocks.

- **Functions**: The compiler allows you to define and call functions, including support for recursive functions.

- **Pointers**: SCC handles pointers, allowing you to work with memory addresses and data manipulation.

- **Arrays**: It supports the declaration and manipulation of arrays, including multidimensional arrays {(array[i])[j]}.

- **standard library**: 
  - **malloc(int n)**
  - **free()**
  - **print_num(int n)**: (without newline)
  - **printl_num(int n)**: (with newline)

---

## 📂 Repository Structure

```
└── SCC.git/
    ├── .gitignore
    ├── README.md
    ├── src/
    │   ├── __init__.py
    │   ├── cLexer.py
    │   ├── cParser.py
    │   ├── generator.py
    │   ├── scc.py
    │   ├── sem_ana.py
    │   └── symbol_table.py
    ├── std/
    │   └── lib.c
    └── tests/
```

---

## ⚙️ Modules

<details ><summary>Src</summary>

| File                                                                                | Summary                                 |
|-------------------------------------------------------------------------------------|-----------------------------------------|
| [scc.py](https://github.com/Lekiios/SCC.git/blob/main/src/scc.py)                   | The main entry point of SCC.GIT.        |
| [cLexer.py](https://github.com/Lekiios/SCC.git/blob/main/src/cLexer.py)             | The lexical analysis module for C code. |
| [cParser.py](https://github.com/Lekiios/SCC.git/blob/main/src/cParser.py)           | The parser module for C code.           |
| [symbol_table.py](https://github.com/Lekiios/SCC.git/blob/main/src/symbol_table.py) | 	Module for managing the symbol table.  |
| [sem_ana.py](https://github.com/Lekiios/SCC.git/blob/main/src/sem_ana.py)           | Semantic analysis module for C code.    |
| [generator.py](https://github.com/Lekiios/SCC.git/blob/main/src/generator.py)       | The code generation module for SCC.GIT. |

</details>

<details ><summary>Std</summary>

| File                                                            | Summary                                 |
|-----------------------------------------------------------------|-----------------------------------------|
| [lib.c](https://github.com/Lekiios/SCC.git/blob/main/std/lib.c) | Standard C library support for SCC.GIT. |
|

</details>

---

## 🚀 Getting Started

***Dependencies***

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Python 3.10`

`- ℹ️ pytest (look in next section for installation)`

### 🔧 Installation

1. Clone the SCC repository:

```sh
git clone https://github.com/Lekiios/SCC.git
```

2. Change to the project directory:

```sh
cd SCC
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### 🤖 Running SCC

Be sure to be located at the root of the project.

```sh
python3 src/scc.py file1.c file2.c  ...
```

Files has to be ordered correctly.\
Declaration before usage.

### 🧪 Tests

```sh
cd tests
pytest
```

[↑ Return](#Top)

---
