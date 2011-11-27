class MarkUp(object):
    def __init__(self, text):
        self.lines = text.splitlines()
        self.lines = [l+'\n' for l in self.lines]
    def translate(self, format="HTML"):
        lines = self.lines
        res = ''

        state = "START"
        for line in lines:
            if state == "START":
                if line == '\n':
                    pass
                else:
                    res+= "<h1>%s</h1>\n" % line[:-1]
                state = "READING"

            elif state == "READING":
                if line == '\n':
                    pass
                elif line.startswith(" -"):
                    current_list = [line]
                    state = "LIST"
                else:
                    line_stack = [line]
                    state = "FIRST_LINE"

            elif state == 'FIRST_LINE':
                if line != '\n':
                    current_paragraph = line_stack
                    current_paragraph.append(line)
                    state = 'PARAGRAPH'
                else:
                    res += "<h2>%s</h2>\n" % line_stack[0][:-1]
                    state = 'READING'

            elif state == "LIST":
                if line.startswith(" -"):
                    current_list.append(line)
                elif line == '\n':
                    pass
                else:
                    res += "<ul>%s</ul>" % ''.join("<li>%s</li>\n" % l[3:-1] for l in current_list)
                    state = "READING"

            elif state == "PARAGRAPH":
                if line != '\n':
                    current_paragraph.append(line)
                else:
                    res += "<p>%s</p>\n" % ''.join(current_paragraph)
                    state = 'READING'

        return res

