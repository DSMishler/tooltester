"""
~/dev/tool4ise$ grep -r tool4ise .
./middleware/invoke:/usr/bin/invoke_app "$@" -C "start_jupyter -A -T @tool tool4ise.ipynb" -t tool4ise \
./bin/tool4ise.py:    dirname = os.path.expanduser('~/.local/share/tool4ise')
./bin/tool4ise.py:    dirname = os.path.expanduser('~/.local/share/tool4ise')
./bin/tool4ise.py:        full_path = os.path.expanduser("~/data/results/.submit_cache/tool4ise")
./bin/tool4ise.py:            full_path = os.path.join(cachedir, "tool4ise")
./bin/tool4ise.py:        os.system("submit  mail2self -s 'nanoHUB tool4ise' -t 'Your Run completed.'&")
./bin/tool4ise.py:            s.run(run_name, "-v ncn-hub_M@brown -n 8 -w 1440 tool4ise-r7 config.xml")   # "-r7" suffix??
./bin/tool4ise.py:                        cachename='tool4ise',
./bin/tool4ise.py:                            cachename='tool4ise',
./README.md:# tool4ise
./tool4ise.ipynb:    "import tool4ise"
./tool4ise.ipynb:    "tool4ise.gui"
"""
import sys
import shutil
import os


num_args = len(sys.argv)
print('num_args=',num_args)
if (num_args < 2):
    print("Usage: %s <new tool name>")
    sys.exit(1)
toolname = sys.argv[1]
print('toolname=',toolname)


with open('middleware/invoke', 'r') as myfile:
    new_text = myfile.read().replace('tool4ise', toolname)
with open('middleware/invoke', 'w') as myfile:
    myfile.write(new_text)

#--------------
old_file = os.path.join("bin", 'tool4ise.py')
new_file = os.path.join("bin", toolname + '.py')
shutil.move(old_file, new_file)
print('Renaming ',old_file, ' to ',new_file)

print('Replacing toolname in ',new_file)
with open(new_file, 'r') as myfile:
    new_text = myfile.read().replace('tool4ise', toolname)
with open(new_file, 'w') as myfile:
    myfile.write(new_text)

#--------------
old_file = 'tool4ise.ipynb'
new_file = toolname + '.ipynb'
shutil.move(old_file, new_file)
print('Renaming ',old_file, ' to ',new_file)

print('Replacing toolname in ',new_file)
with open(new_file, 'r') as myfile:
    new_text = myfile.read().replace('tool4ise', toolname)
with open(new_file, 'w') as myfile:
    myfile.write(new_text)


#--------------
"""
In /data:
python xml2jupyter.py PhysiCell_settings.xml
Copy the generated user_params.py to ../bin
"""
print('Running xml2jupyter on your .xml file')
os.chdir("data")
os.system("python xml2jupyter.py PhysiCell_settings.xml")
new_file = os.path.join("..","bin")
shutil.copy("user_params.py", new_file)

try:
    print("Trying to import hublib.ui")
    import hublib.ui
except:
    print("hublib.ui is not found, will try to install it.")
    os.system("pip install -U hublib")

