Adrianna is writing an essay, and wants to remove all mention of "professor" and replace it with her Professor's name.

But because this essay has a strict length limit, Adrianna wants to know how long the new essay will be after replacement.

In particular, while the string `professor` (case-sensitive) is still in the string, she will replace the first `professor` with the professor's name.

## Input

Input will start with a single string ~s~, the professor's name. ~s~ will only contain characters a-z and A-Z.
The next line will contain Adrianna's essay ~e~, in full. This will contain characters a-z, A-Z and whitespace (spaces and tabs).

## Output

Output a single integer, the final length of Adrianna's essay. If Adrianna's string replacement algorithm will never terminate (`professor` will always be in the essay, no matter how many replacements), output `-1` instead.

## Constraints

~1 \leq |s| \leq 20~
~1 \leq |e| \leq 3000~

## Example run

Input
```
essorPROFprof
my profprofessoressor is a very friendly person
```

Output
```
59
```

Explanation

The replacements cause the following interaction:

* `my profprofessoressor is a very friendly person` becomes
* `my professorPROFprofessor is a very friendly person` becomes
* `my essorPROFprofPROFprofessor is a very friendly person` becomes
* `my essorPROFprofPROFessorPROFprof is a very friendly person`.

Which has length 59.
