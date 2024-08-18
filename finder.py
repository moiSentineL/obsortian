import os
import re
import yaml
import json
import random

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

    def get_matching_files(self) -> list:
        matching_files = []

        for root, _, files in os.walk(vault_path := self.data["vault_path"]):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(os.path.join(root, file), vault_path)

                    if any(ex in relative_path for ex in self.data["exclusions"]):
                        continue

                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    frontmatter = self.parse_frontmatter(content)
                    
                    if 'tags' in frontmatter and 'status' in frontmatter:
                        tags = frontmatter['tags']
                        status = frontmatter['status']

                        bruh = ' '.join(map(str, tags)) if isinstance(tags, list) else tags
                        huh = ' '.join(map(str, status)) if isinstance(status, list) else status
                        
                        if str(type(bruh)) != "<class 'NoneType'>" and self.data["tag"] in bruh and self.data["status"] in huh:
                            # print(relative_path)
                            matching_files.append(os.path.basename(relative_path))
        return matching_files
              
if __name__ == "__main__":
    
    matched = finder().get_matching_files()
    # with open("new", "w") as f: 
    if len(matched) >= 20:
        for _ in random.sample([file for file in matched], 20): print(_)
    # print(matched)
        print(f"Selected 20 out of {len(matched)}")
    else:
        for _ in random.sample([file for file in matched], len(matched)): print(_)
        # f.write(_) 