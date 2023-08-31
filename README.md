# SCC
Simple C Compiler

## Token Types Description 

- Constant: {type: "const", value: string(number)}
- Identifier: {type: "id", value: string}
- Add: {type: "+"}
- Minus: {type: "-"}
- Multiply: {type: "*"}
- Divide: {type: "/"}
- Affectation: {type: "="}
- Equal: {type: "=="}
- LParent: {type: "("}
- RParent: {type: ")"}
- Not: {type: "!"}
- Semicolon: {type: ";"}
- End Of File (EOF): {type: "EOF"}

#### Keywords

- int: {type: "int"}
- for: {type: "for"}
- while: {type: "while"}
- if: {type: "if"}
- else: {type: "else"}
- break: {type: "break"}
- continue: {type: "continue"}
- return: {type: "return"}