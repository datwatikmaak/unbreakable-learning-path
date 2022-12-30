import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    indent = True
    formatted_poem = []

    for line in poem.split("\n"):
        if not line:
            indent = False
            continue

        if not indent:
            formatted_line = textwrap.dedent(line)
            indent = True
        else:
            formatted_line = textwrap.indent(line.strip(), prefix=" " * INDENTS)

        formatted_poem.append(formatted_line)

    print("\n".join(formatted_poem))
