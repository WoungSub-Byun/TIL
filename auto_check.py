import os
from shutil import copymode
import string

content = "# Summary\n\n"

def get_components(path: str, depth: int):
    components = sorted(os.listdir(path))
    for component in components:
        if component[0] == '.' or ('.' in component and (not is_md(component))):
            continue
        elif component == 'README.md':
            continue
        elif component == 'Image':
            continue
        elif is_md(component):
            append_content(path, component, depth, "md")
        else:
            append_content(path, component, depth, "dir")
            depth += 1
            get_components(path+component+'/', depth) # ./CS/, 1
            depth -= 1

def is_md(title: str):
    return True if title[-2:] == 'md' else False

def append_content(path: str, component: str, depth: int, type: str):
    global content
    if component == 'SUMMARY.md':
        text = "    " * depth + "- [{}]({})\n".format("Intro", path+component)
    if type == "dir":
        text = "    " * depth + "- [{}]({}/README.md)\n".format(component, path+component)
    elif type == "md": 
        component = component if component.isupper() else string.capwords(component)
        text = "    " * depth + "- [{}]({})\n".format(component, path+component)
    content+=text
    

def run():
    get_components('./', 0)
    with open('./SUMMARY.md', 'w') as f:
        f.write(content)

run()