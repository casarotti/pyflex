#! /usr/bin/env python
"""
Convert empty IPython notebook to a sphinx doc page.
"""
import io
import os
import sys

from IPython.nbformat import current


def clean_for_doc(nb):
    """
    Cleans the notebook to be suitable for inclusion in the docs.
    """
    new_cells = []
    for cell in nb.worksheets[0].cells:
        # Remove the pylab inline line.
        if "input" in cell and cell["input"].strip() == "%pylab inline":
            continue
        # Remove output resulting from the stream/trace method chaining.
        if "outputs" in cell:
            outputs = [_i for _i in cell["outputs"] if "text" not in _i or
                       not _i["text"].startswith("<obspy.core")]
            cell["outputs"] = outputs
        new_cells.append(cell)
    nb.worksheets[0].cells = new_cells
    return nb


def strip_output(nb):
    """
    strip the outputs from a notebook object
    """
    for cell in nb.worksheets[0].cells:
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'prompt_number' in cell:
            cell['prompt_number'] = None
    return nb


def convert_nb(nbname):
    os.system("runipy --o %s.ipynb --matplotlib --quiet" % nbname)
    os.system("rm -rf ./index_files")

    filename = "%s.ipynb" % nbname
    with io.open(filename, 'r', encoding='utf8') as f:
        nb = current.read(f, 'json')
    nb = clean_for_doc(nb)
    print "Writing to", filename
    with io.open(filename, 'w', encoding='utf8') as f:
        current.write(nb, f, 'json')

    os.system("ipython nbconvert --to rst %s.ipynb" % nbname)

    filename = "%s.ipynb" % nbname
    with io.open(filename, 'r', encoding='utf8') as f:
        nb = current.read(f, 'json')
    nb = strip_output(nb)
    print "Writing to", filename
    with io.open(filename, 'w', encoding='utf8') as f:
        current.write(nb, f, 'json')


if __name__ == "__main__":
    for nbname in sys.argv[1:]:
        convert_nb(nbname)
