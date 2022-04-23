import os

def convertIt(infile, outfile):

  in_lines = [line.rstrip('\n') for line in open(infile)]
  print("in_lines len: %i\n" % len(in_lines))

  fw = open(outfile, 'w')
  id = ""
  smiles = ""
  read_mol = True
  for line in in_lines:
    if read_mol:
      if id == "":
        id = line
        continue
      if line == "> <PUBCHEM_OPENEYE_CAN_SMILES>":
        smiles = "x"
        continue
      if smiles == "x":
        smiles = line
        read_mol = False
    
    if line == "$$$$":
      line_out = id + "," + smiles 
      print(line_out)
      fw.write(line_out + "\n")
      id = ""
      smiles = ""
      read_mol = True
      continue
  fw.close()

#
# Main
#

infile = "data/dataset.sdf"
outfile = "data/dataset.csv"
if os.path.isfile(outfile):
  os.remove(outfile)

convertIt(infile, outfile)