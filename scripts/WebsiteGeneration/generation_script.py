#Script that will loop through Tutorials folder, 
import os
import glob
PATH = "./adl_tutorials/Tutorials/"
ADL_PATH = "./adl"

for chapter in os.listdir(PATH):
	if(not os.path.isdir(PATH+chapter)):
		continue

	for page in os.listdir(PATH+chapter):
		ipynb_folder = PATH+chapter+"/"+page
		if(not os.path.isdir(ipynb_folder)):
			continue
		# print("------------>"+str(glob.glob(ipynb_folder+"/*.ipynb")))
		title = glob.glob(ipynb_folder+"/*.ipynb")[0].split('/')[-1].split('.')[0]
		print(ipynb_folder+"/"+title)
		os.system(f'jupyter nbconvert --to html "{ipynb_folder}/{title}.ipynb"')
		os.remove(f"{ipynb_folder}/{title}.ipynb")
		md_file = f"---\nlayout: default\ntitle: {title}\nparent: {chapter}\ngrand_parent: Adversarial Deep Learning\n---"
		with open(f"{PATH+chapter}/{title}.md","w") as f:
			f.write(md_file+f'\n{{% include_relative {page}/{title}.html %}}')
	index_md = f"---\nlayout: default\ntitle: {chapter}\nparent: Adversarial Deep Learning\nhas_children: true\n---"
	with open(f"{PATH+chapter}/index.md","w") as f:
			f.write(index_md)