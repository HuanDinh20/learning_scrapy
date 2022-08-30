"""
As the old computer science joke goes: “Let’s say you have a problem, and you decide
to solve it with regular expressions. Well, now you have two problems.”
Rules:
1.
[A-Za-z0-9\._+]+ :The regular expression shorthand is pretty smart. For
example, it knows that “A-Z” means “any uppercase letter,
A through Z.”
2.
@: This is fairly straightforward: the @ symbol must occur in
the middle, and it must occur exactly once.
3.
[A-Za-z]+: You may use only letters in the first part of the domain
name, after the @ symbol. Also, there must be at least one
character
4.
\. You must include a period (.) before the domain name.
The backspace is used here as an escape character.
5.
(com|org|edu|net)
This lists the possible sequences of letters that can occur
after the period in the second part of an email address.
"""
