# Miscellaneous [I]

You want to know how many ways you can organise ~n~ `(` and `)` brackets so the result string is *balanced*, that is, so that every closing `)` bracket is preceded by an accompanying opening `(` bracket somewhere earlier in the string.

Examples of all valid organisations with ~n=3~:

* `((()))`
* `()()()`
* `(())()`
* `()(())`
* `(()())`

Examples of invalid organisations with ~n=3~:

* `())(()`
* `)()()(`
* `(()))(`

## Input

Input will consist of a single integer ~n~, representing the number of open and closed brackets we want to organise

## Output

Output should be a single integer, representing the number of unique strings of balanced parenthesis of length ~n~. Since this number could be quite large, output the answer modulo ~10^9+7~

## Constraints

* ~1 \leq n \leq 1000~

## Example

#### Input
```
3
```
#### Output
```
5
```

#### Input
```
10
```
#### Output
```
16796
```
