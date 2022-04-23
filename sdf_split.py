import os

def saveMol(lines, mols, out_prefix, out_count):
  print("save file %i: %i" % (out_count, mols))
  with open(out_prefix + str(out_count) + '.sdf', 'w') as f:
    for item in lines:
      f.write("%s" % item)

def splitMols(in_file, mol_per_file, out_prefix):
  lines = []
  mols = 0
  out_count = 1
  with open(in_file) as f:
    for line in f:
      lines.append(line)
      if line.strip() == "$$$$":
        mols += 1

      if mols >= mol_per_file:
        saveMol(lines, mols, out_prefix, out_count)
        out_count += 1
        lines = []
        mols = 0

  if mols > 0:
    saveMol(lines, mols, out_prefix, out_count)

#
# Main
#

in_file = "data/dataset.sdf"
mol_per_file = 50
out_prefix = "data/dataset_out_"

splitMols(in_file, mol_per_file, out_prefix)