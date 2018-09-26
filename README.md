# split_file_obo

Split a obo file in a __n__ number of files with __t__ numbers of terms Program written in python 3

## Usage

### Run locally 

No external dependencies required

Split a __input_file.obo__ in __n__ numbers of sub files with __t__ numbers of terms each one. The program finish when the __n__ sub files are written or all terms are written. The result are output_file-1.obo ... to ... output_file-n.obo

```
cd split_file
python3 split_file.py -i input_file.obo -n 10 -t 1000 -o output_file.obo
```

Split a __input_file.obo__ in each sub files with __t__ numbers of terms each one. The program finish when all terms are written. The result are output_file-1.obo ... to ... output_file-n.obo

```
cd split_file
python3 split_file.py -i input_file.obo -t 1000 -o output_file.obo
```