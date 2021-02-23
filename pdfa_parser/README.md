# Avisleser PDF-A parser

Avisleser is a CLI tool to extract text from PDFs that have been digitally produced (it does not work well with OCR'ed embedded text). Since PDFs only have spatial information about characters in a canvas (page), the script uses an heuristic to recreate the reading flow. In order to do that, two different engines can be used:

- PDFMiner (`pdf2txt`), which builds words character by character and then lines word by word. Lines are then grouped in blocks and blocks are grouped together depending on closeness. How this decision are made can be somewhat modified by tuning the parameters `--line_margin` and `--boxes_flow`.
- MuPDF (`mupdf`), which is a C-based PDF reader and as such builds a representation of the page in memory. In some cases, it provides a better reading flow than PDFMiner, but it does not accept much tweaking.

Moreover, the script will run two passes:

1. First, it collects information on the most frequent font family and size.
2. Then, it uses this pair of font family and size to filter out the rest.

The final output will resemble the same structure as the input, but renaming files to end with "*.txt", adding double break lines when appropriate.


Usage:

```bash
$ python avisleser.py --help
usage: avisleser.py [-h] [--no_overwrite] [--split_sentences] [--n_jobs N_JOBS] [--timeout TIMEOUT] [--line_margin LINE_MARGIN]
                    [--boxes_flow BOXES_FLOW] [--skip_empty] [--no_all_texts] [--engine ENGINE] [--progress_file PROGRESS_FILE] [--total TOTAL]
                    pdfs_dir pdfs_glob output_dir
```

Positional arguments:

- `pdfs_dir`. Directory with the pdfs files
- `pdfs_glob`. Glob for the directory with the pdfs files
- `output_dir`. Directory to store output files

Optional arguments:

- `-h`, `--help`. Show this help message and exit
- `--no_overwrite`. Do not overwrite outputs
- `--split_sentences`. Split sentences
- `--n_jobs N_JOBS`. Number of multiprocessing jobs. Defaults to 1 (-1 for max)
- `--timeout TIMEOUT`. Parsing timeout in seconds. Defaults to 30
- `--line_margin LINE_MARGIN`. Line margin for PDFMiner.six LTParams. Defaults to 0.25
- `--boxes_flow BOXES_FLOW`. Boxes flow for PDFMiner.six LTParams. Defaults to -0.8
- `--skip_empty`. Ignore files if the extraction produced an empty text
- `--no_all_texts`. Do not extract from texts in or captioning images. If set, it might mess with complicated layouts, specially when using MuPDF as an engine
- `--engine ENGINE`. Options are "pdf2txt" (default) for PDFMiner or "mupdf" for MuPDF
- `--progress_file PROGRESS_FILE`. Save the progress to a local file
- `--total TOTAL`. Total number of files to process. Calculated if not passed

Example usage:

- Extract text from PDFs in `./pdfs/*.pdf`, place them in `./outputs`, set a maximum processing time of 60 seconds, and process them using 8 cores

```bash
$ avisleser.py ./pdfs "*.pdf" ./outputs --timeout 60 --n_jobs 8
```

- Extract text using `pdf2txt` (PDFMiner) from PDFs in `./pdfs/**/**/**/*.pdf`, place them in `./pdf/pdf2txt/2020`, set a maximum processing time of 60 seconds, process them using 48 cores, do not overwrite files if they exist already, save the progress in a file named `avisleser.pdf2txt.log`, and use as a total for the progress bar 880,235 instead of calculating it.

```bash
$ python avisleser.py pdf/2020 "**/**/**/*.pdf" pdf/pdf2txt/2020 --n_jobs 48 --timeout 60 --engine pdf2txt --no_overwrite --progress_file avisleser.pdf2txt.log --total 880235
```

- When using MuPDF, sometimes parsing fails with a segmentation fault (`SIGSEGV`), making the script to fail as well. To avoid stopping the processing, you could set a fixed `--progress_file` so avisleser can retry while ignoring the problematic PDF file. One possible option is to make use of both `while` and `!!` in bash:

```bash
$ python avisleser.py pdf/2020 "**/**/**/*.pdf" pdf/mupdf/2020 --n_jobs 48 --timeout 60 --engine mupdf --no_overwrite --progress_file avisleser.mupdf.log --total 880235
$ while [ $? -ne 0 ]; do (echo "Restarting..." && !! ); done
```

Or all together:

```bash
$ python avisleser.py pdf/2020 "**/**/**/*.pdf" pdf/mupdf/2020 --n_jobs 48 --timeout 60 --engine mupdf --no_overwrite --progress_file avisleser.mupdf.log --total 880235; while [ $? -ne 0 ]; do (echo "Restarting..." && !! ); done
```
