# Pluxml-to-Markdown
A Python script to convert PluXml posts to Markdown

This script currently only converts PluXml posts in simple Markdown and for GravCMS which may be okay for some other CMS based on Markdown.

## Installation

```
git clone https://github.com/KillianKemps/Pluxml-to-Markdown
cd Pluxml-to-Markdown
pip install -U requirements.txt
```

## Usage

```
python main.py [pluxml-data-folder] [converter]
```

*All converted files will be outputed in `converted_posts` in the script folder*


### Available converters
  - `simple` will simply output all the files in markdown

  - `grav` will create a folder for each converted post and import your images too.

**Caution: importing comments and categories are not supported**

## Contribute

If you wish to add some other converter, simply edit the `converter.py` file and add you converter by inspiring yourself with existing ones. You will then need to add it as an option for argparse in `main.py` and `controller.py` to be used.

Don't be shy! If you need help to use or contribute, don't hesitate to contact me on Github. If I see that people are using it, I may improve the way how it work. (This was just a one-day project for a personal need)
