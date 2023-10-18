# SCC
Simple C Compiler

###### Dev Prerequisites :
- _python 3.10_
- _pytest_

## Token Types Description 

- Constant: {type: "const", value: string(number)}
- Identifier: {type: "id", value: string}
- Add: {type: "+"}
- Minus: {type: "-"}
- Multiply: {type: "*"}
- Divide: {type: "/"}
- Modulo: {type: "%"}
- Affectation: {type: "="}
- Equal: {type: "=="}
- Not: {type: "!"}
- Not Equal: {type: "!="}
- Inferior: {type: "<"}
- Inferior or Equal: {type: "<="}
- Superior: {type: ">"}
- Superior or Equal: {type: ">="}
- Or: {type: "||"}
- And: {type: "&&"}
- Reference: {type: "&"}
- LParent: {type: "("}
- RParent: {type: ")"}
- LBracket: {type: "["}
- RBracket: {type: "]"}
- LCurly-Bracket: {type: "{"}
- RCurly-Bracket: {type: "}"}
- Comma: {type: ","}
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
