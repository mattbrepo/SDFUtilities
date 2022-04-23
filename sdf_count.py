import os

def countMols(infile):
  all_lines = 0
  mols = 0
  with open(infile) as f:
    for line in f:
      all_lines += 1
      if line.strip() == "$$$$":
        mols += 1
  print("all lines: %i" % all_lines)
  print("molecules: %i" % mols)

#
# Main
#

infile = "data/dataset.sdf"

countMols(infile)