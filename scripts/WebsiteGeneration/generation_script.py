#Script that will loop through Tutorials folder, 
import os
import glob
PATH = "./adl_tutorials/Tutorials/"
ADL_PATH = "./adl"

for chapter in os.listdir(PATH):
	if(not os.path.isdir(PATH+chapter)):
		print("Skipping "+chapter)
		continue

	for page in os.listdir(PATH+chapter):
		ipynb_folder = PATH+chapter+"/"+page
		print("1)  ipynb_folder:  "+ ipynb_folder+"/\n")
		if(not os.path.isdir(ipynb_folder)):
			print("2)   Skipping "+ipynb_folder+"\n")
			continue
		print("------------>"+str(glob.glob(ipynb_folder+"/*.ipynb"))+"\n")
		title = glob.glob(ipynb_folder+"/*.ipynb")[0].split('/')[-1].split('.')[0]
		print("3)     title:  "+title+"\n")
		print("4)     ipynb_folder/title:   "+ipynb_folder+"/"+title+"\n")
		os.system(
			f'jupyter nbconvert --to html "{ipynb_folder}/{title}.ipynb" --HTMLExporter.theme=dark')
		print("5)     {ipynb_folder}/{title}.ipynb:   "+ipynb_folder+"/"+title+"\n")
		os.remove(f"{ipynb_folder}/{title}.ipynb")
		md_file = f"---\nlayout: default\ntitle: {title}\nparent: {chapter}\ngrand_parent: Adversarial Deep Learning\n---"
		print("5)  md_file:  "+md_file+"\n")
		with open(f"{PATH+chapter}/{title}.md","w") as f:
			f.write(md_file+f'\n{{% include_relative {page}/{title}.html %}}')
	index_md = f"---\nlayout: default\ntitle: {chapter}\nparent: Adversarial Deep Learning\nhas_children: true\n---"
	print("6) index_md: "+index_md+"\n")
	with open(f"{PATH+chapter}/index.md","w") as f:
			f.write(index_md)
