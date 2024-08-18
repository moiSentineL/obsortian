import os
import re
import yaml
import json

class finder:
    def __init__(self):
        with open("conf.json", "r") as f:
            self.data = json.load(f)

    def parse_frontmatter(self, content):
        frontmatter = {}
        if (match := re.match(r'^---\n(.*?)\n---', content, re.DOTALL)):
            try:
                frontmatter = yaml.safe_load(match.group(1))
            except yaml.YAMLError:
                pass
        return frontmatter

    def get_matching_files(self):
        matching_files = []

        for root, _, files in os.walk(vault_path := self.data["vault_path"]):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(os.path.join(root, file), vault_path)

                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    frontmatter = self.parse_frontmatter(content)
                    
                    if 'tags' in frontmatter and 'status' in frontmatter:
                        tags = frontmatter['tags']
                        status = frontmatter['status']

                        bruh = ' '.join(map(str, tags)) if isinstance(tags, list) else tags
                        huh = ' '.join(map(str, status)) if isinstance(status, list) else status
                        
                        if str(type(bruh)) != "<class 'NoneType'>" and self.data["tag"] in bruh and self.data["status"] in huh:
                            print(relative_path)
                            # matching_files.append(relative_path)

def main():
    matching_files = finder.get_matching_files()
    
    print(matching_files)
    # output = '\n'.join(file_path for file_path, _ in matching_files)
    
    # with open("test.txt", 'w', encoding='utf-8') as f:
    #     f.write()
    # print (matching_files)
    # print(f"Created file 'study_needs_work.txt' with {len(matching_files)} entries.")

if __name__ == "__main__":
    finder().get_matching_files()
    # main()
    # print(conf()["tag"])