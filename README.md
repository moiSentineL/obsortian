# obsortian

<div align="center">

<p>sort and find markdown files by yaml frontmatter.</p>
<p><i>thank you necessity.</i></p>
</div>

---

Tested only on an [Obsidian](https://obsidian.md) vault, but may be used for other stuff that uses markdown and YAML frontmatter.

## Logic:
- Checks for files on a given path
- Removes any "exclusions"
- Checks for properties (if they exist) on the frontmatter
- Prints/ writes the files.

### Current usage:
For now, it searches the `tags` and `status` properties in the frontmatter, finds the files and returns a *random* list of 20 files from it. (this is more of a personal thing, working to generalise it.)

You can set up which `tag` or `status` to look for in the `conf.json`, and set up the vault path and excluded folders:

```json
{
    "vault_path": "/home/nibir/Documents/obsidian_vault/",
    "exclusions": ["Templates", "Scripts"], // excluded folder must be in array
    "tag": "Study",
    "status": "needs work"
}
```

## Installation

```bash
git clone https://github.com/moiSentineL/obsortian.git

cd obsortian

python finder.py
```

## Contribution

fix the code, goddamit.

