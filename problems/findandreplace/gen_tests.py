with open("tests/1.in", "w") as f:
    f.write("""\
essorPROFprof
my profprofessoressor is a very friendly person
""")

# Special case: -1
with open("tests/2.in", "w") as f:
    f.write("""\
meprofessorme
professor me professor
""")

# Special case: no replacement
with open("tests/3.in", "w") as f:
    f.write("""\
meprofessorme
blorp goop gab
""")

# Special case: largest replacement and many replacements
with open("tests/4.in", "w") as f:
    f.write("PROFESSORZZprofesso\n")
    f.write("professor" + "r" * 2991 + "\n")

# One more case, getting smaller
with open("tests/5.in", "w") as f:
    f.write("""\
orpr
professprofessprofessorofessorofessorofessor professprofessprofessorofessorofessorofessor
""")

# Another case: spaces between professor
with open("tests/6.in", "w") as f:
    f.write("""\
b
prof essor prof essor b prof professor
""")

# And another -1 case
with open("tests/7.in", "w") as f:
    f.write("""\
AprofessorBprofessorC
AprofessorBprofessorC hell yeah
""")
