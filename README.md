# Diffusion_Coefficient_Gromacs_script
Here is a script that can be used to plot the results of a .xvg file exported from Gromacs so you wont need other plot programms such as Grace or Gnuplot
Give the command $ gmx msd -f input_md.trr -s input_md.tpr -n index.ndx -o output.xvg
Then type the number that contains the type of molecules you want to measure diffusion coefficient and then Ctrl + D.
Open the .xvg file in a text editor and replace (usually Ctrl + H) the @ symbols with # symbols.
Finally run the script with $ python diffusion_coefficient_script.py
output.xvg file is provided for testing.
